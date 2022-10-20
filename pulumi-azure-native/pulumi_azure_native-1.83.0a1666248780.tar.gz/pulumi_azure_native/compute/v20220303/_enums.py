# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'Architecture',
    'ConfidentialVMEncryptionType',
    'GalleryApplicationCustomActionParameterType',
    'GalleryExtendedLocationType',
    'GallerySharingPermissionTypes',
    'HostCaching',
    'HyperVGeneration',
    'OperatingSystemStateTypes',
    'OperatingSystemTypes',
    'ReplicationMode',
    'StorageAccountType',
]


class Architecture(str, Enum):
    """
    The architecture of the image. Applicable to OS disks only.
    """
    X64 = "x64"
    ARM64 = "Arm64"


class ConfidentialVMEncryptionType(str, Enum):
    """
    confidential VM encryption types
    """
    ENCRYPTED_VM_GUEST_STATE_ONLY_WITH_PMK = "EncryptedVMGuestStateOnlyWithPmk"
    ENCRYPTED_WITH_PMK = "EncryptedWithPmk"
    ENCRYPTED_WITH_CMK = "EncryptedWithCmk"


class GalleryApplicationCustomActionParameterType(str, Enum):
    """
    Specifies the type of the custom action parameter. Possible values are: String, ConfigurationDataBlob or LogOutputBlob
    """
    STRING = "String"
    CONFIGURATION_DATA_BLOB = "ConfigurationDataBlob"
    LOG_OUTPUT_BLOB = "LogOutputBlob"


class GalleryExtendedLocationType(str, Enum):
    """
    It is type of the extended location.
    """
    EDGE_ZONE = "EdgeZone"
    UNKNOWN = "Unknown"


class GallerySharingPermissionTypes(str, Enum):
    """
    This property allows you to specify the permission of sharing gallery. <br><br> Possible values are: <br><br> **Private** <br><br> **Groups** <br><br> **Community**
    """
    PRIVATE = "Private"
    GROUPS = "Groups"
    COMMUNITY = "Community"


class HostCaching(str, Enum):
    """
    The host caching of the disk. Valid values are 'None', 'ReadOnly', and 'ReadWrite'
    """
    NONE = "None"
    READ_ONLY = "ReadOnly"
    READ_WRITE = "ReadWrite"


class HyperVGeneration(str, Enum):
    """
    The hypervisor generation of the Virtual Machine. Applicable to OS disks only.
    """
    V1 = "V1"
    V2 = "V2"


class OperatingSystemStateTypes(str, Enum):
    """
    This property allows the user to specify whether the virtual machines created under this image are 'Generalized' or 'Specialized'.
    """
    GENERALIZED = "Generalized"
    SPECIALIZED = "Specialized"


class OperatingSystemTypes(str, Enum):
    """
    This property allows you to specify the type of the OS that is included in the disk when creating a VM from a managed image. <br><br> Possible values are: <br><br> **Windows** <br><br> **Linux**
    """
    WINDOWS = "Windows"
    LINUX = "Linux"


class ReplicationMode(str, Enum):
    """
    Optional parameter which specifies the mode to be used for replication. This property is not updatable.
    """
    FULL = "Full"
    SHALLOW = "Shallow"


class StorageAccountType(str, Enum):
    """
    Specifies the storage account type to be used to store the image. This property is not updatable.
    """
    STANDARD_LRS = "Standard_LRS"
    STANDARD_ZRS = "Standard_ZRS"
    PREMIUM_LRS = "Premium_LRS"
