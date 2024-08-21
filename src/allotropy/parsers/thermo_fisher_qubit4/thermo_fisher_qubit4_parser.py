from allotropy.allotrope.models.adm.spectrophotometry.benchling._2023._12.spectrophotometry import (
    Model,
)
from allotropy.allotrope.schema_mappers.adm.spectrophotometry.benchling._2023._12.spectrophotometry import (
    Data,
    Mapper,
)
from allotropy.named_file_contents import NamedFileContents
from allotropy.parsers.release_state import ReleaseState
from allotropy.parsers.thermo_fisher_qubit4.thermo_fisher_qubit4_reader import (
    ThermoFisherQubit4Reader,
)
from allotropy.parsers.thermo_fisher_qubit4.thermo_fisher_qubit4_structure import (
    create_measurement_group,
    create_metadata,
)
from allotropy.parsers.utils.pandas import map_rows
from allotropy.parsers.vendor_parser import MapperVendorParser


class ThermoFisherQubit4Parser(MapperVendorParser[Data, Model]):
    DISPLAY_NAME = "Thermo Fisher Qubit 4"
    RELEASE_STATE = ReleaseState.RECOMMENDED
    SCHEMA_MAPPER = Mapper

    def create_data(self, named_file_contents: NamedFileContents) -> Data:
        return Data(
            create_metadata(named_file_contents.original_file_name),
            measurement_groups=map_rows(
                ThermoFisherQubit4Reader.read(named_file_contents),
                create_measurement_group,
            ),
        )
