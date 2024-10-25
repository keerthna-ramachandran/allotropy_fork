# generated by datamodel-codegen:
#   filename:  binding-affinity-analyzer.schema.json
#   timestamp: 2024-10-25T13:11:35+00:00

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from allotropy.allotrope.models.shared.definitions.custom import (
    TQuantityValueDegreeCelsius,
    TQuantityValueMicroliter,
    TQuantityValueMicroliterPerMinute,
    TQuantityValueMolar,
    TQuantityValueNanomolar,
    TQuantityValuePercent,
    TQuantityValuePerSecond,
    TQuantityValueSecondTime,
    TQuantityValueTODO,
)
from allotropy.allotrope.models.shared.definitions.definitions import (
    TBooleanValue,
    TClass,
    TDateTimeStampValue,
    TDateTimeValue,
    TDoubleValue,
    TIntegerValue,
    TStatisticDatumRole,
    TStringValue,
    TUnit,
)


@dataclass(kw_only=True)
class CustomInformationDocumentItem:
    scalar_double_datum: TDoubleValue | None = None
    unit: TUnit | None = None
    scalar_string_datum: TStringValue | None = None
    scalar_timestamp_datum: TDateTimeValue | None = None
    scalar_boolean_datum: TBooleanValue | None = None
    datum_label: TStringValue | None = None


@dataclass(kw_only=True)
class ElectronicProjectRecord:
    written_name: TStringValue
    description: Any | None = None
    start_time: TDateTimeValue | None = None


@dataclass(kw_only=True)
class ErrorDocumentItem:
    error: TStringValue
    error_feature: TStringValue | None = None


@dataclass(kw_only=True)
class ErrorAggregateDocument:
    error_document: list[ErrorDocumentItem] | None = None


@dataclass(kw_only=True)
class ImageDocumentItem:
    experimental_data_identifier: TStringValue | None = None
    index: TIntegerValue | None = None


@dataclass(kw_only=True)
class ImageAggregateDocument:
    image_document: list[ImageDocumentItem] | None = None


@dataclass(kw_only=True)
class StatisticsDocumentItem:
    statistical_feature: TClass


@dataclass(kw_only=True)
class StatisticsAggregateDocument:
    statistics_document: list[StatisticsDocumentItem] | None = None


@dataclass(kw_only=True)
class TQuantityValueModel:
    value: float
    unit: TUnit
    has_statistic_datum_role: TStatisticDatumRole | None = None
    field_type: TClass | None = None


@dataclass(kw_only=True)
class AnalysisSequenceDocument:
    written_name: TStringValue
    end_time: TDateTimeValue | None = None
    file_name: TStringValue | None = None
    identifier: TStringValue | None = None
    method_identifier: TStringValue | None = None
    method_name: TStringValue | None = None
    start_time: TDateTimeValue | None = None
    UNC_path: TStringValue | None = None
    version_number: TStringValue | None = None


@dataclass(kw_only=True)
class SensorChipDocument:
    sensor_chip_identifier: TStringValue
    sensor_chip_type: TStringValue | None = None
    product_manufacturer: TStringValue | None = None


@dataclass(kw_only=True)
class CustomInformationAggregateDocument:
    custom_information_document: list[CustomInformationDocumentItem]


@dataclass(kw_only=True)
class DataSourceDocumentItem:
    data_source_identifier: TStringValue
    data_source_feature: TStringValue | None = None
    field_index: int | None = None


@dataclass(kw_only=True)
class DataSourceAggregateDocument:
    data_source_document: list[DataSourceDocumentItem]


@dataclass(kw_only=True)
class ElectronicSignatureDocumentItem:
    account_identifier: TStringValue
    personal_name: TStringValue
    signature_role_type: TStringValue
    time: TStringValue
    identifier: TStringValue | None = None
    measurement_identifier: TStringValue | None = None
    method_identifier: TStringValue | None = None
    processed_data_identifier: TStringValue | None = None
    field_index: int | None = None


@dataclass(kw_only=True)
class ElectronicSignatureAggregateDocument:
    electronic_signature_document: list[ElectronicSignatureDocumentItem] | None = None


@dataclass(kw_only=True)
class ProcessedDataAggregateDocument:
    processed_data_document: list[ProcessedDataDocumentItem]
    custom_information_aggregate_document: CustomInformationAggregateDocument | None = (
        None
    )
    electronic_project_record: ElectronicProjectRecord | None = None


@dataclass(kw_only=True)
class DataSystemDocument:
    ASM_file_identifier: TStringValue
    data_system_instance_identifier: TStringValue
    file_name: TStringValue | None = None
    UNC_path: TStringValue | None = None
    ASM_converter_name: TStringValue | None = None
    ASM_converter_version: TStringValue | None = None
    database_primary_key: TStringValue | None = None
    software_name: TStringValue | None = None
    software_version: TStringValue | None = None
    custom_information_aggregate_document: CustomInformationAggregateDocument | None = (
        None
    )


@dataclass(kw_only=True)
class DeviceDocumentItem:
    device_type: TStringValue
    brand_name: TStringValue | None = None
    device_identifier: TStringValue | None = None
    equipment_serial_number: TStringValue | None = None
    firmware_version: TStringValue | None = None
    model_number: TStringValue | None = None
    product_manufacturer: TStringValue | None = None
    written_name: TStringValue | None = None
    custom_information_aggregate_document: CustomInformationAggregateDocument | None = (
        None
    )
    field_index: int | None = None


@dataclass(kw_only=True)
class DeviceSystemDocument:
    device_identifier: TStringValue
    model_number: TStringValue
    asset_management_identifier: TStringValue | None = None
    brand_name: TStringValue | None = None
    description: Any | None = None
    device_document: list[DeviceDocumentItem] | None = None
    equipment_serial_number: TStringValue | None = None
    firmware_version: TStringValue | None = None
    product_manufacturer: TStringValue | None = None
    custom_information_aggregate_document: CustomInformationAggregateDocument | None = (
        None
    )


@dataclass(kw_only=True)
class DiagnosticTraceDocumentItem:
    description: Any
    custom_information_aggregate_document: CustomInformationAggregateDocument | None = (
        None
    )


@dataclass(kw_only=True)
class DiagnosticTraceAggregateDocument:
    diagnostic_trace_document: list[DiagnosticTraceDocumentItem] | None = None
    custom_information_aggregate_document: CustomInformationAggregateDocument | None = (
        None
    )


@dataclass(kw_only=True)
class DeviceControlDocumentItem:
    device_type: TStringValue
    brand_name: TStringValue | None = None
    detection_type: TStringValue | None = None
    device_identifier: TStringValue | None = None
    equipment_serial_number: TStringValue | None = None
    firmware_version: TStringValue | None = None
    model_number: TStringValue | None = None
    product_manufacturer: TStringValue | None = None
    custom_information_aggregate_document: CustomInformationAggregateDocument | None = (
        None
    )
    field_index: int | None = None
    sample_volume_setting: TQuantityValueMicroliter | None = None
    sample_temperature_setting: TQuantityValueDegreeCelsius | None = None
    flow_cell_identifier: TStringValue | None = None
    flow_rate: TQuantityValueMicroliterPerMinute | None = None
    contact_time: TQuantityValueSecondTime | None = None
    dilution_factor: TQuantityValuePercent | None = None
    flow_path: TStringValue | None = None


@dataclass(kw_only=True)
class DeviceControlAggregateDocument:
    device_control_document: list[DeviceControlDocumentItem]
    custom_information_aggregate_document: CustomInformationAggregateDocument | None = (
        None
    )


@dataclass(kw_only=True)
class ProcessedDataDocumentItem:
    custom_information_aggregate_document: CustomInformationAggregateDocument | None = (
        None
    )
    data_processing_document: dict[str, Any] | None = None
    data_source_aggregate_document: DataSourceAggregateDocument | None = None
    electronic_project_record: ElectronicProjectRecord | None = None
    processed_data_identifier: TStringValue | None = None
    field_index: int | None = None
    POSIX_path: TStringValue | None = None
    identifier: TStringValue | None = None
    binding_on_rate_measurement_datum__kon_: TQuantityValueTODO | None = None
    binding_off_rate_measurement_datum__koff_: TQuantityValuePerSecond | None = None
    equilibrium_dissociation_constant__KD_: TQuantityValueMolar | None = None
    maximum_binding_capacity__Rmax_: TQuantityValueTODO | None = None


@dataclass(kw_only=True)
class SampleDocument:
    sample_identifier: TStringValue
    batch_identifier: TStringValue | None = None
    description: Any | None = None
    sample_role_type: TClass | None = None
    written_name: TStringValue | None = None
    custom_information_aggregate_document: CustomInformationAggregateDocument | None = (
        None
    )
    location_identifier: TStringValue | None = None
    well_plate_identifier: TStringValue | None = None
    concentration: TQuantityValueNanomolar | None = None


@dataclass(kw_only=True)
class CalculatedDataDocumentItem:
    calculated_data_name: TStringValue
    calculated_result: TQuantityValueModel
    calculated_data_identifier: TStringValue | None = None
    calculation_description: TStringValue | None = None
    data_source_aggregate_document: DataSourceAggregateDocument | None = None
    electronic_project_record: ElectronicProjectRecord | None = None
    field_index: int | None = None


@dataclass(kw_only=True)
class CalculatedDataAggregateDocument:
    calculated_data_document: list[CalculatedDataDocumentItem]


@dataclass(kw_only=True)
class MeasurementDocument:
    device_control_aggregate_document: DeviceControlAggregateDocument
    measurement_identifier: TStringValue
    sample_document: SampleDocument
    POSIX_path: TStringValue
    calculated_data_aggregate_document: CalculatedDataAggregateDocument | None = None
    custom_information_aggregate_document: CustomInformationAggregateDocument | None = (
        None
    )
    detection_type: TStringValue | None = None
    electronic_project_record: ElectronicProjectRecord | None = None
    error_aggregate_document: ErrorAggregateDocument | None = None
    image_aggregate_document: ImageAggregateDocument | None = None
    measurement_time: TDateTimeStampValue | None = None
    processed_data_aggregate_document: ProcessedDataAggregateDocument | None = None
    statistics_aggregate_document: StatisticsAggregateDocument | None = None
    identifier: TStringValue | None = None
    sensor_chip_document: SensorChipDocument | None = None
    method_name: TStringValue | None = None
    ligand_identifier: TStringValue | None = None


@dataclass(kw_only=True)
class MeasurementAggregateDocument:
    measurement_document: list[MeasurementDocument]
    measurement_time: TDateTimeStampValue
    calculated_data_aggregate_document: CalculatedDataAggregateDocument | None = None
    custom_information_aggregate_document: CustomInformationAggregateDocument | None = (
        None
    )
    diagnostic_trace_aggregate_document: DiagnosticTraceAggregateDocument | None = None
    error_aggregate_document: ErrorAggregateDocument | None = None
    image_aggregate_document: ImageAggregateDocument | None = None
    processed_data_aggregate_document: ProcessedDataAggregateDocument | None = None
    statistics_aggregate_document: StatisticsAggregateDocument | None = None
    experiment_type: TStringValue | None = None
    analytical_method_identifier: TStringValue | None = None
    compartment_temperature: TQuantityValueDegreeCelsius | None = None


@dataclass(kw_only=True)
class BindingAffinityAnalyzerDocumentItem:
    measurement_aggregate_document: MeasurementAggregateDocument
    analyst: TStringValue | None = None
    electronic_project_record: ElectronicProjectRecord | None = None
    submitter: TStringValue | None = None


@dataclass(kw_only=True)
class BindingAffinityAnalyzerAggregateDocument:
    binding_affinity_analyzer_document: list[BindingAffinityAnalyzerDocumentItem]
    analysis_sequence_document: AnalysisSequenceDocument | None = None
    calculated_data_aggregate_document: CalculatedDataAggregateDocument | None = None
    custom_information_aggregate_document: CustomInformationAggregateDocument | None = (
        None
    )
    data_system_document: DataSystemDocument | None = None
    device_system_document: DeviceSystemDocument | None = None
    electronic_project_record: ElectronicProjectRecord | None = None
    electronic_signature_aggregate_document: ElectronicSignatureAggregateDocument | None = (
        None
    )
    processed_data_aggregate_document: ProcessedDataAggregateDocument | None = None
    statistics_aggregate_document: StatisticsAggregateDocument | None = None


@dataclass(kw_only=True)
class Model:
    manifest: str = "http://purl.allotrope.org/manifests/binding-affinity-analyzer/WD/2024/12/binding-affinity-analyzer.manifest"
    binding_affinity_analyzer_aggregate_document: BindingAffinityAnalyzerAggregateDocument | None = (
        None
    )
