# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ComputeType',
    'EncryptionStatus',
    'PrivateEndpointServiceConnectionStatus',
    'RemoteLoginPortPublicAccess',
    'ResourceIdentityType',
    'VmPriority',
]


class ComputeType(str, Enum):
    """
    The type of compute
    """
    AKS = "AKS"
    AML_COMPUTE = "AmlCompute"
    DATA_FACTORY = "DataFactory"
    VIRTUAL_MACHINE = "VirtualMachine"
    HD_INSIGHT = "HDInsight"
    DATABRICKS = "Databricks"
    DATA_LAKE_ANALYTICS = "DataLakeAnalytics"


class EncryptionStatus(str, Enum):
    """
    Indicates whether or not the encryption is enabled for the workspace.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class PrivateEndpointServiceConnectionStatus(str, Enum):
    """
    Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
    """
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"


class RemoteLoginPortPublicAccess(str, Enum):
    """
    State of the public SSH port. Possible values are: Disabled - Indicates that the public ssh port is closed on all nodes of the cluster. Enabled - Indicates that the public ssh port is open on all nodes of the cluster. NotSpecified - Indicates that the public ssh port is closed on all nodes of the cluster if VNet is defined, else is open all public nodes. It can be default only during cluster creation time, after creation it will be either enabled or disabled.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"
    NOT_SPECIFIED = "NotSpecified"


class ResourceIdentityType(str, Enum):
    """
    The identity type.
    """
    SYSTEM_ASSIGNED = "SystemAssigned"


class VmPriority(str, Enum):
    """
    Virtual Machine priority
    """
    DEDICATED = "Dedicated"
    LOW_PRIORITY = "LowPriority"
