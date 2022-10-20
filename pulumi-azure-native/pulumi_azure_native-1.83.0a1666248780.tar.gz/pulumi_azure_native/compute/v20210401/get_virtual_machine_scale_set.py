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
    'GetVirtualMachineScaleSetResult',
    'AwaitableGetVirtualMachineScaleSetResult',
    'get_virtual_machine_scale_set',
    'get_virtual_machine_scale_set_output',
]

@pulumi.output_type
class GetVirtualMachineScaleSetResult:
    """
    Describes a Virtual Machine Scale Set.
    """
    def __init__(__self__, additional_capabilities=None, automatic_repairs_policy=None, do_not_run_extensions_on_overprovisioned_vms=None, extended_location=None, host_group=None, id=None, identity=None, location=None, name=None, orchestration_mode=None, overprovision=None, plan=None, platform_fault_domain_count=None, provisioning_state=None, proximity_placement_group=None, scale_in_policy=None, single_placement_group=None, sku=None, spot_restore_policy=None, tags=None, type=None, unique_id=None, upgrade_policy=None, virtual_machine_profile=None, zone_balance=None, zones=None):
        if additional_capabilities and not isinstance(additional_capabilities, dict):
            raise TypeError("Expected argument 'additional_capabilities' to be a dict")
        pulumi.set(__self__, "additional_capabilities", additional_capabilities)
        if automatic_repairs_policy and not isinstance(automatic_repairs_policy, dict):
            raise TypeError("Expected argument 'automatic_repairs_policy' to be a dict")
        pulumi.set(__self__, "automatic_repairs_policy", automatic_repairs_policy)
        if do_not_run_extensions_on_overprovisioned_vms and not isinstance(do_not_run_extensions_on_overprovisioned_vms, bool):
            raise TypeError("Expected argument 'do_not_run_extensions_on_overprovisioned_vms' to be a bool")
        pulumi.set(__self__, "do_not_run_extensions_on_overprovisioned_vms", do_not_run_extensions_on_overprovisioned_vms)
        if extended_location and not isinstance(extended_location, dict):
            raise TypeError("Expected argument 'extended_location' to be a dict")
        pulumi.set(__self__, "extended_location", extended_location)
        if host_group and not isinstance(host_group, dict):
            raise TypeError("Expected argument 'host_group' to be a dict")
        pulumi.set(__self__, "host_group", host_group)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if orchestration_mode and not isinstance(orchestration_mode, str):
            raise TypeError("Expected argument 'orchestration_mode' to be a str")
        pulumi.set(__self__, "orchestration_mode", orchestration_mode)
        if overprovision and not isinstance(overprovision, bool):
            raise TypeError("Expected argument 'overprovision' to be a bool")
        pulumi.set(__self__, "overprovision", overprovision)
        if plan and not isinstance(plan, dict):
            raise TypeError("Expected argument 'plan' to be a dict")
        pulumi.set(__self__, "plan", plan)
        if platform_fault_domain_count and not isinstance(platform_fault_domain_count, int):
            raise TypeError("Expected argument 'platform_fault_domain_count' to be a int")
        pulumi.set(__self__, "platform_fault_domain_count", platform_fault_domain_count)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if proximity_placement_group and not isinstance(proximity_placement_group, dict):
            raise TypeError("Expected argument 'proximity_placement_group' to be a dict")
        pulumi.set(__self__, "proximity_placement_group", proximity_placement_group)
        if scale_in_policy and not isinstance(scale_in_policy, dict):
            raise TypeError("Expected argument 'scale_in_policy' to be a dict")
        pulumi.set(__self__, "scale_in_policy", scale_in_policy)
        if single_placement_group and not isinstance(single_placement_group, bool):
            raise TypeError("Expected argument 'single_placement_group' to be a bool")
        pulumi.set(__self__, "single_placement_group", single_placement_group)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if spot_restore_policy and not isinstance(spot_restore_policy, dict):
            raise TypeError("Expected argument 'spot_restore_policy' to be a dict")
        pulumi.set(__self__, "spot_restore_policy", spot_restore_policy)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if unique_id and not isinstance(unique_id, str):
            raise TypeError("Expected argument 'unique_id' to be a str")
        pulumi.set(__self__, "unique_id", unique_id)
        if upgrade_policy and not isinstance(upgrade_policy, dict):
            raise TypeError("Expected argument 'upgrade_policy' to be a dict")
        pulumi.set(__self__, "upgrade_policy", upgrade_policy)
        if virtual_machine_profile and not isinstance(virtual_machine_profile, dict):
            raise TypeError("Expected argument 'virtual_machine_profile' to be a dict")
        pulumi.set(__self__, "virtual_machine_profile", virtual_machine_profile)
        if zone_balance and not isinstance(zone_balance, bool):
            raise TypeError("Expected argument 'zone_balance' to be a bool")
        pulumi.set(__self__, "zone_balance", zone_balance)
        if zones and not isinstance(zones, list):
            raise TypeError("Expected argument 'zones' to be a list")
        pulumi.set(__self__, "zones", zones)

    @property
    @pulumi.getter(name="additionalCapabilities")
    def additional_capabilities(self) -> Optional['outputs.AdditionalCapabilitiesResponse']:
        """
        Specifies additional capabilities enabled or disabled on the Virtual Machines in the Virtual Machine Scale Set. For instance: whether the Virtual Machines have the capability to support attaching managed data disks with UltraSSD_LRS storage account type.
        """
        return pulumi.get(self, "additional_capabilities")

    @property
    @pulumi.getter(name="automaticRepairsPolicy")
    def automatic_repairs_policy(self) -> Optional['outputs.AutomaticRepairsPolicyResponse']:
        """
        Policy for automatic repairs.
        """
        return pulumi.get(self, "automatic_repairs_policy")

    @property
    @pulumi.getter(name="doNotRunExtensionsOnOverprovisionedVMs")
    def do_not_run_extensions_on_overprovisioned_vms(self) -> Optional[bool]:
        """
        When Overprovision is enabled, extensions are launched only on the requested number of VMs which are finally kept. This property will hence ensure that the extensions do not run on the extra overprovisioned VMs.
        """
        return pulumi.get(self, "do_not_run_extensions_on_overprovisioned_vms")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional['outputs.ExtendedLocationResponse']:
        """
        The extended location of the Virtual Machine Scale Set.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter(name="hostGroup")
    def host_group(self) -> Optional['outputs.SubResourceResponse']:
        """
        Specifies information about the dedicated host group that the virtual machine scale set resides in. <br><br>Minimum api-version: 2020-06-01.
        """
        return pulumi.get(self, "host_group")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.VirtualMachineScaleSetIdentityResponse']:
        """
        The identity of the virtual machine scale set, if configured.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="orchestrationMode")
    def orchestration_mode(self) -> Optional[str]:
        """
        Specifies the orchestration mode for the virtual machine scale set.
        """
        return pulumi.get(self, "orchestration_mode")

    @property
    @pulumi.getter
    def overprovision(self) -> Optional[bool]:
        """
        Specifies whether the Virtual Machine Scale Set should be overprovisioned.
        """
        return pulumi.get(self, "overprovision")

    @property
    @pulumi.getter
    def plan(self) -> Optional['outputs.PlanResponse']:
        """
        Specifies information about the marketplace image used to create the virtual machine. This element is only used for marketplace images. Before you can use a marketplace image from an API, you must enable the image for programmatic use.  In the Azure portal, find the marketplace image that you want to use and then click **Want to deploy programmatically, Get Started ->**. Enter any required information and then click **Save**.
        """
        return pulumi.get(self, "plan")

    @property
    @pulumi.getter(name="platformFaultDomainCount")
    def platform_fault_domain_count(self) -> Optional[int]:
        """
        Fault Domain count for each placement group.
        """
        return pulumi.get(self, "platform_fault_domain_count")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state, which only appears in the response.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="proximityPlacementGroup")
    def proximity_placement_group(self) -> Optional['outputs.SubResourceResponse']:
        """
        Specifies information about the proximity placement group that the virtual machine scale set should be assigned to. <br><br>Minimum api-version: 2018-04-01.
        """
        return pulumi.get(self, "proximity_placement_group")

    @property
    @pulumi.getter(name="scaleInPolicy")
    def scale_in_policy(self) -> Optional['outputs.ScaleInPolicyResponse']:
        """
        Specifies the scale-in policy that decides which virtual machines are chosen for removal when a Virtual Machine Scale Set is scaled-in.
        """
        return pulumi.get(self, "scale_in_policy")

    @property
    @pulumi.getter(name="singlePlacementGroup")
    def single_placement_group(self) -> Optional[bool]:
        """
        When true this limits the scale set to a single placement group, of max size 100 virtual machines. NOTE: If singlePlacementGroup is true, it may be modified to false. However, if singlePlacementGroup is false, it may not be modified to true.
        """
        return pulumi.get(self, "single_placement_group")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.SkuResponse']:
        """
        The virtual machine scale set sku.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="spotRestorePolicy")
    def spot_restore_policy(self) -> Optional['outputs.SpotRestorePolicyResponse']:
        """
        Specifies the Spot Restore properties for the virtual machine scale set.
        """
        return pulumi.get(self, "spot_restore_policy")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="uniqueId")
    def unique_id(self) -> str:
        """
        Specifies the ID which uniquely identifies a Virtual Machine Scale Set.
        """
        return pulumi.get(self, "unique_id")

    @property
    @pulumi.getter(name="upgradePolicy")
    def upgrade_policy(self) -> Optional['outputs.UpgradePolicyResponse']:
        """
        The upgrade policy.
        """
        return pulumi.get(self, "upgrade_policy")

    @property
    @pulumi.getter(name="virtualMachineProfile")
    def virtual_machine_profile(self) -> Optional['outputs.VirtualMachineScaleSetVMProfileResponse']:
        """
        The virtual machine profile.
        """
        return pulumi.get(self, "virtual_machine_profile")

    @property
    @pulumi.getter(name="zoneBalance")
    def zone_balance(self) -> Optional[bool]:
        """
        Whether to force strictly even Virtual Machine distribution cross x-zones in case there is zone outage. zoneBalance property can only be set if the zones property of the scale set contains more than one zone. If there are no zones or only one zone specified, then zoneBalance property should not be set.
        """
        return pulumi.get(self, "zone_balance")

    @property
    @pulumi.getter
    def zones(self) -> Optional[Sequence[str]]:
        """
        The virtual machine scale set zones. NOTE: Availability zones can only be set when you create the scale set
        """
        return pulumi.get(self, "zones")


class AwaitableGetVirtualMachineScaleSetResult(GetVirtualMachineScaleSetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVirtualMachineScaleSetResult(
            additional_capabilities=self.additional_capabilities,
            automatic_repairs_policy=self.automatic_repairs_policy,
            do_not_run_extensions_on_overprovisioned_vms=self.do_not_run_extensions_on_overprovisioned_vms,
            extended_location=self.extended_location,
            host_group=self.host_group,
            id=self.id,
            identity=self.identity,
            location=self.location,
            name=self.name,
            orchestration_mode=self.orchestration_mode,
            overprovision=self.overprovision,
            plan=self.plan,
            platform_fault_domain_count=self.platform_fault_domain_count,
            provisioning_state=self.provisioning_state,
            proximity_placement_group=self.proximity_placement_group,
            scale_in_policy=self.scale_in_policy,
            single_placement_group=self.single_placement_group,
            sku=self.sku,
            spot_restore_policy=self.spot_restore_policy,
            tags=self.tags,
            type=self.type,
            unique_id=self.unique_id,
            upgrade_policy=self.upgrade_policy,
            virtual_machine_profile=self.virtual_machine_profile,
            zone_balance=self.zone_balance,
            zones=self.zones)


def get_virtual_machine_scale_set(expand: Optional[str] = None,
                                  resource_group_name: Optional[str] = None,
                                  vm_scale_set_name: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVirtualMachineScaleSetResult:
    """
    Describes a Virtual Machine Scale Set.


    :param str expand: The expand expression to apply on the operation. 'UserData' retrieves the UserData property of the VM scale set that was provided by the user during the VM scale set Create/Update operation
    :param str resource_group_name: The name of the resource group.
    :param str vm_scale_set_name: The name of the VM scale set.
    """
    __args__ = dict()
    __args__['expand'] = expand
    __args__['resourceGroupName'] = resource_group_name
    __args__['vmScaleSetName'] = vm_scale_set_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:compute/v20210401:getVirtualMachineScaleSet', __args__, opts=opts, typ=GetVirtualMachineScaleSetResult).value

    return AwaitableGetVirtualMachineScaleSetResult(
        additional_capabilities=__ret__.additional_capabilities,
        automatic_repairs_policy=__ret__.automatic_repairs_policy,
        do_not_run_extensions_on_overprovisioned_vms=__ret__.do_not_run_extensions_on_overprovisioned_vms,
        extended_location=__ret__.extended_location,
        host_group=__ret__.host_group,
        id=__ret__.id,
        identity=__ret__.identity,
        location=__ret__.location,
        name=__ret__.name,
        orchestration_mode=__ret__.orchestration_mode,
        overprovision=__ret__.overprovision,
        plan=__ret__.plan,
        platform_fault_domain_count=__ret__.platform_fault_domain_count,
        provisioning_state=__ret__.provisioning_state,
        proximity_placement_group=__ret__.proximity_placement_group,
        scale_in_policy=__ret__.scale_in_policy,
        single_placement_group=__ret__.single_placement_group,
        sku=__ret__.sku,
        spot_restore_policy=__ret__.spot_restore_policy,
        tags=__ret__.tags,
        type=__ret__.type,
        unique_id=__ret__.unique_id,
        upgrade_policy=__ret__.upgrade_policy,
        virtual_machine_profile=__ret__.virtual_machine_profile,
        zone_balance=__ret__.zone_balance,
        zones=__ret__.zones)


@_utilities.lift_output_func(get_virtual_machine_scale_set)
def get_virtual_machine_scale_set_output(expand: Optional[pulumi.Input[Optional[str]]] = None,
                                         resource_group_name: Optional[pulumi.Input[str]] = None,
                                         vm_scale_set_name: Optional[pulumi.Input[str]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVirtualMachineScaleSetResult]:
    """
    Describes a Virtual Machine Scale Set.


    :param str expand: The expand expression to apply on the operation. 'UserData' retrieves the UserData property of the VM scale set that was provided by the user during the VM scale set Create/Update operation
    :param str resource_group_name: The name of the resource group.
    :param str vm_scale_set_name: The name of the VM scale set.
    """
    ...
