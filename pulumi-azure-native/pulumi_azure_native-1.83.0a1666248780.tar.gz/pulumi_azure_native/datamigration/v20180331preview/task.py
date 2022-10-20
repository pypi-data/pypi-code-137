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

__all__ = ['TaskArgs', 'Task']

@pulumi.input_type
class TaskArgs:
    def __init__(__self__, *,
                 group_name: pulumi.Input[str],
                 project_name: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 properties: Optional[pulumi.Input[Union['ConnectToSourceSqlServerTaskPropertiesArgs', 'ConnectToTargetSqlDbTaskPropertiesArgs', 'ConnectToTargetSqlMITaskPropertiesArgs', 'GetUserTablesSqlTaskPropertiesArgs', 'MigrateSqlServerSqlDbTaskPropertiesArgs', 'MigrateSqlServerSqlMITaskPropertiesArgs', 'ValidateMigrationInputSqlServerSqlMITaskPropertiesArgs']]] = None,
                 task_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Task resource.
        :param pulumi.Input[str] group_name: Name of the resource group
        :param pulumi.Input[str] project_name: Name of the project
        :param pulumi.Input[str] service_name: Name of the service
        :param pulumi.Input[Union['ConnectToSourceSqlServerTaskPropertiesArgs', 'ConnectToTargetSqlDbTaskPropertiesArgs', 'ConnectToTargetSqlMITaskPropertiesArgs', 'GetUserTablesSqlTaskPropertiesArgs', 'MigrateSqlServerSqlDbTaskPropertiesArgs', 'MigrateSqlServerSqlMITaskPropertiesArgs', 'ValidateMigrationInputSqlServerSqlMITaskPropertiesArgs']] properties: Custom task properties
        :param pulumi.Input[str] task_name: Name of the Task
        """
        pulumi.set(__self__, "group_name", group_name)
        pulumi.set(__self__, "project_name", project_name)
        pulumi.set(__self__, "service_name", service_name)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if task_name is not None:
            pulumi.set(__self__, "task_name", task_name)

    @property
    @pulumi.getter(name="groupName")
    def group_name(self) -> pulumi.Input[str]:
        """
        Name of the resource group
        """
        return pulumi.get(self, "group_name")

    @group_name.setter
    def group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "group_name", value)

    @property
    @pulumi.getter(name="projectName")
    def project_name(self) -> pulumi.Input[str]:
        """
        Name of the project
        """
        return pulumi.get(self, "project_name")

    @project_name.setter
    def project_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "project_name", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        """
        Name of the service
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[Union['ConnectToSourceSqlServerTaskPropertiesArgs', 'ConnectToTargetSqlDbTaskPropertiesArgs', 'ConnectToTargetSqlMITaskPropertiesArgs', 'GetUserTablesSqlTaskPropertiesArgs', 'MigrateSqlServerSqlDbTaskPropertiesArgs', 'MigrateSqlServerSqlMITaskPropertiesArgs', 'ValidateMigrationInputSqlServerSqlMITaskPropertiesArgs']]]:
        """
        Custom task properties
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input[Union['ConnectToSourceSqlServerTaskPropertiesArgs', 'ConnectToTargetSqlDbTaskPropertiesArgs', 'ConnectToTargetSqlMITaskPropertiesArgs', 'GetUserTablesSqlTaskPropertiesArgs', 'MigrateSqlServerSqlDbTaskPropertiesArgs', 'MigrateSqlServerSqlMITaskPropertiesArgs', 'ValidateMigrationInputSqlServerSqlMITaskPropertiesArgs']]]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter(name="taskName")
    def task_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Task
        """
        return pulumi.get(self, "task_name")

    @task_name.setter
    def task_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "task_name", value)


warnings.warn("""Version 2018-03-31-preview will be removed in v2 of the provider.""", DeprecationWarning)


class Task(pulumi.CustomResource):
    warnings.warn("""Version 2018-03-31-preview will be removed in v2 of the provider.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 group_name: Optional[pulumi.Input[str]] = None,
                 project_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union[pulumi.InputType['ConnectToSourceSqlServerTaskPropertiesArgs'], pulumi.InputType['ConnectToTargetSqlDbTaskPropertiesArgs'], pulumi.InputType['ConnectToTargetSqlMITaskPropertiesArgs'], pulumi.InputType['GetUserTablesSqlTaskPropertiesArgs'], pulumi.InputType['MigrateSqlServerSqlDbTaskPropertiesArgs'], pulumi.InputType['MigrateSqlServerSqlMITaskPropertiesArgs'], pulumi.InputType['ValidateMigrationInputSqlServerSqlMITaskPropertiesArgs']]]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 task_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A task resource

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] group_name: Name of the resource group
        :param pulumi.Input[str] project_name: Name of the project
        :param pulumi.Input[Union[pulumi.InputType['ConnectToSourceSqlServerTaskPropertiesArgs'], pulumi.InputType['ConnectToTargetSqlDbTaskPropertiesArgs'], pulumi.InputType['ConnectToTargetSqlMITaskPropertiesArgs'], pulumi.InputType['GetUserTablesSqlTaskPropertiesArgs'], pulumi.InputType['MigrateSqlServerSqlDbTaskPropertiesArgs'], pulumi.InputType['MigrateSqlServerSqlMITaskPropertiesArgs'], pulumi.InputType['ValidateMigrationInputSqlServerSqlMITaskPropertiesArgs']]] properties: Custom task properties
        :param pulumi.Input[str] service_name: Name of the service
        :param pulumi.Input[str] task_name: Name of the Task
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TaskArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A task resource

        :param str resource_name: The name of the resource.
        :param TaskArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TaskArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 group_name: Optional[pulumi.Input[str]] = None,
                 project_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union[pulumi.InputType['ConnectToSourceSqlServerTaskPropertiesArgs'], pulumi.InputType['ConnectToTargetSqlDbTaskPropertiesArgs'], pulumi.InputType['ConnectToTargetSqlMITaskPropertiesArgs'], pulumi.InputType['GetUserTablesSqlTaskPropertiesArgs'], pulumi.InputType['MigrateSqlServerSqlDbTaskPropertiesArgs'], pulumi.InputType['MigrateSqlServerSqlMITaskPropertiesArgs'], pulumi.InputType['ValidateMigrationInputSqlServerSqlMITaskPropertiesArgs']]]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 task_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""Task is deprecated: Version 2018-03-31-preview will be removed in v2 of the provider.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TaskArgs.__new__(TaskArgs)

            if group_name is None and not opts.urn:
                raise TypeError("Missing required property 'group_name'")
            __props__.__dict__["group_name"] = group_name
            if project_name is None and not opts.urn:
                raise TypeError("Missing required property 'project_name'")
            __props__.__dict__["project_name"] = project_name
            __props__.__dict__["properties"] = properties
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["task_name"] = task_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:datamigration:Task"), pulumi.Alias(type_="azure-native:datamigration/v20171115preview:Task"), pulumi.Alias(type_="azure-native:datamigration/v20180315preview:Task"), pulumi.Alias(type_="azure-native:datamigration/v20180419:Task"), pulumi.Alias(type_="azure-native:datamigration/v20180715preview:Task"), pulumi.Alias(type_="azure-native:datamigration/v20210630:Task"), pulumi.Alias(type_="azure-native:datamigration/v20211030preview:Task"), pulumi.Alias(type_="azure-native:datamigration/v20220130preview:Task"), pulumi.Alias(type_="azure-native:datamigration/v20220330preview:Task")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Task, __self__).__init__(
            'azure-native:datamigration/v20180331preview:Task',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Task':
        """
        Get an existing Task resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TaskArgs.__new__(TaskArgs)

        __props__.__dict__["etag"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["type"] = None
        return Task(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        HTTP strong entity tag value. This is ignored if submitted.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output[Any]:
        """
        Custom task properties
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

