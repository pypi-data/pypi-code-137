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
from ._inputs import *

__all__ = ['VirtualMachineScaleSetVMRunCommandArgs', 'VirtualMachineScaleSetVMRunCommand']

@pulumi.input_type
class VirtualMachineScaleSetVMRunCommandArgs:
    def __init__(__self__, *,
                 instance_id: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 vm_scale_set_name: pulumi.Input[str],
                 async_execution: Optional[pulumi.Input[bool]] = None,
                 error_blob_uri: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 output_blob_uri: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Sequence[pulumi.Input['RunCommandInputParameterArgs']]]] = None,
                 protected_parameters: Optional[pulumi.Input[Sequence[pulumi.Input['RunCommandInputParameterArgs']]]] = None,
                 run_as_password: Optional[pulumi.Input[str]] = None,
                 run_as_user: Optional[pulumi.Input[str]] = None,
                 run_command_name: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input['VirtualMachineRunCommandScriptSourceArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 timeout_in_seconds: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a VirtualMachineScaleSetVMRunCommand resource.
        :param pulumi.Input[str] instance_id: The instance ID of the virtual machine.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] vm_scale_set_name: The name of the VM scale set.
        :param pulumi.Input[bool] async_execution: Optional. If set to true, provisioning will complete as soon as the script starts and will not wait for script to complete.
        :param pulumi.Input[str] error_blob_uri: Specifies the Azure storage blob where script error stream will be uploaded.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] output_blob_uri: Specifies the Azure storage blob where script output stream will be uploaded.
        :param pulumi.Input[Sequence[pulumi.Input['RunCommandInputParameterArgs']]] parameters: The parameters used by the script.
        :param pulumi.Input[Sequence[pulumi.Input['RunCommandInputParameterArgs']]] protected_parameters: The parameters used by the script.
        :param pulumi.Input[str] run_as_password: Specifies the user account password on the VM when executing the run command.
        :param pulumi.Input[str] run_as_user: Specifies the user account on the VM when executing the run command.
        :param pulumi.Input[str] run_command_name: The name of the virtual machine run command.
        :param pulumi.Input['VirtualMachineRunCommandScriptSourceArgs'] source: The source of the run command script.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[int] timeout_in_seconds: The timeout in seconds to execute the run command.
        """
        pulumi.set(__self__, "instance_id", instance_id)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "vm_scale_set_name", vm_scale_set_name)
        if async_execution is None:
            async_execution = False
        if async_execution is not None:
            pulumi.set(__self__, "async_execution", async_execution)
        if error_blob_uri is not None:
            pulumi.set(__self__, "error_blob_uri", error_blob_uri)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if output_blob_uri is not None:
            pulumi.set(__self__, "output_blob_uri", output_blob_uri)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if protected_parameters is not None:
            pulumi.set(__self__, "protected_parameters", protected_parameters)
        if run_as_password is not None:
            pulumi.set(__self__, "run_as_password", run_as_password)
        if run_as_user is not None:
            pulumi.set(__self__, "run_as_user", run_as_user)
        if run_command_name is not None:
            pulumi.set(__self__, "run_command_name", run_command_name)
        if source is not None:
            pulumi.set(__self__, "source", source)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if timeout_in_seconds is not None:
            pulumi.set(__self__, "timeout_in_seconds", timeout_in_seconds)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Input[str]:
        """
        The instance ID of the virtual machine.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_id", value)

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
    @pulumi.getter(name="vmScaleSetName")
    def vm_scale_set_name(self) -> pulumi.Input[str]:
        """
        The name of the VM scale set.
        """
        return pulumi.get(self, "vm_scale_set_name")

    @vm_scale_set_name.setter
    def vm_scale_set_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "vm_scale_set_name", value)

    @property
    @pulumi.getter(name="asyncExecution")
    def async_execution(self) -> Optional[pulumi.Input[bool]]:
        """
        Optional. If set to true, provisioning will complete as soon as the script starts and will not wait for script to complete.
        """
        return pulumi.get(self, "async_execution")

    @async_execution.setter
    def async_execution(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "async_execution", value)

    @property
    @pulumi.getter(name="errorBlobUri")
    def error_blob_uri(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the Azure storage blob where script error stream will be uploaded.
        """
        return pulumi.get(self, "error_blob_uri")

    @error_blob_uri.setter
    def error_blob_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "error_blob_uri", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="outputBlobUri")
    def output_blob_uri(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the Azure storage blob where script output stream will be uploaded.
        """
        return pulumi.get(self, "output_blob_uri")

    @output_blob_uri.setter
    def output_blob_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "output_blob_uri", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RunCommandInputParameterArgs']]]]:
        """
        The parameters used by the script.
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RunCommandInputParameterArgs']]]]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter(name="protectedParameters")
    def protected_parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RunCommandInputParameterArgs']]]]:
        """
        The parameters used by the script.
        """
        return pulumi.get(self, "protected_parameters")

    @protected_parameters.setter
    def protected_parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RunCommandInputParameterArgs']]]]):
        pulumi.set(self, "protected_parameters", value)

    @property
    @pulumi.getter(name="runAsPassword")
    def run_as_password(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the user account password on the VM when executing the run command.
        """
        return pulumi.get(self, "run_as_password")

    @run_as_password.setter
    def run_as_password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "run_as_password", value)

    @property
    @pulumi.getter(name="runAsUser")
    def run_as_user(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the user account on the VM when executing the run command.
        """
        return pulumi.get(self, "run_as_user")

    @run_as_user.setter
    def run_as_user(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "run_as_user", value)

    @property
    @pulumi.getter(name="runCommandName")
    def run_command_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the virtual machine run command.
        """
        return pulumi.get(self, "run_command_name")

    @run_command_name.setter
    def run_command_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "run_command_name", value)

    @property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input['VirtualMachineRunCommandScriptSourceArgs']]:
        """
        The source of the run command script.
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: Optional[pulumi.Input['VirtualMachineRunCommandScriptSourceArgs']]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="timeoutInSeconds")
    def timeout_in_seconds(self) -> Optional[pulumi.Input[int]]:
        """
        The timeout in seconds to execute the run command.
        """
        return pulumi.get(self, "timeout_in_seconds")

    @timeout_in_seconds.setter
    def timeout_in_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "timeout_in_seconds", value)


class VirtualMachineScaleSetVMRunCommand(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 async_execution: Optional[pulumi.Input[bool]] = None,
                 error_blob_uri: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 output_blob_uri: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RunCommandInputParameterArgs']]]]] = None,
                 protected_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RunCommandInputParameterArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 run_as_password: Optional[pulumi.Input[str]] = None,
                 run_as_user: Optional[pulumi.Input[str]] = None,
                 run_command_name: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[pulumi.InputType['VirtualMachineRunCommandScriptSourceArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 timeout_in_seconds: Optional[pulumi.Input[int]] = None,
                 vm_scale_set_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Describes a Virtual Machine run command.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] async_execution: Optional. If set to true, provisioning will complete as soon as the script starts and will not wait for script to complete.
        :param pulumi.Input[str] error_blob_uri: Specifies the Azure storage blob where script error stream will be uploaded.
        :param pulumi.Input[str] instance_id: The instance ID of the virtual machine.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] output_blob_uri: Specifies the Azure storage blob where script output stream will be uploaded.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RunCommandInputParameterArgs']]]] parameters: The parameters used by the script.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RunCommandInputParameterArgs']]]] protected_parameters: The parameters used by the script.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] run_as_password: Specifies the user account password on the VM when executing the run command.
        :param pulumi.Input[str] run_as_user: Specifies the user account on the VM when executing the run command.
        :param pulumi.Input[str] run_command_name: The name of the virtual machine run command.
        :param pulumi.Input[pulumi.InputType['VirtualMachineRunCommandScriptSourceArgs']] source: The source of the run command script.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[int] timeout_in_seconds: The timeout in seconds to execute the run command.
        :param pulumi.Input[str] vm_scale_set_name: The name of the VM scale set.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VirtualMachineScaleSetVMRunCommandArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Describes a Virtual Machine run command.

        :param str resource_name: The name of the resource.
        :param VirtualMachineScaleSetVMRunCommandArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VirtualMachineScaleSetVMRunCommandArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 async_execution: Optional[pulumi.Input[bool]] = None,
                 error_blob_uri: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 output_blob_uri: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RunCommandInputParameterArgs']]]]] = None,
                 protected_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RunCommandInputParameterArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 run_as_password: Optional[pulumi.Input[str]] = None,
                 run_as_user: Optional[pulumi.Input[str]] = None,
                 run_command_name: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[pulumi.InputType['VirtualMachineRunCommandScriptSourceArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 timeout_in_seconds: Optional[pulumi.Input[int]] = None,
                 vm_scale_set_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VirtualMachineScaleSetVMRunCommandArgs.__new__(VirtualMachineScaleSetVMRunCommandArgs)

            if async_execution is None:
                async_execution = False
            __props__.__dict__["async_execution"] = async_execution
            __props__.__dict__["error_blob_uri"] = error_blob_uri
            if instance_id is None and not opts.urn:
                raise TypeError("Missing required property 'instance_id'")
            __props__.__dict__["instance_id"] = instance_id
            __props__.__dict__["location"] = location
            __props__.__dict__["output_blob_uri"] = output_blob_uri
            __props__.__dict__["parameters"] = parameters
            __props__.__dict__["protected_parameters"] = protected_parameters
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["run_as_password"] = run_as_password
            __props__.__dict__["run_as_user"] = run_as_user
            __props__.__dict__["run_command_name"] = run_command_name
            __props__.__dict__["source"] = source
            __props__.__dict__["tags"] = tags
            __props__.__dict__["timeout_in_seconds"] = timeout_in_seconds
            if vm_scale_set_name is None and not opts.urn:
                raise TypeError("Missing required property 'vm_scale_set_name'")
            __props__.__dict__["vm_scale_set_name"] = vm_scale_set_name
            __props__.__dict__["instance_view"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:compute:VirtualMachineScaleSetVMRunCommand"), pulumi.Alias(type_="azure-native:compute/v20200601:VirtualMachineScaleSetVMRunCommand"), pulumi.Alias(type_="azure-native:compute/v20201201:VirtualMachineScaleSetVMRunCommand"), pulumi.Alias(type_="azure-native:compute/v20210301:VirtualMachineScaleSetVMRunCommand"), pulumi.Alias(type_="azure-native:compute/v20210401:VirtualMachineScaleSetVMRunCommand"), pulumi.Alias(type_="azure-native:compute/v20210701:VirtualMachineScaleSetVMRunCommand"), pulumi.Alias(type_="azure-native:compute/v20211101:VirtualMachineScaleSetVMRunCommand"), pulumi.Alias(type_="azure-native:compute/v20220301:VirtualMachineScaleSetVMRunCommand")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(VirtualMachineScaleSetVMRunCommand, __self__).__init__(
            'azure-native:compute/v20220801:VirtualMachineScaleSetVMRunCommand',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VirtualMachineScaleSetVMRunCommand':
        """
        Get an existing VirtualMachineScaleSetVMRunCommand resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VirtualMachineScaleSetVMRunCommandArgs.__new__(VirtualMachineScaleSetVMRunCommandArgs)

        __props__.__dict__["async_execution"] = None
        __props__.__dict__["error_blob_uri"] = None
        __props__.__dict__["instance_view"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["output_blob_uri"] = None
        __props__.__dict__["parameters"] = None
        __props__.__dict__["protected_parameters"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["run_as_password"] = None
        __props__.__dict__["run_as_user"] = None
        __props__.__dict__["source"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["timeout_in_seconds"] = None
        __props__.__dict__["type"] = None
        return VirtualMachineScaleSetVMRunCommand(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="asyncExecution")
    def async_execution(self) -> pulumi.Output[Optional[bool]]:
        """
        Optional. If set to true, provisioning will complete as soon as the script starts and will not wait for script to complete.
        """
        return pulumi.get(self, "async_execution")

    @property
    @pulumi.getter(name="errorBlobUri")
    def error_blob_uri(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the Azure storage blob where script error stream will be uploaded.
        """
        return pulumi.get(self, "error_blob_uri")

    @property
    @pulumi.getter(name="instanceView")
    def instance_view(self) -> pulumi.Output['outputs.VirtualMachineRunCommandInstanceViewResponse']:
        """
        The virtual machine run command instance view.
        """
        return pulumi.get(self, "instance_view")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="outputBlobUri")
    def output_blob_uri(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the Azure storage blob where script output stream will be uploaded.
        """
        return pulumi.get(self, "output_blob_uri")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Sequence['outputs.RunCommandInputParameterResponse']]]:
        """
        The parameters used by the script.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="protectedParameters")
    def protected_parameters(self) -> pulumi.Output[Optional[Sequence['outputs.RunCommandInputParameterResponse']]]:
        """
        The parameters used by the script.
        """
        return pulumi.get(self, "protected_parameters")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state, which only appears in the response.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="runAsPassword")
    def run_as_password(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the user account password on the VM when executing the run command.
        """
        return pulumi.get(self, "run_as_password")

    @property
    @pulumi.getter(name="runAsUser")
    def run_as_user(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the user account on the VM when executing the run command.
        """
        return pulumi.get(self, "run_as_user")

    @property
    @pulumi.getter
    def source(self) -> pulumi.Output[Optional['outputs.VirtualMachineRunCommandScriptSourceResponse']]:
        """
        The source of the run command script.
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="timeoutInSeconds")
    def timeout_in_seconds(self) -> pulumi.Output[Optional[int]]:
        """
        The timeout in seconds to execute the run command.
        """
        return pulumi.get(self, "timeout_in_seconds")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

