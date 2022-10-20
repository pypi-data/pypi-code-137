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

__all__ = [
    'GetBackupScheduleGroupResult',
    'AwaitableGetBackupScheduleGroupResult',
    'get_backup_schedule_group',
    'get_backup_schedule_group_output',
]

warnings.warn("""Version 2016-10-01 will be removed in v2 of the provider.""", DeprecationWarning)

@pulumi.output_type
class GetBackupScheduleGroupResult:
    """
    The Backup Schedule Group
    """
    def __init__(__self__, id=None, name=None, start_time=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if start_time and not isinstance(start_time, dict):
            raise TypeError("Expected argument 'start_time' to be a dict")
        pulumi.set(__self__, "start_time", start_time)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The identifier.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> 'outputs.TimeResponse':
        """
        The start time. When this field is specified we will generate Default GrandFather Father Son Backup Schedules.
        """
        return pulumi.get(self, "start_time")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type.
        """
        return pulumi.get(self, "type")


class AwaitableGetBackupScheduleGroupResult(GetBackupScheduleGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBackupScheduleGroupResult(
            id=self.id,
            name=self.name,
            start_time=self.start_time,
            type=self.type)


def get_backup_schedule_group(device_name: Optional[str] = None,
                              manager_name: Optional[str] = None,
                              resource_group_name: Optional[str] = None,
                              schedule_group_name: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBackupScheduleGroupResult:
    """
    The Backup Schedule Group


    :param str device_name: The name of the device.
    :param str manager_name: The manager name
    :param str resource_group_name: The resource group name
    :param str schedule_group_name: The name of the schedule group.
    """
    pulumi.log.warn("""get_backup_schedule_group is deprecated: Version 2016-10-01 will be removed in v2 of the provider.""")
    __args__ = dict()
    __args__['deviceName'] = device_name
    __args__['managerName'] = manager_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['scheduleGroupName'] = schedule_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:storsimple/v20161001:getBackupScheduleGroup', __args__, opts=opts, typ=GetBackupScheduleGroupResult).value

    return AwaitableGetBackupScheduleGroupResult(
        id=__ret__.id,
        name=__ret__.name,
        start_time=__ret__.start_time,
        type=__ret__.type)


@_utilities.lift_output_func(get_backup_schedule_group)
def get_backup_schedule_group_output(device_name: Optional[pulumi.Input[str]] = None,
                                     manager_name: Optional[pulumi.Input[str]] = None,
                                     resource_group_name: Optional[pulumi.Input[str]] = None,
                                     schedule_group_name: Optional[pulumi.Input[str]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBackupScheduleGroupResult]:
    """
    The Backup Schedule Group


    :param str device_name: The name of the device.
    :param str manager_name: The manager name
    :param str resource_group_name: The resource group name
    :param str schedule_group_name: The name of the schedule group.
    """
    pulumi.log.warn("""get_backup_schedule_group is deprecated: Version 2016-10-01 will be removed in v2 of the provider.""")
    ...
