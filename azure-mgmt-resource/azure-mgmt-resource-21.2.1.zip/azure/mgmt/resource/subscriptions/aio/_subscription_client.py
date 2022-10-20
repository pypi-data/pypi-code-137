# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin

from .._serialization import Deserializer, Serializer
from ._configuration import SubscriptionClientConfiguration
from ._operations_mixin import SubscriptionClientOperationsMixin

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

class _SDKClient(object):
    def __init__(self, *args, **kwargs):
        """This is a fake class to support current implemetation of MultiApiClientMixin."
        Will be removed in final version of multiapi azure-core based client
        """
        pass

class SubscriptionClient(SubscriptionClientOperationsMixin, MultiApiClientMixin, _SDKClient):
    """All resource groups and resources exist within subscriptions. These operation enable you get information about your subscriptions and tenants. A tenant is a dedicated instance of Azure Active Directory (Azure AD) for your organization.

    This ready contains multiple API versions, to help you deal with all of the Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, it uses the latest API version available on public Azure.
    For production, you should stick to a particular api-version and/or profile.
    The profile sets a mapping between an operation group and its API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param api_version: API version to use if no profile is provided, or if missing in profile.
    :type api_version: str
    :param base_url: Service URL
    :type base_url: str
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    """

    DEFAULT_API_VERSION = '2021-01-01'
    _PROFILE_TAG = "azure.mgmt.resource.subscriptions.SubscriptionClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
            'operations': '2019-11-01',
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        api_version: Optional[str] = None,
        base_url: str = "https://management.azure.com",
        profile: KnownProfiles = KnownProfiles.default,
        **kwargs  # type: Any
    ) -> None:
        self._config = SubscriptionClientConfiguration(credential, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)
        super(SubscriptionClient, self).__init__(
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2016-06-01: :mod:`v2016_06_01.models<azure.mgmt.resource.subscriptions.v2016_06_01.models>`
           * 2018-06-01: :mod:`v2018_06_01.models<azure.mgmt.resource.subscriptions.v2018_06_01.models>`
           * 2019-06-01: :mod:`v2019_06_01.models<azure.mgmt.resource.subscriptions.v2019_06_01.models>`
           * 2019-11-01: :mod:`v2019_11_01.models<azure.mgmt.resource.subscriptions.v2019_11_01.models>`
           * 2021-01-01: :mod:`v2021_01_01.models<azure.mgmt.resource.subscriptions.v2021_01_01.models>`
        """
        if api_version == '2016-06-01':
            from ..v2016_06_01 import models
            return models
        elif api_version == '2018-06-01':
            from ..v2018_06_01 import models
            return models
        elif api_version == '2019-06-01':
            from ..v2019_06_01 import models
            return models
        elif api_version == '2019-11-01':
            from ..v2019_11_01 import models
            return models
        elif api_version == '2021-01-01':
            from ..v2021_01_01 import models
            return models
        raise ValueError("API version {} is not available".format(api_version))

    @property
    def operations(self):
        """Instance depends on the API version:

           * 2016-06-01: :class:`Operations<azure.mgmt.resource.subscriptions.v2016_06_01.aio.operations.Operations>`
           * 2018-06-01: :class:`Operations<azure.mgmt.resource.subscriptions.v2018_06_01.aio.operations.Operations>`
           * 2019-06-01: :class:`Operations<azure.mgmt.resource.subscriptions.v2019_06_01.aio.operations.Operations>`
           * 2019-11-01: :class:`Operations<azure.mgmt.resource.subscriptions.v2019_11_01.aio.operations.Operations>`
        """
        api_version = self._get_api_version('operations')
        if api_version == '2016-06-01':
            from ..v2016_06_01.aio.operations import Operations as OperationClass
        elif api_version == '2018-06-01':
            from ..v2018_06_01.aio.operations import Operations as OperationClass
        elif api_version == '2019-06-01':
            from ..v2019_06_01.aio.operations import Operations as OperationClass
        elif api_version == '2019-11-01':
            from ..v2019_11_01.aio.operations import Operations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'operations'".format(api_version))
        self._config.api_version = api_version
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def subscriptions(self):
        """Instance depends on the API version:

           * 2016-06-01: :class:`SubscriptionsOperations<azure.mgmt.resource.subscriptions.v2016_06_01.aio.operations.SubscriptionsOperations>`
           * 2018-06-01: :class:`SubscriptionsOperations<azure.mgmt.resource.subscriptions.v2018_06_01.aio.operations.SubscriptionsOperations>`
           * 2019-06-01: :class:`SubscriptionsOperations<azure.mgmt.resource.subscriptions.v2019_06_01.aio.operations.SubscriptionsOperations>`
           * 2019-11-01: :class:`SubscriptionsOperations<azure.mgmt.resource.subscriptions.v2019_11_01.aio.operations.SubscriptionsOperations>`
           * 2021-01-01: :class:`SubscriptionsOperations<azure.mgmt.resource.subscriptions.v2021_01_01.aio.operations.SubscriptionsOperations>`
        """
        api_version = self._get_api_version('subscriptions')
        if api_version == '2016-06-01':
            from ..v2016_06_01.aio.operations import SubscriptionsOperations as OperationClass
        elif api_version == '2018-06-01':
            from ..v2018_06_01.aio.operations import SubscriptionsOperations as OperationClass
        elif api_version == '2019-06-01':
            from ..v2019_06_01.aio.operations import SubscriptionsOperations as OperationClass
        elif api_version == '2019-11-01':
            from ..v2019_11_01.aio.operations import SubscriptionsOperations as OperationClass
        elif api_version == '2021-01-01':
            from ..v2021_01_01.aio.operations import SubscriptionsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'subscriptions'".format(api_version))
        self._config.api_version = api_version
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def tenants(self):
        """Instance depends on the API version:

           * 2016-06-01: :class:`TenantsOperations<azure.mgmt.resource.subscriptions.v2016_06_01.aio.operations.TenantsOperations>`
           * 2018-06-01: :class:`TenantsOperations<azure.mgmt.resource.subscriptions.v2018_06_01.aio.operations.TenantsOperations>`
           * 2019-06-01: :class:`TenantsOperations<azure.mgmt.resource.subscriptions.v2019_06_01.aio.operations.TenantsOperations>`
           * 2019-11-01: :class:`TenantsOperations<azure.mgmt.resource.subscriptions.v2019_11_01.aio.operations.TenantsOperations>`
           * 2021-01-01: :class:`TenantsOperations<azure.mgmt.resource.subscriptions.v2021_01_01.aio.operations.TenantsOperations>`
        """
        api_version = self._get_api_version('tenants')
        if api_version == '2016-06-01':
            from ..v2016_06_01.aio.operations import TenantsOperations as OperationClass
        elif api_version == '2018-06-01':
            from ..v2018_06_01.aio.operations import TenantsOperations as OperationClass
        elif api_version == '2019-06-01':
            from ..v2019_06_01.aio.operations import TenantsOperations as OperationClass
        elif api_version == '2019-11-01':
            from ..v2019_11_01.aio.operations import TenantsOperations as OperationClass
        elif api_version == '2021-01-01':
            from ..v2021_01_01.aio.operations import TenantsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'tenants'".format(api_version))
        self._config.api_version = api_version
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    async def close(self):
        await self._client.close()
    async def __aenter__(self):
        await self._client.__aenter__()
        return self
    async def __aexit__(self, *exc_details):
        await self._client.__aexit__(*exc_details)
