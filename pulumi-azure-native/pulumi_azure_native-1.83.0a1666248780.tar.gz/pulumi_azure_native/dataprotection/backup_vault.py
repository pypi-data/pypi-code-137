# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['BackupVaultInitArgs', 'BackupVault']

@pulumi.input_type
class BackupVaultInitArgs:
    def __init__(__self__, *,
                 properties: pulumi.Input['BackupVaultArgs'],
                 resource_group_name: pulumi.Input[str],
                 e_tag: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input['DppIdentityDetailsArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vault_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a BackupVault resource.
        :param pulumi.Input['BackupVaultArgs'] properties: BackupVaultResource properties
        :param pulumi.Input[str] resource_group_name: The name of the resource group where the backup vault is present.
        :param pulumi.Input[str] e_tag: Optional ETag.
        :param pulumi.Input['DppIdentityDetailsArgs'] identity: Input Managed Identity Details
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] vault_name: The name of the backup vault.
        """
        pulumi.set(__self__, "properties", properties)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if e_tag is not None:
            pulumi.set(__self__, "e_tag", e_tag)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if vault_name is not None:
            pulumi.set(__self__, "vault_name", vault_name)

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Input['BackupVaultArgs']:
        """
        BackupVaultResource properties
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: pulumi.Input['BackupVaultArgs']):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group where the backup vault is present.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[pulumi.Input[str]]:
        """
        Optional ETag.
        """
        return pulumi.get(self, "e_tag")

    @e_tag.setter
    def e_tag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "e_tag", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['DppIdentityDetailsArgs']]:
        """
        Input Managed Identity Details
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['DppIdentityDetailsArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="vaultName")
    def vault_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the backup vault.
        """
        return pulumi.get(self, "vault_name")

    @vault_name.setter
    def vault_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vault_name", value)


class BackupVault(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 e_tag: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['DppIdentityDetailsArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['BackupVaultArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vault_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Backup Vault Resource
        API Version: 2021-01-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] e_tag: Optional ETag.
        :param pulumi.Input[pulumi.InputType['DppIdentityDetailsArgs']] identity: Input Managed Identity Details
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[pulumi.InputType['BackupVaultArgs']] properties: BackupVaultResource properties
        :param pulumi.Input[str] resource_group_name: The name of the resource group where the backup vault is present.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] vault_name: The name of the backup vault.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BackupVaultInitArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Backup Vault Resource
        API Version: 2021-01-01.

        :param str resource_name: The name of the resource.
        :param BackupVaultInitArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BackupVaultInitArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 e_tag: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['DppIdentityDetailsArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['BackupVaultArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vault_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BackupVaultInitArgs.__new__(BackupVaultInitArgs)

            __props__.__dict__["e_tag"] = e_tag
            __props__.__dict__["identity"] = identity
            __props__.__dict__["location"] = location
            if properties is None and not opts.urn:
                raise TypeError("Missing required property 'properties'")
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["vault_name"] = vault_name
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:dataprotection/v20210101:BackupVault"), pulumi.Alias(type_="azure-native:dataprotection/v20210201preview:BackupVault"), pulumi.Alias(type_="azure-native:dataprotection/v20210601preview:BackupVault"), pulumi.Alias(type_="azure-native:dataprotection/v20210701:BackupVault"), pulumi.Alias(type_="azure-native:dataprotection/v20211001preview:BackupVault"), pulumi.Alias(type_="azure-native:dataprotection/v20211201preview:BackupVault"), pulumi.Alias(type_="azure-native:dataprotection/v20220101:BackupVault"), pulumi.Alias(type_="azure-native:dataprotection/v20220201preview:BackupVault"), pulumi.Alias(type_="azure-native:dataprotection/v20220301:BackupVault"), pulumi.Alias(type_="azure-native:dataprotection/v20220331preview:BackupVault"), pulumi.Alias(type_="azure-native:dataprotection/v20220401:BackupVault"), pulumi.Alias(type_="azure-native:dataprotection/v20220501:BackupVault"), pulumi.Alias(type_="azure-native:dataprotection/v20220901preview:BackupVault"), pulumi.Alias(type_="azure-native:dataprotection/v20221001preview:BackupVault")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(BackupVault, __self__).__init__(
            'azure-native:dataprotection:BackupVault',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'BackupVault':
        """
        Get an existing BackupVault resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = BackupVaultInitArgs.__new__(BackupVaultInitArgs)

        __props__.__dict__["e_tag"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return BackupVault(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> pulumi.Output[Optional[str]]:
        """
        Optional ETag.
        """
        return pulumi.get(self, "e_tag")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.DppIdentityDetailsResponse']]:
        """
        Input Managed Identity Details
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name associated with the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.BackupVaultResponse']:
        """
        BackupVaultResource properties
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/...
        """
        return pulumi.get(self, "type")

