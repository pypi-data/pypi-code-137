"""
Copyright 2022 Searis AS

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from datetime import datetime
from pydantic.fields import Optional

from pydantic import BaseModel

from pyclarify.fields.constraints import Annotations, SHA1Hash


class ResourceMetadata(BaseModel):
    """
    Common meta data resources.

    Parameters
    ----------

    annotations: Annotations
        A key-value store where integrations can store programmatic meta-data about the resource instance. Filtering is done one member fields.
    
    attributesHash: string
        A SHA1 hash generated from all attribute fields. The hash is not stored, and can not be queried.
    
    relationshipsHash: string
        A SHA1 hash generated from all relationship fields. The hash is not stored, and can not be queried.

    updatedAt: Date/Time
        A timestamp for when the resource was last updated.
    
    createdAt: Date/Time	
        A timestamp for when the resource was created.    
    """

    annotations: Annotations
    attributesHash: SHA1Hash
    relationshipsHash: SHA1Hash
    updatedAt: datetime
    createdAt: datetime


class BaseResource(BaseModel):
    """
    Base attributes shared by most meta data structures.

    Parameters
    ----------
    id: string 
        A unique ID generated by the server. Queries may be considered invalid if trying to use an invalid ID format according to the target resource type.
    
    type: string
        A string identifying the plural name of the resource type.
    
    meta: ResourceMeta
        An object containing common meta data. (See ResourceMeta for more information)
    """

    id: str
    type: str
    meta: ResourceMetadata


class SelectionMeta(BaseModel):
    total: int
    groupIncludedByType: bool


class RelationshipMetadata(BaseModel):
    type: str
    id: str


class RelationshipData(BaseModel):
    data: Optional[RelationshipMetadata]


class RelationshipsDict(BaseModel):
    integration: RelationshipData
    item: RelationshipData
