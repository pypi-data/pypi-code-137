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

__all__ = ['ReportConfigArgs', 'ReportConfig']

@pulumi.input_type
class ReportConfigArgs:
    def __init__(__self__, *,
                 definition: pulumi.Input['ReportConfigDefinitionArgs'],
                 delivery_info: pulumi.Input['ReportConfigDeliveryInfoArgs'],
                 format: Optional[pulumi.Input[Union[str, 'FormatType']]] = None,
                 report_config_name: Optional[pulumi.Input[str]] = None,
                 schedule: Optional[pulumi.Input['ReportConfigScheduleArgs']] = None):
        """
        The set of arguments for constructing a ReportConfig resource.
        :param pulumi.Input['ReportConfigDefinitionArgs'] definition: Has definition for the report config.
        :param pulumi.Input['ReportConfigDeliveryInfoArgs'] delivery_info: Has delivery information for the report config.
        :param pulumi.Input[Union[str, 'FormatType']] format: The format of the report being delivered.
        :param pulumi.Input[str] report_config_name: Report Config Name.
        :param pulumi.Input['ReportConfigScheduleArgs'] schedule: Has schedule information for the report config.
        """
        pulumi.set(__self__, "definition", definition)
        pulumi.set(__self__, "delivery_info", delivery_info)
        if format is not None:
            pulumi.set(__self__, "format", format)
        if report_config_name is not None:
            pulumi.set(__self__, "report_config_name", report_config_name)
        if schedule is not None:
            pulumi.set(__self__, "schedule", schedule)

    @property
    @pulumi.getter
    def definition(self) -> pulumi.Input['ReportConfigDefinitionArgs']:
        """
        Has definition for the report config.
        """
        return pulumi.get(self, "definition")

    @definition.setter
    def definition(self, value: pulumi.Input['ReportConfigDefinitionArgs']):
        pulumi.set(self, "definition", value)

    @property
    @pulumi.getter(name="deliveryInfo")
    def delivery_info(self) -> pulumi.Input['ReportConfigDeliveryInfoArgs']:
        """
        Has delivery information for the report config.
        """
        return pulumi.get(self, "delivery_info")

    @delivery_info.setter
    def delivery_info(self, value: pulumi.Input['ReportConfigDeliveryInfoArgs']):
        pulumi.set(self, "delivery_info", value)

    @property
    @pulumi.getter
    def format(self) -> Optional[pulumi.Input[Union[str, 'FormatType']]]:
        """
        The format of the report being delivered.
        """
        return pulumi.get(self, "format")

    @format.setter
    def format(self, value: Optional[pulumi.Input[Union[str, 'FormatType']]]):
        pulumi.set(self, "format", value)

    @property
    @pulumi.getter(name="reportConfigName")
    def report_config_name(self) -> Optional[pulumi.Input[str]]:
        """
        Report Config Name.
        """
        return pulumi.get(self, "report_config_name")

    @report_config_name.setter
    def report_config_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "report_config_name", value)

    @property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input['ReportConfigScheduleArgs']]:
        """
        Has schedule information for the report config.
        """
        return pulumi.get(self, "schedule")

    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input['ReportConfigScheduleArgs']]):
        pulumi.set(self, "schedule", value)


warnings.warn("""Version 2018-05-31 will be removed in v2 of the provider.""", DeprecationWarning)


class ReportConfig(pulumi.CustomResource):
    warnings.warn("""Version 2018-05-31 will be removed in v2 of the provider.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 definition: Optional[pulumi.Input[pulumi.InputType['ReportConfigDefinitionArgs']]] = None,
                 delivery_info: Optional[pulumi.Input[pulumi.InputType['ReportConfigDeliveryInfoArgs']]] = None,
                 format: Optional[pulumi.Input[Union[str, 'FormatType']]] = None,
                 report_config_name: Optional[pulumi.Input[str]] = None,
                 schedule: Optional[pulumi.Input[pulumi.InputType['ReportConfigScheduleArgs']]] = None,
                 __props__=None):
        """
        A report config resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ReportConfigDefinitionArgs']] definition: Has definition for the report config.
        :param pulumi.Input[pulumi.InputType['ReportConfigDeliveryInfoArgs']] delivery_info: Has delivery information for the report config.
        :param pulumi.Input[Union[str, 'FormatType']] format: The format of the report being delivered.
        :param pulumi.Input[str] report_config_name: Report Config Name.
        :param pulumi.Input[pulumi.InputType['ReportConfigScheduleArgs']] schedule: Has schedule information for the report config.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ReportConfigArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A report config resource.

        :param str resource_name: The name of the resource.
        :param ReportConfigArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ReportConfigArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 definition: Optional[pulumi.Input[pulumi.InputType['ReportConfigDefinitionArgs']]] = None,
                 delivery_info: Optional[pulumi.Input[pulumi.InputType['ReportConfigDeliveryInfoArgs']]] = None,
                 format: Optional[pulumi.Input[Union[str, 'FormatType']]] = None,
                 report_config_name: Optional[pulumi.Input[str]] = None,
                 schedule: Optional[pulumi.Input[pulumi.InputType['ReportConfigScheduleArgs']]] = None,
                 __props__=None):
        pulumi.log.warn("""ReportConfig is deprecated: Version 2018-05-31 will be removed in v2 of the provider.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ReportConfigArgs.__new__(ReportConfigArgs)

            if definition is None and not opts.urn:
                raise TypeError("Missing required property 'definition'")
            __props__.__dict__["definition"] = definition
            if delivery_info is None and not opts.urn:
                raise TypeError("Missing required property 'delivery_info'")
            __props__.__dict__["delivery_info"] = delivery_info
            __props__.__dict__["format"] = format
            __props__.__dict__["report_config_name"] = report_config_name
            __props__.__dict__["schedule"] = schedule
            __props__.__dict__["name"] = None
            __props__.__dict__["tags"] = None
            __props__.__dict__["type"] = None
        super(ReportConfig, __self__).__init__(
            'azure-native:costmanagement/v20180531:ReportConfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ReportConfig':
        """
        Get an existing ReportConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ReportConfigArgs.__new__(ReportConfigArgs)

        __props__.__dict__["definition"] = None
        __props__.__dict__["delivery_info"] = None
        __props__.__dict__["format"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["schedule"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return ReportConfig(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def definition(self) -> pulumi.Output['outputs.ReportConfigDefinitionResponse']:
        """
        Has definition for the report config.
        """
        return pulumi.get(self, "definition")

    @property
    @pulumi.getter(name="deliveryInfo")
    def delivery_info(self) -> pulumi.Output['outputs.ReportConfigDeliveryInfoResponse']:
        """
        Has delivery information for the report config.
        """
        return pulumi.get(self, "delivery_info")

    @property
    @pulumi.getter
    def format(self) -> pulumi.Output[Optional[str]]:
        """
        The format of the report being delivered.
        """
        return pulumi.get(self, "format")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def schedule(self) -> pulumi.Output[Optional['outputs.ReportConfigScheduleResponse']]:
        """
        Has schedule information for the report config.
        """
        return pulumi.get(self, "schedule")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

