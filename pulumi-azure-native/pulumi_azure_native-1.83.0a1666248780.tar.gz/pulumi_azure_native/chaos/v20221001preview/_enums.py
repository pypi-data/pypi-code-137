# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'FilterType',
    'ResourceIdentityType',
    'SelectorType',
    'TargetReferenceType',
]


class FilterType(str, Enum):
    """
    Enum that discriminates between filter types. Currently only `Simple` type is supported.
    """
    SIMPLE = "Simple"


class ResourceIdentityType(str, Enum):
    """
    String of the resource identity type.
    """
    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"


class SelectorType(str, Enum):
    """
    Enum of the selector type.
    """
    PERCENT = "Percent"
    RANDOM = "Random"
    TAG = "Tag"
    LIST = "List"


class TargetReferenceType(str, Enum):
    """
    Enum of the Target reference type.
    """
    CHAOS_TARGET = "ChaosTarget"
