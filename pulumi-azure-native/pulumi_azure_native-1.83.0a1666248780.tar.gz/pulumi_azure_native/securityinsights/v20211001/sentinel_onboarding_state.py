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

__all__ = ['SentinelOnboardingStateArgs', 'SentinelOnboardingState']

@pulumi.input_type
class SentinelOnboardingStateArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 customer_managed_key: Optional[pulumi.Input[bool]] = None,
                 sentinel_onboarding_state_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SentinelOnboardingState resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        :param pulumi.Input[bool] customer_managed_key: Flag that indicates the status of the CMK setting
        :param pulumi.Input[str] sentinel_onboarding_state_name: The Sentinel onboarding state name. Supports - default
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if customer_managed_key is not None:
            pulumi.set(__self__, "customer_managed_key", customer_managed_key)
        if sentinel_onboarding_state_name is not None:
            pulumi.set(__self__, "sentinel_onboarding_state_name", sentinel_onboarding_state_name)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[str]:
        """
        The name of the workspace.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter(name="customerManagedKey")
    def customer_managed_key(self) -> Optional[pulumi.Input[bool]]:
        """
        Flag that indicates the status of the CMK setting
        """
        return pulumi.get(self, "customer_managed_key")

    @customer_managed_key.setter
    def customer_managed_key(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "customer_managed_key", value)

    @property
    @pulumi.getter(name="sentinelOnboardingStateName")
    def sentinel_onboarding_state_name(self) -> Optional[pulumi.Input[str]]:
        """
        The Sentinel onboarding state name. Supports - default
        """
        return pulumi.get(self, "sentinel_onboarding_state_name")

    @sentinel_onboarding_state_name.setter
    def sentinel_onboarding_state_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sentinel_onboarding_state_name", value)


class SentinelOnboardingState(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 customer_managed_key: Optional[pulumi.Input[bool]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sentinel_onboarding_state_name: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Sentinel onboarding state

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] customer_managed_key: Flag that indicates the status of the CMK setting
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] sentinel_onboarding_state_name: The Sentinel onboarding state name. Supports - default
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SentinelOnboardingStateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Sentinel onboarding state

        :param str resource_name: The name of the resource.
        :param SentinelOnboardingStateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SentinelOnboardingStateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 customer_managed_key: Optional[pulumi.Input[bool]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sentinel_onboarding_state_name: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SentinelOnboardingStateArgs.__new__(SentinelOnboardingStateArgs)

            __props__.__dict__["customer_managed_key"] = customer_managed_key
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["sentinel_onboarding_state_name"] = sentinel_onboarding_state_name
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:securityinsights:SentinelOnboardingState"), pulumi.Alias(type_="azure-native:securityinsights/v20210301preview:SentinelOnboardingState"), pulumi.Alias(type_="azure-native:securityinsights/v20210901preview:SentinelOnboardingState"), pulumi.Alias(type_="azure-native:securityinsights/v20211001preview:SentinelOnboardingState"), pulumi.Alias(type_="azure-native:securityinsights/v20220101preview:SentinelOnboardingState"), pulumi.Alias(type_="azure-native:securityinsights/v20220401preview:SentinelOnboardingState"), pulumi.Alias(type_="azure-native:securityinsights/v20220501preview:SentinelOnboardingState"), pulumi.Alias(type_="azure-native:securityinsights/v20220601preview:SentinelOnboardingState"), pulumi.Alias(type_="azure-native:securityinsights/v20220701preview:SentinelOnboardingState"), pulumi.Alias(type_="azure-native:securityinsights/v20220801:SentinelOnboardingState"), pulumi.Alias(type_="azure-native:securityinsights/v20220801preview:SentinelOnboardingState"), pulumi.Alias(type_="azure-native:securityinsights/v20220901preview:SentinelOnboardingState"), pulumi.Alias(type_="azure-native:securityinsights/v20221001preview:SentinelOnboardingState")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SentinelOnboardingState, __self__).__init__(
            'azure-native:securityinsights/v20211001:SentinelOnboardingState',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SentinelOnboardingState':
        """
        Get an existing SentinelOnboardingState resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SentinelOnboardingStateArgs.__new__(SentinelOnboardingStateArgs)

        __props__.__dict__["customer_managed_key"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return SentinelOnboardingState(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="customerManagedKey")
    def customer_managed_key(self) -> pulumi.Output[Optional[bool]]:
        """
        Flag that indicates the status of the CMK setting
        """
        return pulumi.get(self, "customer_managed_key")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        Etag of the azure resource
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

