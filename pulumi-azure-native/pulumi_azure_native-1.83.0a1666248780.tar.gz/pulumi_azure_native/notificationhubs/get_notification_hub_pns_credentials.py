# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetNotificationHubPnsCredentialsResult',
    'AwaitableGetNotificationHubPnsCredentialsResult',
    'get_notification_hub_pns_credentials',
    'get_notification_hub_pns_credentials_output',
]

@pulumi.output_type
class GetNotificationHubPnsCredentialsResult:
    """
    Description of a NotificationHub PNS Credentials.
    """
    def __init__(__self__, adm_credential=None, apns_credential=None, baidu_credential=None, gcm_credential=None, id=None, location=None, mpns_credential=None, name=None, sku=None, tags=None, type=None, wns_credential=None):
        if adm_credential and not isinstance(adm_credential, dict):
            raise TypeError("Expected argument 'adm_credential' to be a dict")
        pulumi.set(__self__, "adm_credential", adm_credential)
        if apns_credential and not isinstance(apns_credential, dict):
            raise TypeError("Expected argument 'apns_credential' to be a dict")
        pulumi.set(__self__, "apns_credential", apns_credential)
        if baidu_credential and not isinstance(baidu_credential, dict):
            raise TypeError("Expected argument 'baidu_credential' to be a dict")
        pulumi.set(__self__, "baidu_credential", baidu_credential)
        if gcm_credential and not isinstance(gcm_credential, dict):
            raise TypeError("Expected argument 'gcm_credential' to be a dict")
        pulumi.set(__self__, "gcm_credential", gcm_credential)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if mpns_credential and not isinstance(mpns_credential, dict):
            raise TypeError("Expected argument 'mpns_credential' to be a dict")
        pulumi.set(__self__, "mpns_credential", mpns_credential)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if wns_credential and not isinstance(wns_credential, dict):
            raise TypeError("Expected argument 'wns_credential' to be a dict")
        pulumi.set(__self__, "wns_credential", wns_credential)

    @property
    @pulumi.getter(name="admCredential")
    def adm_credential(self) -> Optional['outputs.AdmCredentialResponse']:
        """
        The AdmCredential of the created NotificationHub
        """
        return pulumi.get(self, "adm_credential")

    @property
    @pulumi.getter(name="apnsCredential")
    def apns_credential(self) -> Optional['outputs.ApnsCredentialResponse']:
        """
        The ApnsCredential of the created NotificationHub
        """
        return pulumi.get(self, "apns_credential")

    @property
    @pulumi.getter(name="baiduCredential")
    def baidu_credential(self) -> Optional['outputs.BaiduCredentialResponse']:
        """
        The BaiduCredential of the created NotificationHub
        """
        return pulumi.get(self, "baidu_credential")

    @property
    @pulumi.getter(name="gcmCredential")
    def gcm_credential(self) -> Optional['outputs.GcmCredentialResponse']:
        """
        The GcmCredential of the created NotificationHub
        """
        return pulumi.get(self, "gcm_credential")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="mpnsCredential")
    def mpns_credential(self) -> Optional['outputs.MpnsCredentialResponse']:
        """
        The MpnsCredential of the created NotificationHub
        """
        return pulumi.get(self, "mpns_credential")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.SkuResponse']:
        """
        The sku of the created namespace
        """
        return pulumi.get(self, "sku")

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
    @pulumi.getter(name="wnsCredential")
    def wns_credential(self) -> Optional['outputs.WnsCredentialResponse']:
        """
        The WnsCredential of the created NotificationHub
        """
        return pulumi.get(self, "wns_credential")


class AwaitableGetNotificationHubPnsCredentialsResult(GetNotificationHubPnsCredentialsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNotificationHubPnsCredentialsResult(
            adm_credential=self.adm_credential,
            apns_credential=self.apns_credential,
            baidu_credential=self.baidu_credential,
            gcm_credential=self.gcm_credential,
            id=self.id,
            location=self.location,
            mpns_credential=self.mpns_credential,
            name=self.name,
            sku=self.sku,
            tags=self.tags,
            type=self.type,
            wns_credential=self.wns_credential)


def get_notification_hub_pns_credentials(namespace_name: Optional[str] = None,
                                         notification_hub_name: Optional[str] = None,
                                         resource_group_name: Optional[str] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNotificationHubPnsCredentialsResult:
    """
    Description of a NotificationHub PNS Credentials.
    API Version: 2017-04-01.


    :param str namespace_name: The namespace name.
    :param str notification_hub_name: The notification hub name.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['namespaceName'] = namespace_name
    __args__['notificationHubName'] = notification_hub_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:notificationhubs:getNotificationHubPnsCredentials', __args__, opts=opts, typ=GetNotificationHubPnsCredentialsResult).value

    return AwaitableGetNotificationHubPnsCredentialsResult(
        adm_credential=__ret__.adm_credential,
        apns_credential=__ret__.apns_credential,
        baidu_credential=__ret__.baidu_credential,
        gcm_credential=__ret__.gcm_credential,
        id=__ret__.id,
        location=__ret__.location,
        mpns_credential=__ret__.mpns_credential,
        name=__ret__.name,
        sku=__ret__.sku,
        tags=__ret__.tags,
        type=__ret__.type,
        wns_credential=__ret__.wns_credential)


@_utilities.lift_output_func(get_notification_hub_pns_credentials)
def get_notification_hub_pns_credentials_output(namespace_name: Optional[pulumi.Input[str]] = None,
                                                notification_hub_name: Optional[pulumi.Input[str]] = None,
                                                resource_group_name: Optional[pulumi.Input[str]] = None,
                                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNotificationHubPnsCredentialsResult]:
    """
    Description of a NotificationHub PNS Credentials.
    API Version: 2017-04-01.


    :param str namespace_name: The namespace name.
    :param str notification_hub_name: The notification hub name.
    :param str resource_group_name: The name of the resource group.
    """
    ...
