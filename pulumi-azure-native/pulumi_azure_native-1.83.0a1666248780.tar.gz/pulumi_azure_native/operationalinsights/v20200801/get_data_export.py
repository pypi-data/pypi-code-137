# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetDataExportResult',
    'AwaitableGetDataExportResult',
    'get_data_export',
    'get_data_export_output',
]

@pulumi.output_type
class GetDataExportResult:
    """
    The top level data export resource container.
    """
    def __init__(__self__, created_date=None, data_export_id=None, enable=None, event_hub_name=None, id=None, last_modified_date=None, name=None, resource_id=None, table_names=None, type=None):
        if created_date and not isinstance(created_date, str):
            raise TypeError("Expected argument 'created_date' to be a str")
        pulumi.set(__self__, "created_date", created_date)
        if data_export_id and not isinstance(data_export_id, str):
            raise TypeError("Expected argument 'data_export_id' to be a str")
        pulumi.set(__self__, "data_export_id", data_export_id)
        if enable and not isinstance(enable, bool):
            raise TypeError("Expected argument 'enable' to be a bool")
        pulumi.set(__self__, "enable", enable)
        if event_hub_name and not isinstance(event_hub_name, str):
            raise TypeError("Expected argument 'event_hub_name' to be a str")
        pulumi.set(__self__, "event_hub_name", event_hub_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if last_modified_date and not isinstance(last_modified_date, str):
            raise TypeError("Expected argument 'last_modified_date' to be a str")
        pulumi.set(__self__, "last_modified_date", last_modified_date)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if resource_id and not isinstance(resource_id, str):
            raise TypeError("Expected argument 'resource_id' to be a str")
        pulumi.set(__self__, "resource_id", resource_id)
        if table_names and not isinstance(table_names, list):
            raise TypeError("Expected argument 'table_names' to be a list")
        pulumi.set(__self__, "table_names", table_names)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> Optional[str]:
        """
        The latest data export rule modification time.
        """
        return pulumi.get(self, "created_date")

    @property
    @pulumi.getter(name="dataExportId")
    def data_export_id(self) -> Optional[str]:
        """
        The data export rule ID.
        """
        return pulumi.get(self, "data_export_id")

    @property
    @pulumi.getter
    def enable(self) -> Optional[bool]:
        """
        Active when enabled.
        """
        return pulumi.get(self, "enable")

    @property
    @pulumi.getter(name="eventHubName")
    def event_hub_name(self) -> Optional[str]:
        """
        Optional. Allows to define an Event Hub name. Not applicable when destination is Storage Account.
        """
        return pulumi.get(self, "event_hub_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastModifiedDate")
    def last_modified_date(self) -> Optional[str]:
        """
        Date and time when the export was last modified.
        """
        return pulumi.get(self, "last_modified_date")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> str:
        """
        The destination resource ID. This can be copied from the Properties entry of the destination resource in Azure.
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter(name="tableNames")
    def table_names(self) -> Sequence[str]:
        """
        An array of tables to export, for example: [“Heartbeat, SecurityEvent”].
        """
        return pulumi.get(self, "table_names")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetDataExportResult(GetDataExportResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDataExportResult(
            created_date=self.created_date,
            data_export_id=self.data_export_id,
            enable=self.enable,
            event_hub_name=self.event_hub_name,
            id=self.id,
            last_modified_date=self.last_modified_date,
            name=self.name,
            resource_id=self.resource_id,
            table_names=self.table_names,
            type=self.type)


def get_data_export(data_export_name: Optional[str] = None,
                    resource_group_name: Optional[str] = None,
                    workspace_name: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDataExportResult:
    """
    The top level data export resource container.


    :param str data_export_name: The data export rule name.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace.
    """
    __args__ = dict()
    __args__['dataExportName'] = data_export_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:operationalinsights/v20200801:getDataExport', __args__, opts=opts, typ=GetDataExportResult).value

    return AwaitableGetDataExportResult(
        created_date=__ret__.created_date,
        data_export_id=__ret__.data_export_id,
        enable=__ret__.enable,
        event_hub_name=__ret__.event_hub_name,
        id=__ret__.id,
        last_modified_date=__ret__.last_modified_date,
        name=__ret__.name,
        resource_id=__ret__.resource_id,
        table_names=__ret__.table_names,
        type=__ret__.type)


@_utilities.lift_output_func(get_data_export)
def get_data_export_output(data_export_name: Optional[pulumi.Input[str]] = None,
                           resource_group_name: Optional[pulumi.Input[str]] = None,
                           workspace_name: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDataExportResult]:
    """
    The top level data export resource container.


    :param str data_export_name: The data export rule name.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace.
    """
    ...
