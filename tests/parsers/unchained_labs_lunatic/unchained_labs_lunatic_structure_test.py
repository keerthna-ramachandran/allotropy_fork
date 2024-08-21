from io import StringIO
import re

import pandas as pd
import pytest

from allotropy.allotrope.schema_mappers.adm.plate_reader.benchling._2023._09.plate_reader import (
    CalculatedDataItem,
)
from allotropy.exceptions import AllotropeConversionError
from allotropy.named_file_contents import NamedFileContents
from allotropy.parsers.unchained_labs_lunatic.constants import (
    CALCULATED_DATA_LOOKUP,
    INCORRECT_WAVELENGTH_COLUMN_FORMAT_ERROR_MSG,
    NO_DATE_OR_TIME_ERROR_MSG,
    NO_MEASUREMENT_IN_PLATE_ERROR_MSG,
)
from allotropy.parsers.unchained_labs_lunatic.unchained_labs_lunatic_reader import (
    UnchainedLabsLunaticReader,
)
from allotropy.parsers.unchained_labs_lunatic.unchained_labs_lunatic_structure import (
    _create_measurement,
    _create_measurement_group,
    create_measurement_groups,
    create_metadata,
)
from allotropy.parsers.utils.pandas import SeriesData


@pytest.mark.parametrize(
    "wavelength,absorbance_value,sample_identifier,location_identifier,well_plate_identifier",
    [
        (245, 590, "Sample Name 1", "plateID1", "A1"),
        (230, 90, "Sample Name 2", "plateID2", "A3"),
        (450, 34.9, "Sample Name 3", "plateID3", None),
    ],
)
@pytest.mark.short
def test__create_measurement(
    wavelength: int,
    absorbance_value: float,
    sample_identifier: str,
    location_identifier: str,
    well_plate_identifier: str,
) -> None:
    wavelength_column = f"A{wavelength}"
    well_plate_data = {
        wavelength_column: absorbance_value,
        "Sample name": sample_identifier,
        "Plate ID": well_plate_identifier,
        "Plate Position": location_identifier,
    }
    measurement = _create_measurement(
        SeriesData(pd.Series(well_plate_data)), wavelength_column, []
    )

    assert measurement.detector_wavelength_setting == wavelength
    assert measurement.absorbance == absorbance_value
    assert measurement.sample_identifier == sample_identifier
    assert measurement.location_identifier == location_identifier
    assert measurement.well_plate_identifier == well_plate_identifier


@pytest.mark.short
def test__create_measurement_with_no_wavelength_column() -> None:
    well_plate_data = SeriesData(
        pd.Series(
            {
                "Sample name": "dummy name",
                "Plate ID": "some plate",
                "Plate Position": "B3",
            }
        )
    )
    wavelength_column = "A250"
    msg = NO_MEASUREMENT_IN_PLATE_ERROR_MSG.format(wavelength_column)
    with pytest.raises(AllotropeConversionError, match=msg):
        _create_measurement(well_plate_data, wavelength_column, [])


@pytest.mark.short
def test__create_measurement_with_incorrect_wavelength_column_format() -> None:
    msg = INCORRECT_WAVELENGTH_COLUMN_FORMAT_ERROR_MSG
    well_plate_data = SeriesData(pd.Series({"Sample name": "dummy name"}))
    with pytest.raises(AllotropeConversionError, match=re.escape(msg)):
        _create_measurement(well_plate_data, "Sample name", [])


@pytest.mark.short
def test__get_calculated_data_from_measurement_for_unknown_wavelength() -> None:
    calculated_data: list[CalculatedDataItem] = []
    well_plate_data = {
        "Sample name": "dummy name",
        "Plate ID": "some plate",
        "Plate Position": "B3",
        "A240": 0.5,
        "A260": 0,
        "A260 Concentration (ng/ul)": 4.5,
        "Background (A260)": 0.523,
    }
    _create_measurement(SeriesData(pd.Series(well_plate_data)), "A240", calculated_data)

    assert not calculated_data


@pytest.mark.short
def test__get_calculated_data_from_measurement_for_A260() -> None:  # noqa: N802
    calculated_data: list[CalculatedDataItem] = []
    well_plate_data = {
        "Sample name": "dummy name",
        "Plate ID": "some plate",
        "Plate Position": "B3",
        "A260": 34.5,
        "A260 Concentration (ng/ul)": 4.5,
        "Background (A260)": 0.523,
        "A260/A230": 2.5,
        "A260/A280": 24.9,
    }
    wavelength = "A260"
    _create_measurement(
        SeriesData(pd.Series(well_plate_data)), wavelength, calculated_data
    )

    calculated_data_dict = {data.name: data for data in (calculated_data or [])}

    for item in CALCULATED_DATA_LOOKUP[wavelength]:
        if item["column"] in well_plate_data:
            calculated_data_item = calculated_data_dict[item["name"]]
            assert calculated_data_item.value == well_plate_data[item["column"]]


@pytest.mark.short
def test_create_well_plate() -> None:
    analytical_method_identifier = "dummy method"
    date = "17/10/2016"
    time = "7:19:18"
    plate_data = {
        "A250": 23.45,
        "Sample name": "dummy name",
        "Plate Position": "some plate",
        "Application": analytical_method_identifier,
        "Date": date,
        "Time": time,
    }
    well_plate = _create_measurement_group(
        SeriesData(pd.Series(plate_data)), ["A250"], [], None
    )
    assert well_plate.analytical_method_identifier == analytical_method_identifier
    assert well_plate.measurement_time == f"{date} {time}"
    assert well_plate.measurements[0].absorbance == 23.45


@pytest.mark.short
def test_create_well_plate_with_two_measurements() -> None:
    plate_data = {
        "A452": 23.45,
        "A280": 23.45,
        "Sample name": "dummy name",
        "Plate Position": "some plate",
        "Date": "17/10/2016",
        "Time": "7:19:18",
    }
    well_plate = _create_measurement_group(
        SeriesData(pd.Series(plate_data)), ["A452", "A280"], [], None
    )

    assert len(well_plate.measurements) == 2


@pytest.mark.short
def test_create_well_plate_without_date_column_then_raise() -> None:
    plate_data = SeriesData(
        pd.Series(
            {
                "Sample name": "dummy name",
                "Plate Position": "some plate",
                "Time": "7:19:18",
            }
        )
    )
    with pytest.raises(AllotropeConversionError, match=NO_DATE_OR_TIME_ERROR_MSG):
        _create_measurement_group(plate_data, [], [], None)


@pytest.mark.short
def test_get_calculated_data_items_from_data_with_the_right_values() -> None:
    contents = StringIO(
        """
Sample name,Plate Position,Application,Date,Time,Instrument ID,A260,A260 Concentration (ng/ul)
batch_id,Plate1,dummyApp,2021-05-20,16:55:51,14,23.4,4.5
"""
    )
    reader = UnchainedLabsLunaticReader(NamedFileContents(contents, "filename.csv"))
    _, calculated_data = create_measurement_groups(reader.header, reader.data)
    assert calculated_data
    calculated_data_item = calculated_data[0]

    assert calculated_data_item.name == "Concentration"
    assert calculated_data_item.value == 4.5
    assert calculated_data_item.unit == "ng/µL"
    assert calculated_data_item.data_sources[0].feature == "absorbance"


@pytest.mark.short
def test_get_calculated_data_items_from_data_create_right_ammount_of_items() -> None:
    contents = StringIO(
        """
Sample name,Plate Position,Application,Date,Time,Instrument ID,A260,A260 Concentration (ng/ul),Background (A260),A260/A230,A260/A280
batch_id,Plate1,dummyApp,2021-05-20,16:55:51,14,23.4,4.5,0.523,2.5,24.9
"""
    )
    reader = UnchainedLabsLunaticReader(NamedFileContents(contents, "filename.csv"))
    _, calculated_data = create_measurement_groups(reader.header, reader.data)
    assert len(calculated_data) == 4


@pytest.mark.short
def test_get_calculated_data_items_from_data_with_no_calculated_data_columns() -> (
    None
):
    contents = StringIO(
        """
Sample name,Plate Position,Application,Date,Time,Instrument ID,A260
batch_id,Plate1,dummyApp,2021-05-20,16:55:51,14,23.4
"""
    )
    reader = UnchainedLabsLunaticReader(NamedFileContents(contents, "filename.csv"))
    _, calculated_data = create_measurement_groups(reader.header, reader.data)
    assert not calculated_data


@pytest.mark.short
def test_create_data() -> None:
    contents = StringIO(
        """
Sample name,Plate Position,Application,Date,Time,Instrument ID,A250
batch_id,Plate1,dummyApp,2021-05-20,16:55:51,14,23.4
batch_id,Plate1,dummyApp,2021-05-20,16:55:51,14,32.6
'',Plate1,dummyApp,2021-05-20,16:55:51,14,439
"""
    )
    reader = UnchainedLabsLunaticReader(NamedFileContents(contents, "filename.csv"))
    measurement_groups, _ = create_measurement_groups(reader.header, reader.data)
    metadata = create_metadata(reader.header, "filename.csv")

    assert metadata.device_identifier == "14"
    assert len(measurement_groups) == 3
