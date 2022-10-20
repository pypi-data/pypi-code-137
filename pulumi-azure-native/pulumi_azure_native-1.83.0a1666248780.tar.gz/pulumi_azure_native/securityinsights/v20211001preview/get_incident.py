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
    'GetIncidentResult',
    'AwaitableGetIncidentResult',
    'get_incident',
    'get_incident_output',
]

@pulumi.output_type
class GetIncidentResult:
    """
    Represents an incident in Azure Security Insights.
    """
    def __init__(__self__, additional_data=None, classification=None, classification_comment=None, classification_reason=None, created_time_utc=None, description=None, etag=None, first_activity_time_utc=None, id=None, incident_number=None, incident_url=None, labels=None, last_activity_time_utc=None, last_modified_time_utc=None, name=None, owner=None, provider_incident_id=None, provider_name=None, related_analytic_rule_ids=None, severity=None, status=None, system_data=None, team_information=None, title=None, type=None):
        if additional_data and not isinstance(additional_data, dict):
            raise TypeError("Expected argument 'additional_data' to be a dict")
        pulumi.set(__self__, "additional_data", additional_data)
        if classification and not isinstance(classification, str):
            raise TypeError("Expected argument 'classification' to be a str")
        pulumi.set(__self__, "classification", classification)
        if classification_comment and not isinstance(classification_comment, str):
            raise TypeError("Expected argument 'classification_comment' to be a str")
        pulumi.set(__self__, "classification_comment", classification_comment)
        if classification_reason and not isinstance(classification_reason, str):
            raise TypeError("Expected argument 'classification_reason' to be a str")
        pulumi.set(__self__, "classification_reason", classification_reason)
        if created_time_utc and not isinstance(created_time_utc, str):
            raise TypeError("Expected argument 'created_time_utc' to be a str")
        pulumi.set(__self__, "created_time_utc", created_time_utc)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if first_activity_time_utc and not isinstance(first_activity_time_utc, str):
            raise TypeError("Expected argument 'first_activity_time_utc' to be a str")
        pulumi.set(__self__, "first_activity_time_utc", first_activity_time_utc)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if incident_number and not isinstance(incident_number, int):
            raise TypeError("Expected argument 'incident_number' to be a int")
        pulumi.set(__self__, "incident_number", incident_number)
        if incident_url and not isinstance(incident_url, str):
            raise TypeError("Expected argument 'incident_url' to be a str")
        pulumi.set(__self__, "incident_url", incident_url)
        if labels and not isinstance(labels, list):
            raise TypeError("Expected argument 'labels' to be a list")
        pulumi.set(__self__, "labels", labels)
        if last_activity_time_utc and not isinstance(last_activity_time_utc, str):
            raise TypeError("Expected argument 'last_activity_time_utc' to be a str")
        pulumi.set(__self__, "last_activity_time_utc", last_activity_time_utc)
        if last_modified_time_utc and not isinstance(last_modified_time_utc, str):
            raise TypeError("Expected argument 'last_modified_time_utc' to be a str")
        pulumi.set(__self__, "last_modified_time_utc", last_modified_time_utc)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if owner and not isinstance(owner, dict):
            raise TypeError("Expected argument 'owner' to be a dict")
        pulumi.set(__self__, "owner", owner)
        if provider_incident_id and not isinstance(provider_incident_id, str):
            raise TypeError("Expected argument 'provider_incident_id' to be a str")
        pulumi.set(__self__, "provider_incident_id", provider_incident_id)
        if provider_name and not isinstance(provider_name, str):
            raise TypeError("Expected argument 'provider_name' to be a str")
        pulumi.set(__self__, "provider_name", provider_name)
        if related_analytic_rule_ids and not isinstance(related_analytic_rule_ids, list):
            raise TypeError("Expected argument 'related_analytic_rule_ids' to be a list")
        pulumi.set(__self__, "related_analytic_rule_ids", related_analytic_rule_ids)
        if severity and not isinstance(severity, str):
            raise TypeError("Expected argument 'severity' to be a str")
        pulumi.set(__self__, "severity", severity)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if team_information and not isinstance(team_information, dict):
            raise TypeError("Expected argument 'team_information' to be a dict")
        pulumi.set(__self__, "team_information", team_information)
        if title and not isinstance(title, str):
            raise TypeError("Expected argument 'title' to be a str")
        pulumi.set(__self__, "title", title)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="additionalData")
    def additional_data(self) -> 'outputs.IncidentAdditionalDataResponse':
        """
        Additional data on the incident
        """
        return pulumi.get(self, "additional_data")

    @property
    @pulumi.getter
    def classification(self) -> Optional[str]:
        """
        The reason the incident was closed
        """
        return pulumi.get(self, "classification")

    @property
    @pulumi.getter(name="classificationComment")
    def classification_comment(self) -> Optional[str]:
        """
        Describes the reason the incident was closed
        """
        return pulumi.get(self, "classification_comment")

    @property
    @pulumi.getter(name="classificationReason")
    def classification_reason(self) -> Optional[str]:
        """
        The classification reason the incident was closed with
        """
        return pulumi.get(self, "classification_reason")

    @property
    @pulumi.getter(name="createdTimeUtc")
    def created_time_utc(self) -> str:
        """
        The time the incident was created
        """
        return pulumi.get(self, "created_time_utc")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the incident
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        Etag of the azure resource
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="firstActivityTimeUtc")
    def first_activity_time_utc(self) -> Optional[str]:
        """
        The time of the first activity in the incident
        """
        return pulumi.get(self, "first_activity_time_utc")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="incidentNumber")
    def incident_number(self) -> int:
        """
        A sequential number
        """
        return pulumi.get(self, "incident_number")

    @property
    @pulumi.getter(name="incidentUrl")
    def incident_url(self) -> str:
        """
        The deep-link url to the incident in Azure portal
        """
        return pulumi.get(self, "incident_url")

    @property
    @pulumi.getter
    def labels(self) -> Optional[Sequence['outputs.IncidentLabelResponse']]:
        """
        List of labels relevant to this incident
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="lastActivityTimeUtc")
    def last_activity_time_utc(self) -> Optional[str]:
        """
        The time of the last activity in the incident
        """
        return pulumi.get(self, "last_activity_time_utc")

    @property
    @pulumi.getter(name="lastModifiedTimeUtc")
    def last_modified_time_utc(self) -> str:
        """
        The last time the incident was updated
        """
        return pulumi.get(self, "last_modified_time_utc")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def owner(self) -> Optional['outputs.IncidentOwnerInfoResponse']:
        """
        Describes a user that the incident is assigned to
        """
        return pulumi.get(self, "owner")

    @property
    @pulumi.getter(name="providerIncidentId")
    def provider_incident_id(self) -> Optional[str]:
        """
        The incident ID assigned by the incident provider
        """
        return pulumi.get(self, "provider_incident_id")

    @property
    @pulumi.getter(name="providerName")
    def provider_name(self) -> Optional[str]:
        """
        The name of the source provider that generated the incident
        """
        return pulumi.get(self, "provider_name")

    @property
    @pulumi.getter(name="relatedAnalyticRuleIds")
    def related_analytic_rule_ids(self) -> Sequence[str]:
        """
        List of resource ids of Analytic rules related to the incident
        """
        return pulumi.get(self, "related_analytic_rule_ids")

    @property
    @pulumi.getter
    def severity(self) -> str:
        """
        The severity of the incident
        """
        return pulumi.get(self, "severity")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the incident
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="teamInformation")
    def team_information(self) -> Optional['outputs.TeamInformationResponse']:
        """
        Describes a team for the incident
        """
        return pulumi.get(self, "team_information")

    @property
    @pulumi.getter
    def title(self) -> str:
        """
        The title of the incident
        """
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetIncidentResult(GetIncidentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIncidentResult(
            additional_data=self.additional_data,
            classification=self.classification,
            classification_comment=self.classification_comment,
            classification_reason=self.classification_reason,
            created_time_utc=self.created_time_utc,
            description=self.description,
            etag=self.etag,
            first_activity_time_utc=self.first_activity_time_utc,
            id=self.id,
            incident_number=self.incident_number,
            incident_url=self.incident_url,
            labels=self.labels,
            last_activity_time_utc=self.last_activity_time_utc,
            last_modified_time_utc=self.last_modified_time_utc,
            name=self.name,
            owner=self.owner,
            provider_incident_id=self.provider_incident_id,
            provider_name=self.provider_name,
            related_analytic_rule_ids=self.related_analytic_rule_ids,
            severity=self.severity,
            status=self.status,
            system_data=self.system_data,
            team_information=self.team_information,
            title=self.title,
            type=self.type)


def get_incident(incident_id: Optional[str] = None,
                 resource_group_name: Optional[str] = None,
                 workspace_name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIncidentResult:
    """
    Represents an incident in Azure Security Insights.


    :param str incident_id: Incident ID
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace.
    """
    __args__ = dict()
    __args__['incidentId'] = incident_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:securityinsights/v20211001preview:getIncident', __args__, opts=opts, typ=GetIncidentResult).value

    return AwaitableGetIncidentResult(
        additional_data=__ret__.additional_data,
        classification=__ret__.classification,
        classification_comment=__ret__.classification_comment,
        classification_reason=__ret__.classification_reason,
        created_time_utc=__ret__.created_time_utc,
        description=__ret__.description,
        etag=__ret__.etag,
        first_activity_time_utc=__ret__.first_activity_time_utc,
        id=__ret__.id,
        incident_number=__ret__.incident_number,
        incident_url=__ret__.incident_url,
        labels=__ret__.labels,
        last_activity_time_utc=__ret__.last_activity_time_utc,
        last_modified_time_utc=__ret__.last_modified_time_utc,
        name=__ret__.name,
        owner=__ret__.owner,
        provider_incident_id=__ret__.provider_incident_id,
        provider_name=__ret__.provider_name,
        related_analytic_rule_ids=__ret__.related_analytic_rule_ids,
        severity=__ret__.severity,
        status=__ret__.status,
        system_data=__ret__.system_data,
        team_information=__ret__.team_information,
        title=__ret__.title,
        type=__ret__.type)


@_utilities.lift_output_func(get_incident)
def get_incident_output(incident_id: Optional[pulumi.Input[str]] = None,
                        resource_group_name: Optional[pulumi.Input[str]] = None,
                        workspace_name: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetIncidentResult]:
    """
    Represents an incident in Azure Security Insights.


    :param str incident_id: Incident ID
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace.
    """
    ...
