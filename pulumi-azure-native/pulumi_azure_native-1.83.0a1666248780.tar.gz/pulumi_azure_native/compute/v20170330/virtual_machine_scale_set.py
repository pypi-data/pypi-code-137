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

__all__ = ['VirtualMachineScaleSetArgs', 'VirtualMachineScaleSet']

@pulumi.input_type
class VirtualMachineScaleSetArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 identity: Optional[pulumi.Input['VirtualMachineScaleSetIdentityArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 overprovision: Optional[pulumi.Input[bool]] = None,
                 plan: Optional[pulumi.Input['PlanArgs']] = None,
                 single_placement_group: Optional[pulumi.Input[bool]] = None,
                 sku: Optional[pulumi.Input['SkuArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 upgrade_policy: Optional[pulumi.Input['UpgradePolicyArgs']] = None,
                 virtual_machine_profile: Optional[pulumi.Input['VirtualMachineScaleSetVMProfileArgs']] = None,
                 vm_scale_set_name: Optional[pulumi.Input[str]] = None,
                 zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a VirtualMachineScaleSet resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input['VirtualMachineScaleSetIdentityArgs'] identity: The identity of the virtual machine scale set, if configured.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[bool] overprovision: Specifies whether the Virtual Machine Scale Set should be overprovisioned.
        :param pulumi.Input['PlanArgs'] plan: Specifies information about the marketplace image used to create the virtual machine. This element is only used for marketplace images. Before you can use a marketplace image from an API, you must enable the image for programmatic use.  In the Azure portal, find the marketplace image that you want to use and then click **Want to deploy programmatically, Get Started ->**. Enter any required information and then click **Save**.
        :param pulumi.Input[bool] single_placement_group: When true this limits the scale set to a single placement group, of max size 100 virtual machines.
        :param pulumi.Input['SkuArgs'] sku: The virtual machine scale set sku.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input['UpgradePolicyArgs'] upgrade_policy: The upgrade policy.
        :param pulumi.Input['VirtualMachineScaleSetVMProfileArgs'] virtual_machine_profile: The virtual machine profile.
        :param pulumi.Input[str] vm_scale_set_name: The name of the VM scale set to create or update.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] zones: The virtual machine scale set zones. NOTE: Availability zones can only be set when you create the scale set.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if overprovision is not None:
            pulumi.set(__self__, "overprovision", overprovision)
        if plan is not None:
            pulumi.set(__self__, "plan", plan)
        if single_placement_group is not None:
            pulumi.set(__self__, "single_placement_group", single_placement_group)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if upgrade_policy is not None:
            pulumi.set(__self__, "upgrade_policy", upgrade_policy)
        if virtual_machine_profile is not None:
            pulumi.set(__self__, "virtual_machine_profile", virtual_machine_profile)
        if vm_scale_set_name is not None:
            pulumi.set(__self__, "vm_scale_set_name", vm_scale_set_name)
        if zones is not None:
            pulumi.set(__self__, "zones", zones)

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
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['VirtualMachineScaleSetIdentityArgs']]:
        """
        The identity of the virtual machine scale set, if configured.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['VirtualMachineScaleSetIdentityArgs']]):
        pulumi.set(self, "identity", value)

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
    @pulumi.getter
    def overprovision(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether the Virtual Machine Scale Set should be overprovisioned.
        """
        return pulumi.get(self, "overprovision")

    @overprovision.setter
    def overprovision(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "overprovision", value)

    @property
    @pulumi.getter
    def plan(self) -> Optional[pulumi.Input['PlanArgs']]:
        """
        Specifies information about the marketplace image used to create the virtual machine. This element is only used for marketplace images. Before you can use a marketplace image from an API, you must enable the image for programmatic use.  In the Azure portal, find the marketplace image that you want to use and then click **Want to deploy programmatically, Get Started ->**. Enter any required information and then click **Save**.
        """
        return pulumi.get(self, "plan")

    @plan.setter
    def plan(self, value: Optional[pulumi.Input['PlanArgs']]):
        pulumi.set(self, "plan", value)

    @property
    @pulumi.getter(name="singlePlacementGroup")
    def single_placement_group(self) -> Optional[pulumi.Input[bool]]:
        """
        When true this limits the scale set to a single placement group, of max size 100 virtual machines.
        """
        return pulumi.get(self, "single_placement_group")

    @single_placement_group.setter
    def single_placement_group(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "single_placement_group", value)

    @property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input['SkuArgs']]:
        """
        The virtual machine scale set sku.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input['SkuArgs']]):
        pulumi.set(self, "sku", value)

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
    @pulumi.getter(name="upgradePolicy")
    def upgrade_policy(self) -> Optional[pulumi.Input['UpgradePolicyArgs']]:
        """
        The upgrade policy.
        """
        return pulumi.get(self, "upgrade_policy")

    @upgrade_policy.setter
    def upgrade_policy(self, value: Optional[pulumi.Input['UpgradePolicyArgs']]):
        pulumi.set(self, "upgrade_policy", value)

    @property
    @pulumi.getter(name="virtualMachineProfile")
    def virtual_machine_profile(self) -> Optional[pulumi.Input['VirtualMachineScaleSetVMProfileArgs']]:
        """
        The virtual machine profile.
        """
        return pulumi.get(self, "virtual_machine_profile")

    @virtual_machine_profile.setter
    def virtual_machine_profile(self, value: Optional[pulumi.Input['VirtualMachineScaleSetVMProfileArgs']]):
        pulumi.set(self, "virtual_machine_profile", value)

    @property
    @pulumi.getter(name="vmScaleSetName")
    def vm_scale_set_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the VM scale set to create or update.
        """
        return pulumi.get(self, "vm_scale_set_name")

    @vm_scale_set_name.setter
    def vm_scale_set_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vm_scale_set_name", value)

    @property
    @pulumi.getter
    def zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The virtual machine scale set zones. NOTE: Availability zones can only be set when you create the scale set.
        """
        return pulumi.get(self, "zones")

    @zones.setter
    def zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "zones", value)


warnings.warn("""Version 2017-03-30 will be removed in v2 of the provider.""", DeprecationWarning)


class VirtualMachineScaleSet(pulumi.CustomResource):
    warnings.warn("""Version 2017-03-30 will be removed in v2 of the provider.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['VirtualMachineScaleSetIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 overprovision: Optional[pulumi.Input[bool]] = None,
                 plan: Optional[pulumi.Input[pulumi.InputType['PlanArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 single_placement_group: Optional[pulumi.Input[bool]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 upgrade_policy: Optional[pulumi.Input[pulumi.InputType['UpgradePolicyArgs']]] = None,
                 virtual_machine_profile: Optional[pulumi.Input[pulumi.InputType['VirtualMachineScaleSetVMProfileArgs']]] = None,
                 vm_scale_set_name: Optional[pulumi.Input[str]] = None,
                 zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Describes a Virtual Machine Scale Set.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['VirtualMachineScaleSetIdentityArgs']] identity: The identity of the virtual machine scale set, if configured.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[bool] overprovision: Specifies whether the Virtual Machine Scale Set should be overprovisioned.
        :param pulumi.Input[pulumi.InputType['PlanArgs']] plan: Specifies information about the marketplace image used to create the virtual machine. This element is only used for marketplace images. Before you can use a marketplace image from an API, you must enable the image for programmatic use.  In the Azure portal, find the marketplace image that you want to use and then click **Want to deploy programmatically, Get Started ->**. Enter any required information and then click **Save**.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[bool] single_placement_group: When true this limits the scale set to a single placement group, of max size 100 virtual machines.
        :param pulumi.Input[pulumi.InputType['SkuArgs']] sku: The virtual machine scale set sku.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[pulumi.InputType['UpgradePolicyArgs']] upgrade_policy: The upgrade policy.
        :param pulumi.Input[pulumi.InputType['VirtualMachineScaleSetVMProfileArgs']] virtual_machine_profile: The virtual machine profile.
        :param pulumi.Input[str] vm_scale_set_name: The name of the VM scale set to create or update.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] zones: The virtual machine scale set zones. NOTE: Availability zones can only be set when you create the scale set.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VirtualMachineScaleSetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Describes a Virtual Machine Scale Set.

        :param str resource_name: The name of the resource.
        :param VirtualMachineScaleSetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VirtualMachineScaleSetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['VirtualMachineScaleSetIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 overprovision: Optional[pulumi.Input[bool]] = None,
                 plan: Optional[pulumi.Input[pulumi.InputType['PlanArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 single_placement_group: Optional[pulumi.Input[bool]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 upgrade_policy: Optional[pulumi.Input[pulumi.InputType['UpgradePolicyArgs']]] = None,
                 virtual_machine_profile: Optional[pulumi.Input[pulumi.InputType['VirtualMachineScaleSetVMProfileArgs']]] = None,
                 vm_scale_set_name: Optional[pulumi.Input[str]] = None,
                 zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        pulumi.log.warn("""VirtualMachineScaleSet is deprecated: Version 2017-03-30 will be removed in v2 of the provider.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VirtualMachineScaleSetArgs.__new__(VirtualMachineScaleSetArgs)

            __props__.__dict__["identity"] = identity
            __props__.__dict__["location"] = location
            __props__.__dict__["overprovision"] = overprovision
            __props__.__dict__["plan"] = plan
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["single_placement_group"] = single_placement_group
            __props__.__dict__["sku"] = sku
            __props__.__dict__["tags"] = tags
            __props__.__dict__["upgrade_policy"] = upgrade_policy
            __props__.__dict__["virtual_machine_profile"] = virtual_machine_profile
            __props__.__dict__["vm_scale_set_name"] = vm_scale_set_name
            __props__.__dict__["zones"] = zones
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["unique_id"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:compute:VirtualMachineScaleSet"), pulumi.Alias(type_="azure-native:compute/v20150615:VirtualMachineScaleSet"), pulumi.Alias(type_="azure-native:compute/v20160330:VirtualMachineScaleSet"), pulumi.Alias(type_="azure-native:compute/v20160430preview:VirtualMachineScaleSet"), pulumi.Alias(type_="azure-native:compute/v20171201:VirtualMachineScaleSet"), pulumi.Alias(type_="azure-native:compute/v20180401:VirtualMachineScaleSet"), pulumi.Alias(type_="azure-native:compute/v20180601:VirtualMachineScaleSet"), pulumi.Alias(type_="azure-native:compute/v20181001:VirtualMachineScaleSet"), pulumi.Alias(type_="azure-native:compute/v20190301:VirtualMachineScaleSet"), pulumi.Alias(type_="azure-native:compute/v20190701:VirtualMachineScaleSet"), pulumi.Alias(type_="azure-native:compute/v20191201:VirtualMachineScaleSet"), pulumi.Alias(type_="azure-native:compute/v20200601:VirtualMachineScaleSet"), pulumi.Alias(type_="azure-native:compute/v20201201:VirtualMachineScaleSet"), pulumi.Alias(type_="azure-native:compute/v20210301:VirtualMachineScaleSet"), pulumi.Alias(type_="azure-native:compute/v20210401:VirtualMachineScaleSet"), pulumi.Alias(type_="azure-native:compute/v20210701:VirtualMachineScaleSet"), pulumi.Alias(type_="azure-native:compute/v20211101:VirtualMachineScaleSet"), pulumi.Alias(type_="azure-native:compute/v20220301:VirtualMachineScaleSet"), pulumi.Alias(type_="azure-native:compute/v20220801:VirtualMachineScaleSet")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(VirtualMachineScaleSet, __self__).__init__(
            'azure-native:compute/v20170330:VirtualMachineScaleSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VirtualMachineScaleSet':
        """
        Get an existing VirtualMachineScaleSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VirtualMachineScaleSetArgs.__new__(VirtualMachineScaleSetArgs)

        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["overprovision"] = None
        __props__.__dict__["plan"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["single_placement_group"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["unique_id"] = None
        __props__.__dict__["upgrade_policy"] = None
        __props__.__dict__["virtual_machine_profile"] = None
        __props__.__dict__["zones"] = None
        return VirtualMachineScaleSet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.VirtualMachineScaleSetIdentityResponse']]:
        """
        The identity of the virtual machine scale set, if configured.
        """
        return pulumi.get(self, "identity")

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
    @pulumi.getter
    def overprovision(self) -> pulumi.Output[Optional[bool]]:
        """
        Specifies whether the Virtual Machine Scale Set should be overprovisioned.
        """
        return pulumi.get(self, "overprovision")

    @property
    @pulumi.getter
    def plan(self) -> pulumi.Output[Optional['outputs.PlanResponse']]:
        """
        Specifies information about the marketplace image used to create the virtual machine. This element is only used for marketplace images. Before you can use a marketplace image from an API, you must enable the image for programmatic use.  In the Azure portal, find the marketplace image that you want to use and then click **Want to deploy programmatically, Get Started ->**. Enter any required information and then click **Save**.
        """
        return pulumi.get(self, "plan")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state, which only appears in the response.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="singlePlacementGroup")
    def single_placement_group(self) -> pulumi.Output[Optional[bool]]:
        """
        When true this limits the scale set to a single placement group, of max size 100 virtual machines.
        """
        return pulumi.get(self, "single_placement_group")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.SkuResponse']]:
        """
        The virtual machine scale set sku.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="uniqueId")
    def unique_id(self) -> pulumi.Output[str]:
        """
        Specifies the ID which uniquely identifies a Virtual Machine Scale Set.
        """
        return pulumi.get(self, "unique_id")

    @property
    @pulumi.getter(name="upgradePolicy")
    def upgrade_policy(self) -> pulumi.Output[Optional['outputs.UpgradePolicyResponse']]:
        """
        The upgrade policy.
        """
        return pulumi.get(self, "upgrade_policy")

    @property
    @pulumi.getter(name="virtualMachineProfile")
    def virtual_machine_profile(self) -> pulumi.Output[Optional['outputs.VirtualMachineScaleSetVMProfileResponse']]:
        """
        The virtual machine profile.
        """
        return pulumi.get(self, "virtual_machine_profile")

    @property
    @pulumi.getter
    def zones(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The virtual machine scale set zones. NOTE: Availability zones can only be set when you create the scale set.
        """
        return pulumi.get(self, "zones")

