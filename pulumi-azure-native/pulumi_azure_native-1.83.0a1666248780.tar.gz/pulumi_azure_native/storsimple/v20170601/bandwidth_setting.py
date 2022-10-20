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

__all__ = ['BandwidthSettingArgs', 'BandwidthSetting']

@pulumi.input_type
class BandwidthSettingArgs:
    def __init__(__self__, *,
                 manager_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 schedules: pulumi.Input[Sequence[pulumi.Input['BandwidthScheduleArgs']]],
                 bandwidth_setting_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input['Kind']] = None):
        """
        The set of arguments for constructing a BandwidthSetting resource.
        :param pulumi.Input[str] manager_name: The manager name
        :param pulumi.Input[str] resource_group_name: The resource group name
        :param pulumi.Input[Sequence[pulumi.Input['BandwidthScheduleArgs']]] schedules: The schedules.
        :param pulumi.Input[str] bandwidth_setting_name: The bandwidth setting name.
        :param pulumi.Input['Kind'] kind: The Kind of the object. Currently only Series8000 is supported
        """
        pulumi.set(__self__, "manager_name", manager_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "schedules", schedules)
        if bandwidth_setting_name is not None:
            pulumi.set(__self__, "bandwidth_setting_name", bandwidth_setting_name)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)

    @property
    @pulumi.getter(name="managerName")
    def manager_name(self) -> pulumi.Input[str]:
        """
        The manager name
        """
        return pulumi.get(self, "manager_name")

    @manager_name.setter
    def manager_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "manager_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The resource group name
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def schedules(self) -> pulumi.Input[Sequence[pulumi.Input['BandwidthScheduleArgs']]]:
        """
        The schedules.
        """
        return pulumi.get(self, "schedules")

    @schedules.setter
    def schedules(self, value: pulumi.Input[Sequence[pulumi.Input['BandwidthScheduleArgs']]]):
        pulumi.set(self, "schedules", value)

    @property
    @pulumi.getter(name="bandwidthSettingName")
    def bandwidth_setting_name(self) -> Optional[pulumi.Input[str]]:
        """
        The bandwidth setting name.
        """
        return pulumi.get(self, "bandwidth_setting_name")

    @bandwidth_setting_name.setter
    def bandwidth_setting_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bandwidth_setting_name", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input['Kind']]:
        """
        The Kind of the object. Currently only Series8000 is supported
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input['Kind']]):
        pulumi.set(self, "kind", value)


class BandwidthSetting(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bandwidth_setting_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input['Kind']] = None,
                 manager_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 schedules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BandwidthScheduleArgs']]]]] = None,
                 __props__=None):
        """
        The bandwidth setting.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bandwidth_setting_name: The bandwidth setting name.
        :param pulumi.Input['Kind'] kind: The Kind of the object. Currently only Series8000 is supported
        :param pulumi.Input[str] manager_name: The manager name
        :param pulumi.Input[str] resource_group_name: The resource group name
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BandwidthScheduleArgs']]]] schedules: The schedules.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BandwidthSettingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The bandwidth setting.

        :param str resource_name: The name of the resource.
        :param BandwidthSettingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BandwidthSettingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bandwidth_setting_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input['Kind']] = None,
                 manager_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 schedules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BandwidthScheduleArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BandwidthSettingArgs.__new__(BandwidthSettingArgs)

            __props__.__dict__["bandwidth_setting_name"] = bandwidth_setting_name
            __props__.__dict__["kind"] = kind
            if manager_name is None and not opts.urn:
                raise TypeError("Missing required property 'manager_name'")
            __props__.__dict__["manager_name"] = manager_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if schedules is None and not opts.urn:
                raise TypeError("Missing required property 'schedules'")
            __props__.__dict__["schedules"] = schedules
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["volume_count"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:storsimple:BandwidthSetting")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(BandwidthSetting, __self__).__init__(
            'azure-native:storsimple/v20170601:BandwidthSetting',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'BandwidthSetting':
        """
        Get an existing BandwidthSetting resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = BandwidthSettingArgs.__new__(BandwidthSettingArgs)

        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["schedules"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["volume_count"] = None
        return BandwidthSetting(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        The Kind of the object. Currently only Series8000 is supported
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the object.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def schedules(self) -> pulumi.Output[Sequence['outputs.BandwidthScheduleResponse']]:
        """
        The schedules.
        """
        return pulumi.get(self, "schedules")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The hierarchical type of the object.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="volumeCount")
    def volume_count(self) -> pulumi.Output[int]:
        """
        The number of volumes that uses the bandwidth setting.
        """
        return pulumi.get(self, "volume_count")

