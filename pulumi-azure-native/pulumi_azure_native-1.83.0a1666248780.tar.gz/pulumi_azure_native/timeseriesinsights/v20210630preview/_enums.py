# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AccessPolicyRole',
    'DataStringComparisonBehavior',
    'EnvironmentKind',
    'EventSourceKind',
    'IngressStartAtType',
    'LocalTimestampFormat',
    'PropertyType',
    'ReferenceDataKeyPropertyType',
    'SkuName',
    'StorageLimitExceededBehavior',
]


class AccessPolicyRole(str, Enum):
    """
    A role defining the data plane operations that a principal can perform on a Time Series Insights client.
    """
    READER = "Reader"
    CONTRIBUTOR = "Contributor"


class DataStringComparisonBehavior(str, Enum):
    """
    The reference data set key comparison behavior can be set using this property. By default, the value is 'Ordinal' - which means case sensitive key comparison will be performed while joining reference data with events or while adding new reference data. When 'OrdinalIgnoreCase' is set, case insensitive comparison will be used.
    """
    ORDINAL = "Ordinal"
    ORDINAL_IGNORE_CASE = "OrdinalIgnoreCase"


class EnvironmentKind(str, Enum):
    """
    The kind of the environment.
    """
    GEN1 = "Gen1"
    GEN2 = "Gen2"


class EventSourceKind(str, Enum):
    """
    The kind of the event source.
    """
    MICROSOFT_EVENT_HUB = "Microsoft.EventHub"
    MICROSOFT_IO_T_HUB = "Microsoft.IoTHub"


class IngressStartAtType(str, Enum):
    """
    The type of the ingressStartAt, It can be "EarliestAvailable", "EventSourceCreationTime", "CustomEnqueuedTime".
    """
    EARLIEST_AVAILABLE = "EarliestAvailable"
    EVENT_SOURCE_CREATION_TIME = "EventSourceCreationTime"
    CUSTOM_ENQUEUED_TIME = "CustomEnqueuedTime"


class LocalTimestampFormat(str, Enum):
    """
    An enum that represents the format of the local timestamp property that needs to be set.
    """
    EMBEDDED = "Embedded"


class PropertyType(str, Enum):
    """
    The type of the property.
    """
    STRING = "String"


class ReferenceDataKeyPropertyType(str, Enum):
    """
    The type of the key property.
    """
    STRING = "String"
    DOUBLE = "Double"
    BOOL = "Bool"
    DATE_TIME = "DateTime"


class SkuName(str, Enum):
    """
    The name of this SKU.
    """
    S1 = "S1"
    S2 = "S2"
    P1 = "P1"
    L1 = "L1"


class StorageLimitExceededBehavior(str, Enum):
    """
    The behavior the Time Series Insights service should take when the environment's capacity has been exceeded. If "PauseIngress" is specified, new events will not be read from the event source. If "PurgeOldData" is specified, new events will continue to be read and old events will be deleted from the environment. The default behavior is PurgeOldData.
    """
    PURGE_OLD_DATA = "PurgeOldData"
    PAUSE_INGRESS = "PauseIngress"
