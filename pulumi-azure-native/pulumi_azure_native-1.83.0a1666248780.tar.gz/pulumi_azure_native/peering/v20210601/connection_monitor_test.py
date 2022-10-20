# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['ConnectionMonitorTestArgs', 'ConnectionMonitorTest']

@pulumi.input_type
class ConnectionMonitorTestArgs:
    def __init__(__self__, *,
                 peering_service_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 connection_monitor_test_name: Optional[pulumi.Input[str]] = None,
                 destination: Optional[pulumi.Input[str]] = None,
                 destination_port: Optional[pulumi.Input[int]] = None,
                 source_agent: Optional[pulumi.Input[str]] = None,
                 test_frequency_in_sec: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a ConnectionMonitorTest resource.
        :param pulumi.Input[str] peering_service_name: The name of the peering service.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] connection_monitor_test_name: The name of the connection monitor test
        :param pulumi.Input[str] destination: The Connection Monitor test destination
        :param pulumi.Input[int] destination_port: The Connection Monitor test destination port
        :param pulumi.Input[str] source_agent: The Connection Monitor test source agent
        :param pulumi.Input[int] test_frequency_in_sec: The Connection Monitor test frequency in seconds
        """
        pulumi.set(__self__, "peering_service_name", peering_service_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if connection_monitor_test_name is not None:
            pulumi.set(__self__, "connection_monitor_test_name", connection_monitor_test_name)
        if destination is not None:
            pulumi.set(__self__, "destination", destination)
        if destination_port is not None:
            pulumi.set(__self__, "destination_port", destination_port)
        if source_agent is not None:
            pulumi.set(__self__, "source_agent", source_agent)
        if test_frequency_in_sec is not None:
            pulumi.set(__self__, "test_frequency_in_sec", test_frequency_in_sec)

    @property
    @pulumi.getter(name="peeringServiceName")
    def peering_service_name(self) -> pulumi.Input[str]:
        """
        The name of the peering service.
        """
        return pulumi.get(self, "peering_service_name")

    @peering_service_name.setter
    def peering_service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "peering_service_name", value)

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
    @pulumi.getter(name="connectionMonitorTestName")
    def connection_monitor_test_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the connection monitor test
        """
        return pulumi.get(self, "connection_monitor_test_name")

    @connection_monitor_test_name.setter
    def connection_monitor_test_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connection_monitor_test_name", value)

    @property
    @pulumi.getter
    def destination(self) -> Optional[pulumi.Input[str]]:
        """
        The Connection Monitor test destination
        """
        return pulumi.get(self, "destination")

    @destination.setter
    def destination(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "destination", value)

    @property
    @pulumi.getter(name="destinationPort")
    def destination_port(self) -> Optional[pulumi.Input[int]]:
        """
        The Connection Monitor test destination port
        """
        return pulumi.get(self, "destination_port")

    @destination_port.setter
    def destination_port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "destination_port", value)

    @property
    @pulumi.getter(name="sourceAgent")
    def source_agent(self) -> Optional[pulumi.Input[str]]:
        """
        The Connection Monitor test source agent
        """
        return pulumi.get(self, "source_agent")

    @source_agent.setter
    def source_agent(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_agent", value)

    @property
    @pulumi.getter(name="testFrequencyInSec")
    def test_frequency_in_sec(self) -> Optional[pulumi.Input[int]]:
        """
        The Connection Monitor test frequency in seconds
        """
        return pulumi.get(self, "test_frequency_in_sec")

    @test_frequency_in_sec.setter
    def test_frequency_in_sec(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "test_frequency_in_sec", value)


class ConnectionMonitorTest(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connection_monitor_test_name: Optional[pulumi.Input[str]] = None,
                 destination: Optional[pulumi.Input[str]] = None,
                 destination_port: Optional[pulumi.Input[int]] = None,
                 peering_service_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source_agent: Optional[pulumi.Input[str]] = None,
                 test_frequency_in_sec: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        The Connection Monitor Test class.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] connection_monitor_test_name: The name of the connection monitor test
        :param pulumi.Input[str] destination: The Connection Monitor test destination
        :param pulumi.Input[int] destination_port: The Connection Monitor test destination port
        :param pulumi.Input[str] peering_service_name: The name of the peering service.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] source_agent: The Connection Monitor test source agent
        :param pulumi.Input[int] test_frequency_in_sec: The Connection Monitor test frequency in seconds
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConnectionMonitorTestArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The Connection Monitor Test class.

        :param str resource_name: The name of the resource.
        :param ConnectionMonitorTestArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConnectionMonitorTestArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connection_monitor_test_name: Optional[pulumi.Input[str]] = None,
                 destination: Optional[pulumi.Input[str]] = None,
                 destination_port: Optional[pulumi.Input[int]] = None,
                 peering_service_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source_agent: Optional[pulumi.Input[str]] = None,
                 test_frequency_in_sec: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConnectionMonitorTestArgs.__new__(ConnectionMonitorTestArgs)

            __props__.__dict__["connection_monitor_test_name"] = connection_monitor_test_name
            __props__.__dict__["destination"] = destination
            __props__.__dict__["destination_port"] = destination_port
            if peering_service_name is None and not opts.urn:
                raise TypeError("Missing required property 'peering_service_name'")
            __props__.__dict__["peering_service_name"] = peering_service_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["source_agent"] = source_agent
            __props__.__dict__["test_frequency_in_sec"] = test_frequency_in_sec
            __props__.__dict__["is_test_successful"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["path"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:peering:ConnectionMonitorTest"), pulumi.Alias(type_="azure-native:peering/v20220101:ConnectionMonitorTest"), pulumi.Alias(type_="azure-native:peering/v20220601:ConnectionMonitorTest")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ConnectionMonitorTest, __self__).__init__(
            'azure-native:peering/v20210601:ConnectionMonitorTest',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ConnectionMonitorTest':
        """
        Get an existing ConnectionMonitorTest resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ConnectionMonitorTestArgs.__new__(ConnectionMonitorTestArgs)

        __props__.__dict__["destination"] = None
        __props__.__dict__["destination_port"] = None
        __props__.__dict__["is_test_successful"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["path"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["source_agent"] = None
        __props__.__dict__["test_frequency_in_sec"] = None
        __props__.__dict__["type"] = None
        return ConnectionMonitorTest(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def destination(self) -> pulumi.Output[Optional[str]]:
        """
        The Connection Monitor test destination
        """
        return pulumi.get(self, "destination")

    @property
    @pulumi.getter(name="destinationPort")
    def destination_port(self) -> pulumi.Output[Optional[int]]:
        """
        The Connection Monitor test destination port
        """
        return pulumi.get(self, "destination_port")

    @property
    @pulumi.getter(name="isTestSuccessful")
    def is_test_successful(self) -> pulumi.Output[bool]:
        """
        The flag that indicates if the Connection Monitor test is successful or not.
        """
        return pulumi.get(self, "is_test_successful")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def path(self) -> pulumi.Output[Sequence[str]]:
        """
        The path representing the Connection Monitor test.
        """
        return pulumi.get(self, "path")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="sourceAgent")
    def source_agent(self) -> pulumi.Output[Optional[str]]:
        """
        The Connection Monitor test source agent
        """
        return pulumi.get(self, "source_agent")

    @property
    @pulumi.getter(name="testFrequencyInSec")
    def test_frequency_in_sec(self) -> pulumi.Output[Optional[int]]:
        """
        The Connection Monitor test frequency in seconds
        """
        return pulumi.get(self, "test_frequency_in_sec")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

