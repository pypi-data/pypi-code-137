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
from ._inputs import *

__all__ = ['ObjectReplicationPolicyArgs', 'ObjectReplicationPolicy']

@pulumi.input_type
class ObjectReplicationPolicyArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 destination_account: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 source_account: pulumi.Input[str],
                 object_replication_policy_id: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input['ObjectReplicationPolicyRuleArgs']]]] = None):
        """
        The set of arguments for constructing a ObjectReplicationPolicy resource.
        :param pulumi.Input[str] account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
        :param pulumi.Input[str] destination_account: Required. Destination account name.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
        :param pulumi.Input[str] source_account: Required. Source account name.
        :param pulumi.Input[str] object_replication_policy_id: The ID of object replication policy or 'default' if the policy ID is unknown.
        :param pulumi.Input[Sequence[pulumi.Input['ObjectReplicationPolicyRuleArgs']]] rules: The storage account object replication rules.
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "destination_account", destination_account)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "source_account", source_account)
        if object_replication_policy_id is not None:
            pulumi.set(__self__, "object_replication_policy_id", object_replication_policy_id)
        if rules is not None:
            pulumi.set(__self__, "rules", rules)

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
    @pulumi.getter(name="destinationAccount")
    def destination_account(self) -> pulumi.Input[str]:
        """
        Required. Destination account name.
        """
        return pulumi.get(self, "destination_account")

    @destination_account.setter
    def destination_account(self, value: pulumi.Input[str]):
        pulumi.set(self, "destination_account", value)

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
    @pulumi.getter(name="sourceAccount")
    def source_account(self) -> pulumi.Input[str]:
        """
        Required. Source account name.
        """
        return pulumi.get(self, "source_account")

    @source_account.setter
    def source_account(self, value: pulumi.Input[str]):
        pulumi.set(self, "source_account", value)

    @property
    @pulumi.getter(name="objectReplicationPolicyId")
    def object_replication_policy_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of object replication policy or 'default' if the policy ID is unknown.
        """
        return pulumi.get(self, "object_replication_policy_id")

    @object_replication_policy_id.setter
    def object_replication_policy_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "object_replication_policy_id", value)

    @property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ObjectReplicationPolicyRuleArgs']]]]:
        """
        The storage account object replication rules.
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ObjectReplicationPolicyRuleArgs']]]]):
        pulumi.set(self, "rules", value)


class ObjectReplicationPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 destination_account: Optional[pulumi.Input[str]] = None,
                 object_replication_policy_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ObjectReplicationPolicyRuleArgs']]]]] = None,
                 source_account: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The replication policy between two storage accounts. Multiple rules can be defined in one policy.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
        :param pulumi.Input[str] destination_account: Required. Destination account name.
        :param pulumi.Input[str] object_replication_policy_id: The ID of object replication policy or 'default' if the policy ID is unknown.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ObjectReplicationPolicyRuleArgs']]]] rules: The storage account object replication rules.
        :param pulumi.Input[str] source_account: Required. Source account name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ObjectReplicationPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The replication policy between two storage accounts. Multiple rules can be defined in one policy.

        :param str resource_name: The name of the resource.
        :param ObjectReplicationPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ObjectReplicationPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 destination_account: Optional[pulumi.Input[str]] = None,
                 object_replication_policy_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ObjectReplicationPolicyRuleArgs']]]]] = None,
                 source_account: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ObjectReplicationPolicyArgs.__new__(ObjectReplicationPolicyArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            if destination_account is None and not opts.urn:
                raise TypeError("Missing required property 'destination_account'")
            __props__.__dict__["destination_account"] = destination_account
            __props__.__dict__["object_replication_policy_id"] = object_replication_policy_id
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["rules"] = rules
            if source_account is None and not opts.urn:
                raise TypeError("Missing required property 'source_account'")
            __props__.__dict__["source_account"] = source_account
            __props__.__dict__["enabled_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["policy_id"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:storage:ObjectReplicationPolicy"), pulumi.Alias(type_="azure-native:storage/v20190601:ObjectReplicationPolicy"), pulumi.Alias(type_="azure-native:storage/v20200801preview:ObjectReplicationPolicy"), pulumi.Alias(type_="azure-native:storage/v20210101:ObjectReplicationPolicy"), pulumi.Alias(type_="azure-native:storage/v20210401:ObjectReplicationPolicy"), pulumi.Alias(type_="azure-native:storage/v20210601:ObjectReplicationPolicy"), pulumi.Alias(type_="azure-native:storage/v20210801:ObjectReplicationPolicy"), pulumi.Alias(type_="azure-native:storage/v20210901:ObjectReplicationPolicy"), pulumi.Alias(type_="azure-native:storage/v20220501:ObjectReplicationPolicy")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ObjectReplicationPolicy, __self__).__init__(
            'azure-native:storage/v20210201:ObjectReplicationPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ObjectReplicationPolicy':
        """
        Get an existing ObjectReplicationPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ObjectReplicationPolicyArgs.__new__(ObjectReplicationPolicyArgs)

        __props__.__dict__["destination_account"] = None
        __props__.__dict__["enabled_time"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["policy_id"] = None
        __props__.__dict__["rules"] = None
        __props__.__dict__["source_account"] = None
        __props__.__dict__["type"] = None
        return ObjectReplicationPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="destinationAccount")
    def destination_account(self) -> pulumi.Output[str]:
        """
        Required. Destination account name.
        """
        return pulumi.get(self, "destination_account")

    @property
    @pulumi.getter(name="enabledTime")
    def enabled_time(self) -> pulumi.Output[str]:
        """
        Indicates when the policy is enabled on the source account.
        """
        return pulumi.get(self, "enabled_time")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> pulumi.Output[str]:
        """
        A unique id for object replication policy.
        """
        return pulumi.get(self, "policy_id")

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Optional[Sequence['outputs.ObjectReplicationPolicyRuleResponse']]]:
        """
        The storage account object replication rules.
        """
        return pulumi.get(self, "rules")

    @property
    @pulumi.getter(name="sourceAccount")
    def source_account(self) -> pulumi.Output[str]:
        """
        Required. Source account name.
        """
        return pulumi.get(self, "source_account")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

