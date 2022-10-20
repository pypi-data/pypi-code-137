# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = ['PolicyArgs', 'Policy']

@pulumi.input_type
class PolicyArgs:
    def __init__(__self__, *,
                 lab_name: pulumi.Input[str],
                 policy_set_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 evaluator_type: Optional[pulumi.Input[Union[str, 'PolicyEvaluatorType']]] = None,
                 fact_data: Optional[pulumi.Input[str]] = None,
                 fact_name: Optional[pulumi.Input[Union[str, 'PolicyFactName']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'PolicyStatus']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 threshold: Optional[pulumi.Input[str]] = None,
                 unique_identifier: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Policy resource.
        :param pulumi.Input[str] lab_name: The name of the lab.
        :param pulumi.Input[str] policy_set_name: The name of the policy set.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] description: The description of the policy.
        :param pulumi.Input[Union[str, 'PolicyEvaluatorType']] evaluator_type: The evaluator type of the policy (i.e. AllowedValuesPolicy, MaxValuePolicy).
        :param pulumi.Input[str] fact_data: The fact data of the policy.
        :param pulumi.Input[Union[str, 'PolicyFactName']] fact_name: The fact name of the policy (e.g. LabVmCount, LabVmSize, MaxVmsAllowedPerLab, etc.
        :param pulumi.Input[str] location: The location of the resource.
        :param pulumi.Input[str] name: The name of the policy.
        :param pulumi.Input[str] provisioning_state: The provisioning status of the resource.
        :param pulumi.Input[Union[str, 'PolicyStatus']] status: The status of the policy.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The tags of the resource.
        :param pulumi.Input[str] threshold: The threshold of the policy (i.e. a number for MaxValuePolicy, and a JSON array of values for AllowedValuesPolicy).
        :param pulumi.Input[str] unique_identifier: The unique immutable identifier of a resource (Guid).
        """
        pulumi.set(__self__, "lab_name", lab_name)
        pulumi.set(__self__, "policy_set_name", policy_set_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if evaluator_type is not None:
            pulumi.set(__self__, "evaluator_type", evaluator_type)
        if fact_data is not None:
            pulumi.set(__self__, "fact_data", fact_data)
        if fact_name is not None:
            pulumi.set(__self__, "fact_name", fact_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if provisioning_state is not None:
            pulumi.set(__self__, "provisioning_state", provisioning_state)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if threshold is not None:
            pulumi.set(__self__, "threshold", threshold)
        if unique_identifier is not None:
            pulumi.set(__self__, "unique_identifier", unique_identifier)

    @property
    @pulumi.getter(name="labName")
    def lab_name(self) -> pulumi.Input[str]:
        """
        The name of the lab.
        """
        return pulumi.get(self, "lab_name")

    @lab_name.setter
    def lab_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "lab_name", value)

    @property
    @pulumi.getter(name="policySetName")
    def policy_set_name(self) -> pulumi.Input[str]:
        """
        The name of the policy set.
        """
        return pulumi.get(self, "policy_set_name")

    @policy_set_name.setter
    def policy_set_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "policy_set_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the policy.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="evaluatorType")
    def evaluator_type(self) -> Optional[pulumi.Input[Union[str, 'PolicyEvaluatorType']]]:
        """
        The evaluator type of the policy (i.e. AllowedValuesPolicy, MaxValuePolicy).
        """
        return pulumi.get(self, "evaluator_type")

    @evaluator_type.setter
    def evaluator_type(self, value: Optional[pulumi.Input[Union[str, 'PolicyEvaluatorType']]]):
        pulumi.set(self, "evaluator_type", value)

    @property
    @pulumi.getter(name="factData")
    def fact_data(self) -> Optional[pulumi.Input[str]]:
        """
        The fact data of the policy.
        """
        return pulumi.get(self, "fact_data")

    @fact_data.setter
    def fact_data(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "fact_data", value)

    @property
    @pulumi.getter(name="factName")
    def fact_name(self) -> Optional[pulumi.Input[Union[str, 'PolicyFactName']]]:
        """
        The fact name of the policy (e.g. LabVmCount, LabVmSize, MaxVmsAllowedPerLab, etc.
        """
        return pulumi.get(self, "fact_name")

    @fact_name.setter
    def fact_name(self, value: Optional[pulumi.Input[Union[str, 'PolicyFactName']]]):
        pulumi.set(self, "fact_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location of the resource.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the policy.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[str]]:
        """
        The provisioning status of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provisioning_state", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[str, 'PolicyStatus']]]:
        """
        The status of the policy.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[str, 'PolicyStatus']]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The tags of the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def threshold(self) -> Optional[pulumi.Input[str]]:
        """
        The threshold of the policy (i.e. a number for MaxValuePolicy, and a JSON array of values for AllowedValuesPolicy).
        """
        return pulumi.get(self, "threshold")

    @threshold.setter
    def threshold(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "threshold", value)

    @property
    @pulumi.getter(name="uniqueIdentifier")
    def unique_identifier(self) -> Optional[pulumi.Input[str]]:
        """
        The unique immutable identifier of a resource (Guid).
        """
        return pulumi.get(self, "unique_identifier")

    @unique_identifier.setter
    def unique_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "unique_identifier", value)


warnings.warn("""Version 2016-05-15 will be removed in v2 of the provider.""", DeprecationWarning)


class Policy(pulumi.CustomResource):
    warnings.warn("""Version 2016-05-15 will be removed in v2 of the provider.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 evaluator_type: Optional[pulumi.Input[Union[str, 'PolicyEvaluatorType']]] = None,
                 fact_data: Optional[pulumi.Input[str]] = None,
                 fact_name: Optional[pulumi.Input[Union[str, 'PolicyFactName']]] = None,
                 lab_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 policy_set_name: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'PolicyStatus']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 threshold: Optional[pulumi.Input[str]] = None,
                 unique_identifier: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A Policy.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the policy.
        :param pulumi.Input[Union[str, 'PolicyEvaluatorType']] evaluator_type: The evaluator type of the policy (i.e. AllowedValuesPolicy, MaxValuePolicy).
        :param pulumi.Input[str] fact_data: The fact data of the policy.
        :param pulumi.Input[Union[str, 'PolicyFactName']] fact_name: The fact name of the policy (e.g. LabVmCount, LabVmSize, MaxVmsAllowedPerLab, etc.
        :param pulumi.Input[str] lab_name: The name of the lab.
        :param pulumi.Input[str] location: The location of the resource.
        :param pulumi.Input[str] name: The name of the policy.
        :param pulumi.Input[str] policy_set_name: The name of the policy set.
        :param pulumi.Input[str] provisioning_state: The provisioning status of the resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Union[str, 'PolicyStatus']] status: The status of the policy.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The tags of the resource.
        :param pulumi.Input[str] threshold: The threshold of the policy (i.e. a number for MaxValuePolicy, and a JSON array of values for AllowedValuesPolicy).
        :param pulumi.Input[str] unique_identifier: The unique immutable identifier of a resource (Guid).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A Policy.

        :param str resource_name: The name of the resource.
        :param PolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 evaluator_type: Optional[pulumi.Input[Union[str, 'PolicyEvaluatorType']]] = None,
                 fact_data: Optional[pulumi.Input[str]] = None,
                 fact_name: Optional[pulumi.Input[Union[str, 'PolicyFactName']]] = None,
                 lab_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 policy_set_name: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'PolicyStatus']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 threshold: Optional[pulumi.Input[str]] = None,
                 unique_identifier: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""Policy is deprecated: Version 2016-05-15 will be removed in v2 of the provider.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PolicyArgs.__new__(PolicyArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["evaluator_type"] = evaluator_type
            __props__.__dict__["fact_data"] = fact_data
            __props__.__dict__["fact_name"] = fact_name
            if lab_name is None and not opts.urn:
                raise TypeError("Missing required property 'lab_name'")
            __props__.__dict__["lab_name"] = lab_name
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            if policy_set_name is None and not opts.urn:
                raise TypeError("Missing required property 'policy_set_name'")
            __props__.__dict__["policy_set_name"] = policy_set_name
            __props__.__dict__["provisioning_state"] = provisioning_state
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["status"] = status
            __props__.__dict__["tags"] = tags
            __props__.__dict__["threshold"] = threshold
            __props__.__dict__["unique_identifier"] = unique_identifier
            __props__.__dict__["created_date"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:devtestlab:Policy"), pulumi.Alias(type_="azure-native:devtestlab/v20150521preview:Policy"), pulumi.Alias(type_="azure-native:devtestlab/v20180915:Policy")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Policy, __self__).__init__(
            'azure-native:devtestlab/v20160515:Policy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Policy':
        """
        Get an existing Policy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PolicyArgs.__new__(PolicyArgs)

        __props__.__dict__["created_date"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["evaluator_type"] = None
        __props__.__dict__["fact_data"] = None
        __props__.__dict__["fact_name"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["threshold"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["unique_identifier"] = None
        return Policy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> pulumi.Output[str]:
        """
        The creation date of the policy.
        """
        return pulumi.get(self, "created_date")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the policy.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="evaluatorType")
    def evaluator_type(self) -> pulumi.Output[Optional[str]]:
        """
        The evaluator type of the policy (i.e. AllowedValuesPolicy, MaxValuePolicy).
        """
        return pulumi.get(self, "evaluator_type")

    @property
    @pulumi.getter(name="factData")
    def fact_data(self) -> pulumi.Output[Optional[str]]:
        """
        The fact data of the policy.
        """
        return pulumi.get(self, "fact_data")

    @property
    @pulumi.getter(name="factName")
    def fact_name(self) -> pulumi.Output[Optional[str]]:
        """
        The fact name of the policy (e.g. LabVmCount, LabVmSize, MaxVmsAllowedPerLab, etc.
        """
        return pulumi.get(self, "fact_name")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[str]]:
        """
        The provisioning status of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[str]]:
        """
        The status of the policy.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The tags of the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def threshold(self) -> pulumi.Output[Optional[str]]:
        """
        The threshold of the policy (i.e. a number for MaxValuePolicy, and a JSON array of values for AllowedValuesPolicy).
        """
        return pulumi.get(self, "threshold")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="uniqueIdentifier")
    def unique_identifier(self) -> pulumi.Output[Optional[str]]:
        """
        The unique immutable identifier of a resource (Guid).
        """
        return pulumi.get(self, "unique_identifier")

