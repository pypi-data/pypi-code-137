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
    'GetContentKeyPolicyResult',
    'AwaitableGetContentKeyPolicyResult',
    'get_content_key_policy',
    'get_content_key_policy_output',
]

@pulumi.output_type
class GetContentKeyPolicyResult:
    """
    A Content Key Policy resource.
    """
    def __init__(__self__, created=None, description=None, id=None, last_modified=None, name=None, options=None, policy_id=None, system_data=None, type=None):
        if created and not isinstance(created, str):
            raise TypeError("Expected argument 'created' to be a str")
        pulumi.set(__self__, "created", created)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if last_modified and not isinstance(last_modified, str):
            raise TypeError("Expected argument 'last_modified' to be a str")
        pulumi.set(__self__, "last_modified", last_modified)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if options and not isinstance(options, list):
            raise TypeError("Expected argument 'options' to be a list")
        pulumi.set(__self__, "options", options)
        if policy_id and not isinstance(policy_id, str):
            raise TypeError("Expected argument 'policy_id' to be a str")
        pulumi.set(__self__, "policy_id", policy_id)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def created(self) -> str:
        """
        The creation date of the Policy
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        A description for the Policy.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> str:
        """
        The last modified date of the Policy
        """
        return pulumi.get(self, "last_modified")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def options(self) -> Sequence['outputs.ContentKeyPolicyOptionResponse']:
        """
        The Key Policy options.
        """
        return pulumi.get(self, "options")

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> str:
        """
        The legacy Policy ID.
        """
        return pulumi.get(self, "policy_id")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system metadata relating to this resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetContentKeyPolicyResult(GetContentKeyPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetContentKeyPolicyResult(
            created=self.created,
            description=self.description,
            id=self.id,
            last_modified=self.last_modified,
            name=self.name,
            options=self.options,
            policy_id=self.policy_id,
            system_data=self.system_data,
            type=self.type)


def get_content_key_policy(account_name: Optional[str] = None,
                           content_key_policy_name: Optional[str] = None,
                           resource_group_name: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetContentKeyPolicyResult:
    """
    A Content Key Policy resource.


    :param str account_name: The Media Services account name.
    :param str content_key_policy_name: The Content Key Policy name.
    :param str resource_group_name: The name of the resource group within the Azure subscription.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['contentKeyPolicyName'] = content_key_policy_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:media/v20220801:getContentKeyPolicy', __args__, opts=opts, typ=GetContentKeyPolicyResult).value

    return AwaitableGetContentKeyPolicyResult(
        created=__ret__.created,
        description=__ret__.description,
        id=__ret__.id,
        last_modified=__ret__.last_modified,
        name=__ret__.name,
        options=__ret__.options,
        policy_id=__ret__.policy_id,
        system_data=__ret__.system_data,
        type=__ret__.type)


@_utilities.lift_output_func(get_content_key_policy)
def get_content_key_policy_output(account_name: Optional[pulumi.Input[str]] = None,
                                  content_key_policy_name: Optional[pulumi.Input[str]] = None,
                                  resource_group_name: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetContentKeyPolicyResult]:
    """
    A Content Key Policy resource.


    :param str account_name: The Media Services account name.
    :param str content_key_policy_name: The Content Key Policy name.
    :param str resource_group_name: The name of the resource group within the Azure subscription.
    """
    ...
