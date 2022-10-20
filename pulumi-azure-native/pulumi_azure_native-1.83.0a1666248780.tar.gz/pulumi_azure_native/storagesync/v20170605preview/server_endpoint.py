# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['ServerEndpointArgs', 'ServerEndpoint']

@pulumi.input_type
class ServerEndpointArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 storage_sync_service_name: pulumi.Input[str],
                 sync_group_name: pulumi.Input[str],
                 byte_progress: Optional[pulumi.Input[int]] = None,
                 byte_total: Optional[pulumi.Input[int]] = None,
                 cloud_tiering: Optional[pulumi.Input[str]] = None,
                 current_progress_type: Optional[pulumi.Input[str]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 item_download_error_count: Optional[pulumi.Input[int]] = None,
                 item_progress_count: Optional[pulumi.Input[int]] = None,
                 item_total_count: Optional[pulumi.Input[int]] = None,
                 item_upload_error_count: Optional[pulumi.Input[int]] = None,
                 last_sync_success: Optional[pulumi.Input[str]] = None,
                 last_workflow_id: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 server_endpoint_name: Optional[pulumi.Input[str]] = None,
                 server_local_path: Optional[pulumi.Input[str]] = None,
                 server_resource_id: Optional[pulumi.Input[str]] = None,
                 sync_error_context: Optional[pulumi.Input[str]] = None,
                 sync_error_direction: Optional[pulumi.Input[str]] = None,
                 sync_error_state: Optional[pulumi.Input[str]] = None,
                 sync_error_state_timestamp: Optional[pulumi.Input[str]] = None,
                 total_progress: Optional[pulumi.Input[int]] = None,
                 volume_free_space_percent: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a ServerEndpoint resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
        :param pulumi.Input[str] storage_sync_service_name: Name of Storage Sync Service resource.
        :param pulumi.Input[str] sync_group_name: Name of Sync Group resource.
        :param pulumi.Input[int] byte_progress: Bytes in progress
        :param pulumi.Input[int] byte_total: Bytes total
        :param pulumi.Input[str] cloud_tiering: Cloud Tiering.
        :param pulumi.Input[str] current_progress_type: current progress type.
        :param pulumi.Input[str] friendly_name: Friendly Name
        :param pulumi.Input[int] item_download_error_count: Item download error count.
        :param pulumi.Input[int] item_progress_count: Item Progress Count
        :param pulumi.Input[int] item_total_count: Item Total Count
        :param pulumi.Input[int] item_upload_error_count: Item Upload Error Count.
        :param pulumi.Input[str] last_sync_success: Last Sync Success
        :param pulumi.Input[str] last_workflow_id: ServerEndpoint lastWorkflowId
        :param pulumi.Input[str] provisioning_state: ServerEndpoint Provisioning State
        :param pulumi.Input[str] server_endpoint_name: Name of Server Endpoint object.
        :param pulumi.Input[str] server_local_path: Server Local path.
        :param pulumi.Input[str] server_resource_id: Server Resource Id.
        :param pulumi.Input[str] sync_error_context: sync error context.
        :param pulumi.Input[str] sync_error_direction: Sync Error Direction.
        :param pulumi.Input[str] sync_error_state: Sync Error State
        :param pulumi.Input[str] sync_error_state_timestamp: Sync Error State Timestamp
        :param pulumi.Input[int] total_progress: Total progress
        :param pulumi.Input[int] volume_free_space_percent: Level of free space to be maintained by Cloud Tiering if it is enabled.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "storage_sync_service_name", storage_sync_service_name)
        pulumi.set(__self__, "sync_group_name", sync_group_name)
        if byte_progress is not None:
            pulumi.set(__self__, "byte_progress", byte_progress)
        if byte_total is not None:
            pulumi.set(__self__, "byte_total", byte_total)
        if cloud_tiering is not None:
            pulumi.set(__self__, "cloud_tiering", cloud_tiering)
        if current_progress_type is not None:
            pulumi.set(__self__, "current_progress_type", current_progress_type)
        if friendly_name is not None:
            pulumi.set(__self__, "friendly_name", friendly_name)
        if item_download_error_count is not None:
            pulumi.set(__self__, "item_download_error_count", item_download_error_count)
        if item_progress_count is not None:
            pulumi.set(__self__, "item_progress_count", item_progress_count)
        if item_total_count is not None:
            pulumi.set(__self__, "item_total_count", item_total_count)
        if item_upload_error_count is not None:
            pulumi.set(__self__, "item_upload_error_count", item_upload_error_count)
        if last_sync_success is not None:
            pulumi.set(__self__, "last_sync_success", last_sync_success)
        if last_workflow_id is not None:
            pulumi.set(__self__, "last_workflow_id", last_workflow_id)
        if provisioning_state is not None:
            pulumi.set(__self__, "provisioning_state", provisioning_state)
        if server_endpoint_name is not None:
            pulumi.set(__self__, "server_endpoint_name", server_endpoint_name)
        if server_local_path is not None:
            pulumi.set(__self__, "server_local_path", server_local_path)
        if server_resource_id is not None:
            pulumi.set(__self__, "server_resource_id", server_resource_id)
        if sync_error_context is not None:
            pulumi.set(__self__, "sync_error_context", sync_error_context)
        if sync_error_direction is not None:
            pulumi.set(__self__, "sync_error_direction", sync_error_direction)
        if sync_error_state is not None:
            pulumi.set(__self__, "sync_error_state", sync_error_state)
        if sync_error_state_timestamp is not None:
            pulumi.set(__self__, "sync_error_state_timestamp", sync_error_state_timestamp)
        if total_progress is not None:
            pulumi.set(__self__, "total_progress", total_progress)
        if volume_free_space_percent is not None:
            pulumi.set(__self__, "volume_free_space_percent", volume_free_space_percent)

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
    @pulumi.getter(name="storageSyncServiceName")
    def storage_sync_service_name(self) -> pulumi.Input[str]:
        """
        Name of Storage Sync Service resource.
        """
        return pulumi.get(self, "storage_sync_service_name")

    @storage_sync_service_name.setter
    def storage_sync_service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "storage_sync_service_name", value)

    @property
    @pulumi.getter(name="syncGroupName")
    def sync_group_name(self) -> pulumi.Input[str]:
        """
        Name of Sync Group resource.
        """
        return pulumi.get(self, "sync_group_name")

    @sync_group_name.setter
    def sync_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "sync_group_name", value)

    @property
    @pulumi.getter(name="byteProgress")
    def byte_progress(self) -> Optional[pulumi.Input[int]]:
        """
        Bytes in progress
        """
        return pulumi.get(self, "byte_progress")

    @byte_progress.setter
    def byte_progress(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "byte_progress", value)

    @property
    @pulumi.getter(name="byteTotal")
    def byte_total(self) -> Optional[pulumi.Input[int]]:
        """
        Bytes total
        """
        return pulumi.get(self, "byte_total")

    @byte_total.setter
    def byte_total(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "byte_total", value)

    @property
    @pulumi.getter(name="cloudTiering")
    def cloud_tiering(self) -> Optional[pulumi.Input[str]]:
        """
        Cloud Tiering.
        """
        return pulumi.get(self, "cloud_tiering")

    @cloud_tiering.setter
    def cloud_tiering(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cloud_tiering", value)

    @property
    @pulumi.getter(name="currentProgressType")
    def current_progress_type(self) -> Optional[pulumi.Input[str]]:
        """
        current progress type.
        """
        return pulumi.get(self, "current_progress_type")

    @current_progress_type.setter
    def current_progress_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "current_progress_type", value)

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[str]]:
        """
        Friendly Name
        """
        return pulumi.get(self, "friendly_name")

    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "friendly_name", value)

    @property
    @pulumi.getter(name="itemDownloadErrorCount")
    def item_download_error_count(self) -> Optional[pulumi.Input[int]]:
        """
        Item download error count.
        """
        return pulumi.get(self, "item_download_error_count")

    @item_download_error_count.setter
    def item_download_error_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "item_download_error_count", value)

    @property
    @pulumi.getter(name="itemProgressCount")
    def item_progress_count(self) -> Optional[pulumi.Input[int]]:
        """
        Item Progress Count
        """
        return pulumi.get(self, "item_progress_count")

    @item_progress_count.setter
    def item_progress_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "item_progress_count", value)

    @property
    @pulumi.getter(name="itemTotalCount")
    def item_total_count(self) -> Optional[pulumi.Input[int]]:
        """
        Item Total Count
        """
        return pulumi.get(self, "item_total_count")

    @item_total_count.setter
    def item_total_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "item_total_count", value)

    @property
    @pulumi.getter(name="itemUploadErrorCount")
    def item_upload_error_count(self) -> Optional[pulumi.Input[int]]:
        """
        Item Upload Error Count.
        """
        return pulumi.get(self, "item_upload_error_count")

    @item_upload_error_count.setter
    def item_upload_error_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "item_upload_error_count", value)

    @property
    @pulumi.getter(name="lastSyncSuccess")
    def last_sync_success(self) -> Optional[pulumi.Input[str]]:
        """
        Last Sync Success
        """
        return pulumi.get(self, "last_sync_success")

    @last_sync_success.setter
    def last_sync_success(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_sync_success", value)

    @property
    @pulumi.getter(name="lastWorkflowId")
    def last_workflow_id(self) -> Optional[pulumi.Input[str]]:
        """
        ServerEndpoint lastWorkflowId
        """
        return pulumi.get(self, "last_workflow_id")

    @last_workflow_id.setter
    def last_workflow_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_workflow_id", value)

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[str]]:
        """
        ServerEndpoint Provisioning State
        """
        return pulumi.get(self, "provisioning_state")

    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provisioning_state", value)

    @property
    @pulumi.getter(name="serverEndpointName")
    def server_endpoint_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of Server Endpoint object.
        """
        return pulumi.get(self, "server_endpoint_name")

    @server_endpoint_name.setter
    def server_endpoint_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "server_endpoint_name", value)

    @property
    @pulumi.getter(name="serverLocalPath")
    def server_local_path(self) -> Optional[pulumi.Input[str]]:
        """
        Server Local path.
        """
        return pulumi.get(self, "server_local_path")

    @server_local_path.setter
    def server_local_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "server_local_path", value)

    @property
    @pulumi.getter(name="serverResourceId")
    def server_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        Server Resource Id.
        """
        return pulumi.get(self, "server_resource_id")

    @server_resource_id.setter
    def server_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "server_resource_id", value)

    @property
    @pulumi.getter(name="syncErrorContext")
    def sync_error_context(self) -> Optional[pulumi.Input[str]]:
        """
        sync error context.
        """
        return pulumi.get(self, "sync_error_context")

    @sync_error_context.setter
    def sync_error_context(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sync_error_context", value)

    @property
    @pulumi.getter(name="syncErrorDirection")
    def sync_error_direction(self) -> Optional[pulumi.Input[str]]:
        """
        Sync Error Direction.
        """
        return pulumi.get(self, "sync_error_direction")

    @sync_error_direction.setter
    def sync_error_direction(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sync_error_direction", value)

    @property
    @pulumi.getter(name="syncErrorState")
    def sync_error_state(self) -> Optional[pulumi.Input[str]]:
        """
        Sync Error State
        """
        return pulumi.get(self, "sync_error_state")

    @sync_error_state.setter
    def sync_error_state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sync_error_state", value)

    @property
    @pulumi.getter(name="syncErrorStateTimestamp")
    def sync_error_state_timestamp(self) -> Optional[pulumi.Input[str]]:
        """
        Sync Error State Timestamp
        """
        return pulumi.get(self, "sync_error_state_timestamp")

    @sync_error_state_timestamp.setter
    def sync_error_state_timestamp(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sync_error_state_timestamp", value)

    @property
    @pulumi.getter(name="totalProgress")
    def total_progress(self) -> Optional[pulumi.Input[int]]:
        """
        Total progress
        """
        return pulumi.get(self, "total_progress")

    @total_progress.setter
    def total_progress(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "total_progress", value)

    @property
    @pulumi.getter(name="volumeFreeSpacePercent")
    def volume_free_space_percent(self) -> Optional[pulumi.Input[int]]:
        """
        Level of free space to be maintained by Cloud Tiering if it is enabled.
        """
        return pulumi.get(self, "volume_free_space_percent")

    @volume_free_space_percent.setter
    def volume_free_space_percent(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "volume_free_space_percent", value)


warnings.warn("""Version 2017-06-05-preview will be removed in v2 of the provider.""", DeprecationWarning)


class ServerEndpoint(pulumi.CustomResource):
    warnings.warn("""Version 2017-06-05-preview will be removed in v2 of the provider.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 byte_progress: Optional[pulumi.Input[int]] = None,
                 byte_total: Optional[pulumi.Input[int]] = None,
                 cloud_tiering: Optional[pulumi.Input[str]] = None,
                 current_progress_type: Optional[pulumi.Input[str]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 item_download_error_count: Optional[pulumi.Input[int]] = None,
                 item_progress_count: Optional[pulumi.Input[int]] = None,
                 item_total_count: Optional[pulumi.Input[int]] = None,
                 item_upload_error_count: Optional[pulumi.Input[int]] = None,
                 last_sync_success: Optional[pulumi.Input[str]] = None,
                 last_workflow_id: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_endpoint_name: Optional[pulumi.Input[str]] = None,
                 server_local_path: Optional[pulumi.Input[str]] = None,
                 server_resource_id: Optional[pulumi.Input[str]] = None,
                 storage_sync_service_name: Optional[pulumi.Input[str]] = None,
                 sync_error_context: Optional[pulumi.Input[str]] = None,
                 sync_error_direction: Optional[pulumi.Input[str]] = None,
                 sync_error_state: Optional[pulumi.Input[str]] = None,
                 sync_error_state_timestamp: Optional[pulumi.Input[str]] = None,
                 sync_group_name: Optional[pulumi.Input[str]] = None,
                 total_progress: Optional[pulumi.Input[int]] = None,
                 volume_free_space_percent: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Server Endpoint object.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] byte_progress: Bytes in progress
        :param pulumi.Input[int] byte_total: Bytes total
        :param pulumi.Input[str] cloud_tiering: Cloud Tiering.
        :param pulumi.Input[str] current_progress_type: current progress type.
        :param pulumi.Input[str] friendly_name: Friendly Name
        :param pulumi.Input[int] item_download_error_count: Item download error count.
        :param pulumi.Input[int] item_progress_count: Item Progress Count
        :param pulumi.Input[int] item_total_count: Item Total Count
        :param pulumi.Input[int] item_upload_error_count: Item Upload Error Count.
        :param pulumi.Input[str] last_sync_success: Last Sync Success
        :param pulumi.Input[str] last_workflow_id: ServerEndpoint lastWorkflowId
        :param pulumi.Input[str] provisioning_state: ServerEndpoint Provisioning State
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
        :param pulumi.Input[str] server_endpoint_name: Name of Server Endpoint object.
        :param pulumi.Input[str] server_local_path: Server Local path.
        :param pulumi.Input[str] server_resource_id: Server Resource Id.
        :param pulumi.Input[str] storage_sync_service_name: Name of Storage Sync Service resource.
        :param pulumi.Input[str] sync_error_context: sync error context.
        :param pulumi.Input[str] sync_error_direction: Sync Error Direction.
        :param pulumi.Input[str] sync_error_state: Sync Error State
        :param pulumi.Input[str] sync_error_state_timestamp: Sync Error State Timestamp
        :param pulumi.Input[str] sync_group_name: Name of Sync Group resource.
        :param pulumi.Input[int] total_progress: Total progress
        :param pulumi.Input[int] volume_free_space_percent: Level of free space to be maintained by Cloud Tiering if it is enabled.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServerEndpointArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Server Endpoint object.

        :param str resource_name: The name of the resource.
        :param ServerEndpointArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServerEndpointArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 byte_progress: Optional[pulumi.Input[int]] = None,
                 byte_total: Optional[pulumi.Input[int]] = None,
                 cloud_tiering: Optional[pulumi.Input[str]] = None,
                 current_progress_type: Optional[pulumi.Input[str]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 item_download_error_count: Optional[pulumi.Input[int]] = None,
                 item_progress_count: Optional[pulumi.Input[int]] = None,
                 item_total_count: Optional[pulumi.Input[int]] = None,
                 item_upload_error_count: Optional[pulumi.Input[int]] = None,
                 last_sync_success: Optional[pulumi.Input[str]] = None,
                 last_workflow_id: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_endpoint_name: Optional[pulumi.Input[str]] = None,
                 server_local_path: Optional[pulumi.Input[str]] = None,
                 server_resource_id: Optional[pulumi.Input[str]] = None,
                 storage_sync_service_name: Optional[pulumi.Input[str]] = None,
                 sync_error_context: Optional[pulumi.Input[str]] = None,
                 sync_error_direction: Optional[pulumi.Input[str]] = None,
                 sync_error_state: Optional[pulumi.Input[str]] = None,
                 sync_error_state_timestamp: Optional[pulumi.Input[str]] = None,
                 sync_group_name: Optional[pulumi.Input[str]] = None,
                 total_progress: Optional[pulumi.Input[int]] = None,
                 volume_free_space_percent: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        pulumi.log.warn("""ServerEndpoint is deprecated: Version 2017-06-05-preview will be removed in v2 of the provider.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ServerEndpointArgs.__new__(ServerEndpointArgs)

            __props__.__dict__["byte_progress"] = byte_progress
            __props__.__dict__["byte_total"] = byte_total
            __props__.__dict__["cloud_tiering"] = cloud_tiering
            __props__.__dict__["current_progress_type"] = current_progress_type
            __props__.__dict__["friendly_name"] = friendly_name
            __props__.__dict__["item_download_error_count"] = item_download_error_count
            __props__.__dict__["item_progress_count"] = item_progress_count
            __props__.__dict__["item_total_count"] = item_total_count
            __props__.__dict__["item_upload_error_count"] = item_upload_error_count
            __props__.__dict__["last_sync_success"] = last_sync_success
            __props__.__dict__["last_workflow_id"] = last_workflow_id
            __props__.__dict__["provisioning_state"] = provisioning_state
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["server_endpoint_name"] = server_endpoint_name
            __props__.__dict__["server_local_path"] = server_local_path
            __props__.__dict__["server_resource_id"] = server_resource_id
            if storage_sync_service_name is None and not opts.urn:
                raise TypeError("Missing required property 'storage_sync_service_name'")
            __props__.__dict__["storage_sync_service_name"] = storage_sync_service_name
            __props__.__dict__["sync_error_context"] = sync_error_context
            __props__.__dict__["sync_error_direction"] = sync_error_direction
            __props__.__dict__["sync_error_state"] = sync_error_state
            __props__.__dict__["sync_error_state_timestamp"] = sync_error_state_timestamp
            if sync_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'sync_group_name'")
            __props__.__dict__["sync_group_name"] = sync_group_name
            __props__.__dict__["total_progress"] = total_progress
            __props__.__dict__["volume_free_space_percent"] = volume_free_space_percent
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:storagesync:ServerEndpoint"), pulumi.Alias(type_="azure-native:storagesync/v20180402:ServerEndpoint"), pulumi.Alias(type_="azure-native:storagesync/v20180701:ServerEndpoint"), pulumi.Alias(type_="azure-native:storagesync/v20181001:ServerEndpoint"), pulumi.Alias(type_="azure-native:storagesync/v20190201:ServerEndpoint"), pulumi.Alias(type_="azure-native:storagesync/v20190301:ServerEndpoint"), pulumi.Alias(type_="azure-native:storagesync/v20190601:ServerEndpoint"), pulumi.Alias(type_="azure-native:storagesync/v20191001:ServerEndpoint"), pulumi.Alias(type_="azure-native:storagesync/v20200301:ServerEndpoint"), pulumi.Alias(type_="azure-native:storagesync/v20200901:ServerEndpoint"), pulumi.Alias(type_="azure-native:storagesync/v20220601:ServerEndpoint")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ServerEndpoint, __self__).__init__(
            'azure-native:storagesync/v20170605preview:ServerEndpoint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ServerEndpoint':
        """
        Get an existing ServerEndpoint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ServerEndpointArgs.__new__(ServerEndpointArgs)

        __props__.__dict__["byte_progress"] = None
        __props__.__dict__["byte_total"] = None
        __props__.__dict__["cloud_tiering"] = None
        __props__.__dict__["current_progress_type"] = None
        __props__.__dict__["friendly_name"] = None
        __props__.__dict__["item_download_error_count"] = None
        __props__.__dict__["item_progress_count"] = None
        __props__.__dict__["item_total_count"] = None
        __props__.__dict__["item_upload_error_count"] = None
        __props__.__dict__["last_sync_success"] = None
        __props__.__dict__["last_workflow_id"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["server_local_path"] = None
        __props__.__dict__["server_resource_id"] = None
        __props__.__dict__["sync_error_context"] = None
        __props__.__dict__["sync_error_direction"] = None
        __props__.__dict__["sync_error_state"] = None
        __props__.__dict__["sync_error_state_timestamp"] = None
        __props__.__dict__["total_progress"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["volume_free_space_percent"] = None
        return ServerEndpoint(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="byteProgress")
    def byte_progress(self) -> pulumi.Output[Optional[int]]:
        """
        Bytes in progress
        """
        return pulumi.get(self, "byte_progress")

    @property
    @pulumi.getter(name="byteTotal")
    def byte_total(self) -> pulumi.Output[Optional[int]]:
        """
        Bytes total
        """
        return pulumi.get(self, "byte_total")

    @property
    @pulumi.getter(name="cloudTiering")
    def cloud_tiering(self) -> pulumi.Output[Optional[str]]:
        """
        Cloud Tiering.
        """
        return pulumi.get(self, "cloud_tiering")

    @property
    @pulumi.getter(name="currentProgressType")
    def current_progress_type(self) -> pulumi.Output[Optional[str]]:
        """
        current progress type.
        """
        return pulumi.get(self, "current_progress_type")

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> pulumi.Output[Optional[str]]:
        """
        Friendly Name
        """
        return pulumi.get(self, "friendly_name")

    @property
    @pulumi.getter(name="itemDownloadErrorCount")
    def item_download_error_count(self) -> pulumi.Output[Optional[int]]:
        """
        Item download error count.
        """
        return pulumi.get(self, "item_download_error_count")

    @property
    @pulumi.getter(name="itemProgressCount")
    def item_progress_count(self) -> pulumi.Output[Optional[int]]:
        """
        Item Progress Count
        """
        return pulumi.get(self, "item_progress_count")

    @property
    @pulumi.getter(name="itemTotalCount")
    def item_total_count(self) -> pulumi.Output[Optional[int]]:
        """
        Item Total Count
        """
        return pulumi.get(self, "item_total_count")

    @property
    @pulumi.getter(name="itemUploadErrorCount")
    def item_upload_error_count(self) -> pulumi.Output[Optional[int]]:
        """
        Item Upload Error Count.
        """
        return pulumi.get(self, "item_upload_error_count")

    @property
    @pulumi.getter(name="lastSyncSuccess")
    def last_sync_success(self) -> pulumi.Output[Optional[str]]:
        """
        Last Sync Success
        """
        return pulumi.get(self, "last_sync_success")

    @property
    @pulumi.getter(name="lastWorkflowId")
    def last_workflow_id(self) -> pulumi.Output[Optional[str]]:
        """
        ServerEndpoint lastWorkflowId
        """
        return pulumi.get(self, "last_workflow_id")

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
        ServerEndpoint Provisioning State
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="serverLocalPath")
    def server_local_path(self) -> pulumi.Output[Optional[str]]:
        """
        Server Local path.
        """
        return pulumi.get(self, "server_local_path")

    @property
    @pulumi.getter(name="serverResourceId")
    def server_resource_id(self) -> pulumi.Output[Optional[str]]:
        """
        Server Resource Id.
        """
        return pulumi.get(self, "server_resource_id")

    @property
    @pulumi.getter(name="syncErrorContext")
    def sync_error_context(self) -> pulumi.Output[Optional[str]]:
        """
        sync error context.
        """
        return pulumi.get(self, "sync_error_context")

    @property
    @pulumi.getter(name="syncErrorDirection")
    def sync_error_direction(self) -> pulumi.Output[Optional[str]]:
        """
        Sync Error Direction.
        """
        return pulumi.get(self, "sync_error_direction")

    @property
    @pulumi.getter(name="syncErrorState")
    def sync_error_state(self) -> pulumi.Output[Optional[str]]:
        """
        Sync Error State
        """
        return pulumi.get(self, "sync_error_state")

    @property
    @pulumi.getter(name="syncErrorStateTimestamp")
    def sync_error_state_timestamp(self) -> pulumi.Output[Optional[str]]:
        """
        Sync Error State Timestamp
        """
        return pulumi.get(self, "sync_error_state_timestamp")

    @property
    @pulumi.getter(name="totalProgress")
    def total_progress(self) -> pulumi.Output[Optional[int]]:
        """
        Total progress
        """
        return pulumi.get(self, "total_progress")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="volumeFreeSpacePercent")
    def volume_free_space_percent(self) -> pulumi.Output[Optional[int]]:
        """
        Level of free space to be maintained by Cloud Tiering if it is enabled.
        """
        return pulumi.get(self, "volume_free_space_percent")

