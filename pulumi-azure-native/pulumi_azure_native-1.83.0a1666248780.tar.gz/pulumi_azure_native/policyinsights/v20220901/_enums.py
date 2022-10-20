# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ComplianceState',
]


class ComplianceState(str, Enum):
    """
    The compliance state that should be set on the resource.
    """
    COMPLIANT = "Compliant"
    """
    The resource is in compliance with the policy.
    """
    NON_COMPLIANT = "NonCompliant"
    """
    The resource is not in compliance with the policy.
    """
    UNKNOWN = "Unknown"
    """
    The compliance state of the resource is not known.
    """
