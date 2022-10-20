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

__all__ = [
    'ListWebAppBackupStatusSecretsSlotResult',
    'AwaitableListWebAppBackupStatusSecretsSlotResult',
    'list_web_app_backup_status_secrets_slot',
    'list_web_app_backup_status_secrets_slot_output',
]

@pulumi.output_type
class ListWebAppBackupStatusSecretsSlotResult:
    """
    Backup description.
    """
    def __init__(__self__, backup_id=None, blob_name=None, correlation_id=None, created=None, databases=None, finished_time_stamp=None, id=None, kind=None, last_restore_time_stamp=None, log=None, name=None, scheduled=None, size_in_bytes=None, status=None, storage_account_url=None, type=None, website_size_in_bytes=None):
        if backup_id and not isinstance(backup_id, int):
            raise TypeError("Expected argument 'backup_id' to be a int")
        pulumi.set(__self__, "backup_id", backup_id)
        if blob_name and not isinstance(blob_name, str):
            raise TypeError("Expected argument 'blob_name' to be a str")
        pulumi.set(__self__, "blob_name", blob_name)
        if correlation_id and not isinstance(correlation_id, str):
            raise TypeError("Expected argument 'correlation_id' to be a str")
        pulumi.set(__self__, "correlation_id", correlation_id)
        if created and not isinstance(created, str):
            raise TypeError("Expected argument 'created' to be a str")
        pulumi.set(__self__, "created", created)
        if databases and not isinstance(databases, list):
            raise TypeError("Expected argument 'databases' to be a list")
        pulumi.set(__self__, "databases", databases)
        if finished_time_stamp and not isinstance(finished_time_stamp, str):
            raise TypeError("Expected argument 'finished_time_stamp' to be a str")
        pulumi.set(__self__, "finished_time_stamp", finished_time_stamp)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if last_restore_time_stamp and not isinstance(last_restore_time_stamp, str):
            raise TypeError("Expected argument 'last_restore_time_stamp' to be a str")
        pulumi.set(__self__, "last_restore_time_stamp", last_restore_time_stamp)
        if log and not isinstance(log, str):
            raise TypeError("Expected argument 'log' to be a str")
        pulumi.set(__self__, "log", log)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if scheduled and not isinstance(scheduled, bool):
            raise TypeError("Expected argument 'scheduled' to be a bool")
        pulumi.set(__self__, "scheduled", scheduled)
        if size_in_bytes and not isinstance(size_in_bytes, float):
            raise TypeError("Expected argument 'size_in_bytes' to be a float")
        pulumi.set(__self__, "size_in_bytes", size_in_bytes)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if storage_account_url and not isinstance(storage_account_url, str):
            raise TypeError("Expected argument 'storage_account_url' to be a str")
        pulumi.set(__self__, "storage_account_url", storage_account_url)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if website_size_in_bytes and not isinstance(website_size_in_bytes, float):
            raise TypeError("Expected argument 'website_size_in_bytes' to be a float")
        pulumi.set(__self__, "website_size_in_bytes", website_size_in_bytes)

    @property
    @pulumi.getter(name="backupId")
    def backup_id(self) -> int:
        """
        Id of the backup.
        """
        return pulumi.get(self, "backup_id")

    @property
    @pulumi.getter(name="blobName")
    def blob_name(self) -> str:
        """
        Name of the blob which contains data for this backup.
        """
        return pulumi.get(self, "blob_name")

    @property
    @pulumi.getter(name="correlationId")
    def correlation_id(self) -> str:
        """
        Unique correlation identifier. Please use this along with the timestamp while communicating with Azure support.
        """
        return pulumi.get(self, "correlation_id")

    @property
    @pulumi.getter
    def created(self) -> str:
        """
        Timestamp of the backup creation.
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter
    def databases(self) -> Sequence['outputs.DatabaseBackupSettingResponse']:
        """
        List of databases included in the backup.
        """
        return pulumi.get(self, "databases")

    @property
    @pulumi.getter(name="finishedTimeStamp")
    def finished_time_stamp(self) -> str:
        """
        Timestamp when this backup finished.
        """
        return pulumi.get(self, "finished_time_stamp")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Kind of resource.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="lastRestoreTimeStamp")
    def last_restore_time_stamp(self) -> str:
        """
        Timestamp of a last restore operation which used this backup.
        """
        return pulumi.get(self, "last_restore_time_stamp")

    @property
    @pulumi.getter
    def log(self) -> str:
        """
        Details regarding this backup. Might contain an error message.
        """
        return pulumi.get(self, "log")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource Name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def scheduled(self) -> bool:
        """
        True if this backup has been created due to a schedule being triggered.
        """
        return pulumi.get(self, "scheduled")

    @property
    @pulumi.getter(name="sizeInBytes")
    def size_in_bytes(self) -> float:
        """
        Size of the backup in bytes.
        """
        return pulumi.get(self, "size_in_bytes")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Backup status.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="storageAccountUrl")
    def storage_account_url(self) -> str:
        """
        SAS URL for the storage account container which contains this backup.
        """
        return pulumi.get(self, "storage_account_url")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="websiteSizeInBytes")
    def website_size_in_bytes(self) -> float:
        """
        Size of the original web app which has been backed up.
        """
        return pulumi.get(self, "website_size_in_bytes")


class AwaitableListWebAppBackupStatusSecretsSlotResult(ListWebAppBackupStatusSecretsSlotResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListWebAppBackupStatusSecretsSlotResult(
            backup_id=self.backup_id,
            blob_name=self.blob_name,
            correlation_id=self.correlation_id,
            created=self.created,
            databases=self.databases,
            finished_time_stamp=self.finished_time_stamp,
            id=self.id,
            kind=self.kind,
            last_restore_time_stamp=self.last_restore_time_stamp,
            log=self.log,
            name=self.name,
            scheduled=self.scheduled,
            size_in_bytes=self.size_in_bytes,
            status=self.status,
            storage_account_url=self.storage_account_url,
            type=self.type,
            website_size_in_bytes=self.website_size_in_bytes)


def list_web_app_backup_status_secrets_slot(backup_id: Optional[str] = None,
                                            backup_name: Optional[str] = None,
                                            backup_schedule: Optional[pulumi.InputType['BackupSchedule']] = None,
                                            databases: Optional[Sequence[pulumi.InputType['DatabaseBackupSetting']]] = None,
                                            enabled: Optional[bool] = None,
                                            kind: Optional[str] = None,
                                            name: Optional[str] = None,
                                            resource_group_name: Optional[str] = None,
                                            slot: Optional[str] = None,
                                            storage_account_url: Optional[str] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListWebAppBackupStatusSecretsSlotResult:
    """
    Backup description.


    :param str backup_id: ID of backup.
    :param str backup_name: Name of the backup.
    :param pulumi.InputType['BackupSchedule'] backup_schedule: Schedule for the backup if it is executed periodically.
    :param Sequence[pulumi.InputType['DatabaseBackupSetting']] databases: Databases included in the backup.
    :param bool enabled: True if the backup schedule is enabled (must be included in that case), false if the backup schedule should be disabled.
    :param str kind: Kind of resource.
    :param str name: Name of web app.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    :param str slot: Name of web app slot. If not specified then will default to production slot.
    :param str storage_account_url: SAS URL to the container.
    """
    __args__ = dict()
    __args__['backupId'] = backup_id
    __args__['backupName'] = backup_name
    __args__['backupSchedule'] = backup_schedule
    __args__['databases'] = databases
    __args__['enabled'] = enabled
    __args__['kind'] = kind
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    __args__['slot'] = slot
    __args__['storageAccountUrl'] = storage_account_url
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:web/v20201201:listWebAppBackupStatusSecretsSlot', __args__, opts=opts, typ=ListWebAppBackupStatusSecretsSlotResult).value

    return AwaitableListWebAppBackupStatusSecretsSlotResult(
        backup_id=__ret__.backup_id,
        blob_name=__ret__.blob_name,
        correlation_id=__ret__.correlation_id,
        created=__ret__.created,
        databases=__ret__.databases,
        finished_time_stamp=__ret__.finished_time_stamp,
        id=__ret__.id,
        kind=__ret__.kind,
        last_restore_time_stamp=__ret__.last_restore_time_stamp,
        log=__ret__.log,
        name=__ret__.name,
        scheduled=__ret__.scheduled,
        size_in_bytes=__ret__.size_in_bytes,
        status=__ret__.status,
        storage_account_url=__ret__.storage_account_url,
        type=__ret__.type,
        website_size_in_bytes=__ret__.website_size_in_bytes)


@_utilities.lift_output_func(list_web_app_backup_status_secrets_slot)
def list_web_app_backup_status_secrets_slot_output(backup_id: Optional[pulumi.Input[str]] = None,
                                                   backup_name: Optional[pulumi.Input[Optional[str]]] = None,
                                                   backup_schedule: Optional[pulumi.Input[Optional[pulumi.InputType['BackupSchedule']]]] = None,
                                                   databases: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['DatabaseBackupSetting']]]]] = None,
                                                   enabled: Optional[pulumi.Input[Optional[bool]]] = None,
                                                   kind: Optional[pulumi.Input[Optional[str]]] = None,
                                                   name: Optional[pulumi.Input[str]] = None,
                                                   resource_group_name: Optional[pulumi.Input[str]] = None,
                                                   slot: Optional[pulumi.Input[str]] = None,
                                                   storage_account_url: Optional[pulumi.Input[str]] = None,
                                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListWebAppBackupStatusSecretsSlotResult]:
    """
    Backup description.


    :param str backup_id: ID of backup.
    :param str backup_name: Name of the backup.
    :param pulumi.InputType['BackupSchedule'] backup_schedule: Schedule for the backup if it is executed periodically.
    :param Sequence[pulumi.InputType['DatabaseBackupSetting']] databases: Databases included in the backup.
    :param bool enabled: True if the backup schedule is enabled (must be included in that case), false if the backup schedule should be disabled.
    :param str kind: Kind of resource.
    :param str name: Name of web app.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    :param str slot: Name of web app slot. If not specified then will default to production slot.
    :param str storage_account_url: SAS URL to the container.
    """
    ...
