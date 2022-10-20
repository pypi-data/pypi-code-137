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

__all__ = ['IotConnectorArgs', 'IotConnector']

@pulumi.input_type
class IotConnectorArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 device_mapping: Optional[pulumi.Input['IotMappingPropertiesArgs']] = None,
                 identity: Optional[pulumi.Input['ServiceManagedIdentityIdentityArgs']] = None,
                 ingestion_endpoint_configuration: Optional[pulumi.Input['IotEventHubIngestionEndpointConfigurationArgs']] = None,
                 iot_connector_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a IotConnector resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the service instance.
        :param pulumi.Input[str] workspace_name: The name of workspace resource.
        :param pulumi.Input['IotMappingPropertiesArgs'] device_mapping: Device Mappings.
        :param pulumi.Input['ServiceManagedIdentityIdentityArgs'] identity: Setting indicating whether the service has a managed identity associated with it.
        :param pulumi.Input['IotEventHubIngestionEndpointConfigurationArgs'] ingestion_endpoint_configuration: Source configuration.
        :param pulumi.Input[str] iot_connector_name: The name of IoT Connector resource.
        :param pulumi.Input[str] location: The resource location.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if device_mapping is not None:
            pulumi.set(__self__, "device_mapping", device_mapping)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if ingestion_endpoint_configuration is not None:
            pulumi.set(__self__, "ingestion_endpoint_configuration", ingestion_endpoint_configuration)
        if iot_connector_name is not None:
            pulumi.set(__self__, "iot_connector_name", iot_connector_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group that contains the service instance.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[str]:
        """
        The name of workspace resource.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter(name="deviceMapping")
    def device_mapping(self) -> Optional[pulumi.Input['IotMappingPropertiesArgs']]:
        """
        Device Mappings.
        """
        return pulumi.get(self, "device_mapping")

    @device_mapping.setter
    def device_mapping(self, value: Optional[pulumi.Input['IotMappingPropertiesArgs']]):
        pulumi.set(self, "device_mapping", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['ServiceManagedIdentityIdentityArgs']]:
        """
        Setting indicating whether the service has a managed identity associated with it.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['ServiceManagedIdentityIdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter(name="ingestionEndpointConfiguration")
    def ingestion_endpoint_configuration(self) -> Optional[pulumi.Input['IotEventHubIngestionEndpointConfigurationArgs']]:
        """
        Source configuration.
        """
        return pulumi.get(self, "ingestion_endpoint_configuration")

    @ingestion_endpoint_configuration.setter
    def ingestion_endpoint_configuration(self, value: Optional[pulumi.Input['IotEventHubIngestionEndpointConfigurationArgs']]):
        pulumi.set(self, "ingestion_endpoint_configuration", value)

    @property
    @pulumi.getter(name="iotConnectorName")
    def iot_connector_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of IoT Connector resource.
        """
        return pulumi.get(self, "iot_connector_name")

    @iot_connector_name.setter
    def iot_connector_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "iot_connector_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The resource location.
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


class IotConnector(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 device_mapping: Optional[pulumi.Input[pulumi.InputType['IotMappingPropertiesArgs']]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ServiceManagedIdentityIdentityArgs']]] = None,
                 ingestion_endpoint_configuration: Optional[pulumi.Input[pulumi.InputType['IotEventHubIngestionEndpointConfigurationArgs']]] = None,
                 iot_connector_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        IoT Connector definition.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['IotMappingPropertiesArgs']] device_mapping: Device Mappings.
        :param pulumi.Input[pulumi.InputType['ServiceManagedIdentityIdentityArgs']] identity: Setting indicating whether the service has a managed identity associated with it.
        :param pulumi.Input[pulumi.InputType['IotEventHubIngestionEndpointConfigurationArgs']] ingestion_endpoint_configuration: Source configuration.
        :param pulumi.Input[str] iot_connector_name: The name of IoT Connector resource.
        :param pulumi.Input[str] location: The resource location.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the service instance.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] workspace_name: The name of workspace resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IotConnectorArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        IoT Connector definition.

        :param str resource_name: The name of the resource.
        :param IotConnectorArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IotConnectorArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 device_mapping: Optional[pulumi.Input[pulumi.InputType['IotMappingPropertiesArgs']]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ServiceManagedIdentityIdentityArgs']]] = None,
                 ingestion_endpoint_configuration: Optional[pulumi.Input[pulumi.InputType['IotEventHubIngestionEndpointConfigurationArgs']]] = None,
                 iot_connector_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IotConnectorArgs.__new__(IotConnectorArgs)

            __props__.__dict__["device_mapping"] = device_mapping
            __props__.__dict__["identity"] = identity
            __props__.__dict__["ingestion_endpoint_configuration"] = ingestion_endpoint_configuration
            __props__.__dict__["iot_connector_name"] = iot_connector_name
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:healthcareapis:IotConnector"), pulumi.Alias(type_="azure-native:healthcareapis/v20210601preview:IotConnector"), pulumi.Alias(type_="azure-native:healthcareapis/v20211101:IotConnector"), pulumi.Alias(type_="azure-native:healthcareapis/v20220515:IotConnector"), pulumi.Alias(type_="azure-native:healthcareapis/v20220601:IotConnector")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(IotConnector, __self__).__init__(
            'azure-native:healthcareapis/v20220131preview:IotConnector',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'IotConnector':
        """
        Get an existing IotConnector resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = IotConnectorArgs.__new__(IotConnectorArgs)

        __props__.__dict__["device_mapping"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["ingestion_endpoint_configuration"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return IotConnector(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="deviceMapping")
    def device_mapping(self) -> pulumi.Output[Optional['outputs.IotMappingPropertiesResponse']]:
        """
        Device Mappings.
        """
        return pulumi.get(self, "device_mapping")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        An etag associated with the resource, used for optimistic concurrency when editing it.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.ServiceManagedIdentityResponseIdentity']]:
        """
        Setting indicating whether the service has a managed identity associated with it.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="ingestionEndpointConfiguration")
    def ingestion_endpoint_configuration(self) -> pulumi.Output[Optional['outputs.IotEventHubIngestionEndpointConfigurationResponse']]:
        """
        Source configuration.
        """
        return pulumi.get(self, "ingestion_endpoint_configuration")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

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
        The resource type.
        """
        return pulumi.get(self, "type")

