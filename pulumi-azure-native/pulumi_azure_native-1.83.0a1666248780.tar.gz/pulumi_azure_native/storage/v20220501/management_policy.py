# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['ManagementPolicyArgs', 'ManagementPolicy']

@pulumi.input_type
class ManagementPolicyArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 policy: pulumi.Input['ManagementPolicySchemaArgs'],
                 resource_group_name: pulumi.Input[str],
                 management_policy_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ManagementPolicy resource.
        :param pulumi.Input[str] account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
        :param pulumi.Input['ManagementPolicySchemaArgs'] policy: The Storage Account ManagementPolicy, in JSON format. See more details in: https://docs.microsoft.com/en-us/azure/storage/common/storage-lifecycle-managment-concepts.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
        :param pulumi.Input[str] management_policy_name: The name of the Storage Account Management Policy. It should always be 'default'
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "policy", policy)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if management_policy_name is not None:
            pulumi.set(__self__, "management_policy_name", management_policy_name)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter
    def policy(self) -> pulumi.Input['ManagementPolicySchemaArgs']:
        """
        The Storage Account ManagementPolicy, in JSON format. See more details in: https://docs.microsoft.com/en-us/azure/storage/common/storage-lifecycle-managment-concepts.
        """
        return pulumi.get(self, "policy")

    @policy.setter
    def policy(self, value: pulumi.Input['ManagementPolicySchemaArgs']):
        pulumi.set(self, "policy", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group within the user's subscription. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="managementPolicyName")
    def management_policy_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Storage Account Management Policy. It should always be 'default'
        """
        return pulumi.get(self, "management_policy_name")

    @management_policy_name.setter
    def management_policy_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "management_policy_name", value)


class ManagementPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 management_policy_name: Optional[pulumi.Input[str]] = None,
                 policy: Optional[pulumi.Input[pulumi.InputType['ManagementPolicySchemaArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The Get Storage Account ManagementPolicies operation response.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
        :param pulumi.Input[str] management_policy_name: The name of the Storage Account Management Policy. It should always be 'default'
        :param pulumi.Input[pulumi.InputType['ManagementPolicySchemaArgs']] policy: The Storage Account ManagementPolicy, in JSON format. See more details in: https://docs.microsoft.com/en-us/azure/storage/common/storage-lifecycle-managment-concepts.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ManagementPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The Get Storage Account ManagementPolicies operation response.

        :param str resource_name: The name of the resource.
        :param ManagementPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ManagementPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 management_policy_name: Optional[pulumi.Input[str]] = None,
                 policy: Optional[pulumi.Input[pulumi.InputType['ManagementPolicySchemaArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ManagementPolicyArgs.__new__(ManagementPolicyArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["management_policy_name"] = management_policy_name
            if policy is None and not opts.urn:
                raise TypeError("Missing required property 'policy'")
            __props__.__dict__["policy"] = policy
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["last_modified_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:storage:ManagementPolicy"), pulumi.Alias(type_="azure-native:storage/v20180301preview:ManagementPolicy"), pulumi.Alias(type_="azure-native:storage/v20181101:ManagementPolicy"), pulumi.Alias(type_="azure-native:storage/v20190401:ManagementPolicy"), pulumi.Alias(type_="azure-native:storage/v20190601:ManagementPolicy"), pulumi.Alias(type_="azure-native:storage/v20200801preview:ManagementPolicy"), pulumi.Alias(type_="azure-native:storage/v20210101:ManagementPolicy"), pulumi.Alias(type_="azure-native:storage/v20210201:ManagementPolicy"), pulumi.Alias(type_="azure-native:storage/v20210401:ManagementPolicy"), pulumi.Alias(type_="azure-native:storage/v20210601:ManagementPolicy"), pulumi.Alias(type_="azure-native:storage/v20210801:ManagementPolicy"), pulumi.Alias(type_="azure-native:storage/v20210901:ManagementPolicy")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ManagementPolicy, __self__).__init__(
            'azure-native:storage/v20220501:ManagementPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ManagementPolicy':
        """
        Get an existing ManagementPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ManagementPolicyArgs.__new__(ManagementPolicyArgs)

        __props__.__dict__["last_modified_time"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["policy"] = None
        __props__.__dict__["type"] = None
        return ManagementPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[str]:
        """
        Returns the date and time the ManagementPolicies was last modified.
        """
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def policy(self) -> pulumi.Output['outputs.ManagementPolicySchemaResponse']:
        """
        The Storage Account ManagementPolicy, in JSON format. See more details in: https://docs.microsoft.com/en-us/azure/storage/common/storage-lifecycle-managment-concepts.
        """
        return pulumi.get(self, "policy")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

