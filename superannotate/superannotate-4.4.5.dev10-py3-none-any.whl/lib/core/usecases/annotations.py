import asyncio
import concurrent.futures
import copy
import io
import json
import os
import platform
import re
import time
import traceback
from dataclasses import dataclass
from datetime import datetime
from itertools import islice
from pathlib import Path
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import Optional
from typing import Set
from typing import Tuple

import aiofiles
import boto3
import jsonschema.validators
import lib.core as constants
import nest_asyncio
from jsonschema import Draft7Validator
from jsonschema import ValidationError
from lib.core.conditions import Condition
from lib.core.conditions import CONDITION_EQ as EQ
from lib.core.entities import BaseItemEntity
from lib.core.entities import FolderEntity
from lib.core.entities import ImageEntity
from lib.core.entities import ProjectEntity
from lib.core.entities import TeamEntity
from lib.core.exceptions import AppException
from lib.core.reporter import Reporter
from lib.core.response import Response
from lib.core.service_types import UploadAnnotationAuthData
from lib.core.serviceproviders import BaseServiceProvider
from lib.core.types import PriorityScore
from lib.core.usecases.base import BaseReportableUseCase
from lib.core.video_convertor import VideoFrameGenerator
from pydantic import BaseModel
from superannotate.logger import get_default_logger

logger = get_default_logger()

if platform.system().lower() == "windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

BIG_FILE_THRESHOLD = 15 * 1024 * 1024
ANNOTATION_CHUNK_SIZE_MB = 10 * 1024 * 1024
URI_THRESHOLD = 4 * 1024 - 120
nest_asyncio.apply()


@dataclass
class Report:
    failed_annotations: list
    missing_classes: list
    missing_attr_groups: list
    missing_attrs: list


def log_report(
    report: Report,
):
    if report.missing_classes:
        logger.warning(
            "Could not find annotation classes matching existing classes on the platform: "
            f"[{', '.join(report.missing_classes)}]"
        )
    if report.missing_attr_groups:
        logger.warning(
            "Could not find attribute groups matching existing attribute groups on the platform: "
            f"[{', '.join(report.missing_attr_groups)}]"
        )
    if report.missing_attrs:
        logger.warning(
            "Could not find attributes matching existing attributes on the platform: "
            f"[{', '.join(report.missing_attrs)}]"
        )


class ItemToUpload(BaseModel):
    item: BaseItemEntity
    annotation_json: Optional[dict]
    path: Optional[str]
    file: Optional[io.StringIO]
    file_size: Optional[int]
    mask: Optional[io.BytesIO]

    class Config:
        arbitrary_types_allowed = True


def set_annotation_statuses_in_progress(
    service_provider: BaseServiceProvider,
    project: ProjectEntity,
    folder: FolderEntity,
    item_names: List[str],
    chunk_size=500,
) -> bool:
    failed_on_chunk = False
    for i in range(0, len(item_names), chunk_size):
        status_changed = service_provider.items.set_statuses(
            project=project,
            folder=folder,
            item_names=item_names[i : i + chunk_size],  # noqa: E203
            annotation_status=constants.AnnotationStatus.IN_PROGRESS.value,
        )
        if not status_changed:
            failed_on_chunk = True
    return not failed_on_chunk


async def upload_small_annotations(
    project: ProjectEntity,
    folder: FolderEntity,
    queue: asyncio.Queue,
    service_provider: BaseServiceProvider,
    reporter: Reporter,
    report: Report,
    callback: Callable = None,
):
    async def upload(_chunk):
        failed_annotations, missing_classes, missing_attr_groups, missing_attrs = (
            [],
            [],
            [],
            [],
        )
        try:
            response = await service_provider.annotations.upload_small_annotations(
                project=project,
                folder=folder,
                items_name_file_map={i.item.name: i.file for i in chunk},
            )
            if response.ok:
                if response.data.failed_items:  # noqa
                    failed_annotations = response.data.failed_items
                missing_classes = response.data.missing_resources.classes
                missing_attr_groups = response.data.missing_resources.attribute_groups
                missing_attrs = response.data.missing_resources.attributes
            else:
                failed_annotations.extend([i.item.name for i in chunk])
            if callback:
                for i in chunk:
                    callback(i)
        except Exception:
            logger.debug(traceback.format_exc())
            failed_annotations.extend([i.item.name for i in chunk])
        finally:
            report.failed_annotations.extend(failed_annotations)
            report.missing_classes.extend(missing_classes)
            report.missing_attr_groups.extend(missing_attr_groups)
            report.missing_attrs.extend(missing_attrs)
            reporter.update_progress(len(chunk))

    _size = 0
    chunk = []
    while True:
        item_data = await queue.get()
        queue.task_done()
        if not item_data:
            queue.put_nowait(None)
            break
        if (
            _size + item_data.file_size >= ANNOTATION_CHUNK_SIZE_MB
            or sum([len(i.item.name) for i in chunk])
            >= URI_THRESHOLD - (len(chunk) + 1) * 14
        ):
            await upload(chunk)
            chunk = []
            _size = 0
        chunk.append(item_data)
        _size += item_data.file_size
    if chunk:
        await upload(chunk)


async def upload_big_annotations(
    project: ProjectEntity,
    folder: FolderEntity,
    queue: asyncio.Queue,
    service_provider: BaseServiceProvider,
    reporter: Reporter,
    report: Report,
    callback: Callable = None,
):
    async def _upload_big_annotation(item_data: ItemToUpload) -> Tuple[str, bool]:
        try:
            is_uploaded = await service_provider.annotations.upload_big_annotation(
                project=project,
                folder=folder,
                item_id=item_data.item.id,
                data=item_data.file,
                chunk_size=5 * 1024 * 1024,
            )
            if is_uploaded and callback:
                callback(item_data)
            return item_data.item.name, is_uploaded
        except Exception:
            logger.debug(traceback.format_exc())
            report.failed_annotations.append(item_data.item.name)
        finally:
            reporter.update_progress()

    while True:
        item: ItemToUpload = await queue.get()
        queue.task_done()
        if item:
            await _upload_big_annotation(item)
        else:
            queue.put_nowait(None)
            break


class UploadAnnotationsUseCase(BaseReportableUseCase):
    CHUNK_SIZE = 500
    CHUNK_SIZE_MB = 10 * 1024 * 1024
    URI_THRESHOLD = 4 * 1024 - 120

    def __init__(
        self,
        reporter: Reporter,
        project: ProjectEntity,
        folder: FolderEntity,
        annotations: List[dict],
        service_provider: BaseServiceProvider,
        keep_status: bool = False,
    ):
        super().__init__(reporter)
        self._project = project
        self._folder = folder
        self._annotations = annotations
        self._service_provider = service_provider
        self._keep_status = keep_status
        self._report = Report([], [], [], [])

    def validate_project_type(self):
        if self._project.type == constants.ProjectType.PIXEL.value:
            raise ValidationError("Unsupported project type.")

    def _validate_json(self, json_data: dict) -> list:
        use_case = ValidateAnnotationUseCase(
            reporter=self.reporter,
            team_id=self._project.team_id,
            project_type=self._project.type.value,
            annotation=json_data,
            service_provider=self._service_provider,
        )
        return use_case.execute().data

    def list_existing_items(self, item_names: List[str]) -> List[BaseItemEntity]:
        existing_items = []
        for i in range(0, len(item_names), self.CHUNK_SIZE):
            items_to_check = item_names[i : i + self.CHUNK_SIZE]  # noqa: E203
            response = self._service_provider.items.list_by_names(
                project=self._project, folder=self._folder, names=items_to_check
            )
            existing_items.extend(response.data)
        return existing_items

    async def distribute_queues(self, items_to_upload: List[ItemToUpload]):
        data: List[List[ItemToUpload, bool]] = [[i, False] for i in items_to_upload]
        items_count = len(items_to_upload)
        processed_count = 0
        while processed_count < items_count:
            for idx, (item_to_upload, processed) in enumerate(data):
                if not processed:
                    try:
                        item_to_upload.file = io.StringIO()
                        json.dump(item_to_upload.annotation_json, item_to_upload.file)
                        item_to_upload.file.seek(0, os.SEEK_END)
                        item_to_upload.file_size = item_to_upload.file.tell()
                        item_to_upload.file.seek(0)
                        while True:
                            if item_to_upload.file_size > BIG_FILE_THRESHOLD:
                                if self._big_files_queue.qsize() > 32:
                                    await asyncio.sleep(3)
                                    continue
                                self._big_files_queue.put_nowait(item_to_upload)
                                break
                            else:
                                errors = self._validate_json(
                                    item_to_upload.annotation_json
                                )
                                if errors:
                                    self._report.failed_annotations.append(
                                        item_to_upload.annotation_json["metadata"][
                                            "name"
                                        ]
                                    )
                                    continue
                                self._small_files_queue.put_nowait(item_to_upload)
                                break
                    except Exception:
                        logger.debug(traceback.format_exc())
                        self._report.failed_annotations.append(
                            item_to_upload.annotation_json["metadata"]["name"]
                        )
                        self.reporter.update_progress()
                        data[idx][1] = True  # noqa
                        processed_count += 1
                    data[idx][1] = True  # noqa
                    processed_count += 1
        self._big_files_queue.put_nowait(None)
        self._small_files_queue.put_nowait(None)

    async def run_workers(self, items_to_upload: List[ItemToUpload]):
        self._big_files_queue, self._small_files_queue = (
            asyncio.Queue(),
            asyncio.Queue(),
        )
        await asyncio.gather(
            self.distribute_queues(items_to_upload),
            *[
                upload_big_annotations(
                    project=self._project,
                    folder=self._folder,
                    queue=self._big_files_queue,
                    service_provider=self._service_provider,
                    report=self._report,
                    reporter=self.reporter,
                )
                for _ in range(3)
            ],
        )
        await asyncio.gather(
            upload_small_annotations(
                project=self._project,
                folder=self._folder,
                queue=self._small_files_queue,
                service_provider=self._service_provider,
                reporter=self.reporter,
                report=self._report,
            )
        )

    def execute(self):
        if self.is_valid():
            failed, skipped = [], []
            name_annotation_map = {}
            for annotation in self._annotations:
                try:
                    name = annotation["metadata"]["name"]
                    name_annotation_map[name] = annotation
                except KeyError:
                    failed.append(annotation)
            logger.info(
                f"Uploading {len(name_annotation_map)}/{len(self._annotations)} "
                f"annotations to the project {self._project.name}."
            )
            existing_items = self.list_existing_items(list(name_annotation_map.keys()))
            name_item_map = {i.name: i for i in existing_items}
            len_existing, len_provided = len(existing_items), len(name_annotation_map)
            if len_existing < len_provided:
                logger.warning(
                    f"Couldn't find {len_provided - len_existing}/{len_provided} "
                    "items in the given directory that match the annotations."
                )
            items_to_upload: List[ItemToUpload] = []
            for annotation in name_annotation_map.values():
                annotation_name = annotation["metadata"]["name"]
                item = name_item_map.get(annotation_name)
                if item:
                    items_to_upload.append(
                        ItemToUpload(item=item, annotation_json=annotation)
                    )
                else:
                    skipped.append(annotation_name)
            self.reporter.start_progress(
                len(items_to_upload), description="Uploading Annotations"
            )
            try:
                asyncio.run(self.run_workers(items_to_upload))
            except Exception:
                logger.debug(traceback.format_exc())
                self._response.errors = AppException("Can't upload annotations.")
            self.reporter.finish_progress()

            log_report(self._report)
            failed.extend(self._report.failed_annotations)
            uploaded_annotations = list(
                {i.item.name for i in items_to_upload}
                - set(self._report.failed_annotations).union(set(skipped))
            )
            if uploaded_annotations and not self._keep_status:
                statuses_changed = set_annotation_statuses_in_progress(
                    service_provider=self._service_provider,
                    project=self._project,
                    folder=self._folder,
                    item_names=uploaded_annotations,
                )
                if not statuses_changed:
                    self._response.errors = AppException("Failed to change status.")

            self._response.data = {
                "succeeded": uploaded_annotations,
                "failed": failed,
                "skipped": skipped,
            }
            return self._response


class UploadAnnotationsFromFolderUseCase(BaseReportableUseCase):
    MAX_WORKERS = 16
    CHUNK_SIZE = 100
    CHUNK_SIZE_MB = 10 * 1024 * 1024
    STATUS_CHANGE_CHUNK_SIZE = 100
    AUTH_DATA_CHUNK_SIZE = 500
    THREADS_COUNT = 4
    URI_THRESHOLD = 4 * 1024 - 120

    def __init__(
        self,
        reporter: Reporter,
        project: ProjectEntity,
        folder: FolderEntity,
        team: TeamEntity,
        annotation_paths: List[str],
        service_provider: BaseServiceProvider,
        pre_annotation: bool = False,
        client_s3_bucket=None,
        folder_path: str = None,
        keep_status=False,
    ):
        super().__init__(reporter)
        self._project = project
        self._folder = folder
        self._team = team
        self._service_provider = service_provider
        self._annotation_classes = service_provider.annotation_classes.list(
            Condition("project_id", project.id, EQ)
        ).data
        self._annotation_paths = annotation_paths
        self._client_s3_bucket = client_s3_bucket
        self._pre_annotation = pre_annotation
        self._templates = service_provider.list_templates().data
        self._keep_status = keep_status
        self._annotations_to_upload = []
        self._missing_annotations = []
        self.missing_attribute_groups = set()
        self.missing_classes = set()
        self.missing_attributes = set()
        self._folder_path = folder_path
        if "classes/classes.json" in self._annotation_paths:
            self._annotation_paths.remove("classes/classes.json")
        self._annotation_upload_data = None
        self._item_ids = []
        self._s3_bucket = None
        self._big_files_queue = None
        self._small_files_queue = None
        self._report = Report([], [], [], [])

    @staticmethod
    def get_name_path_mappings(annotation_paths):
        name_path_mappings: Dict[str, str] = {}

        for item_path in annotation_paths:
            name_path_mappings[
                UploadAnnotationsFromFolderUseCase.extract_name(Path(item_path).name)
            ] = item_path
        return name_path_mappings

    def _log_report(
        self,
    ):
        if self._report.missing_classes:
            logger.warning(
                "Could not find annotation classes matching existing classes on the platform: "
                f"[{', '.join(self._report.missing_classes)}]"
            )
        if self._report.missing_attr_groups:
            logger.warning(
                "Could not find attribute groups matching existing attribute groups on the platform: "
                f"[{', '.join(self._report.missing_attr_groups)}]"
            )
        if self._report.missing_attrs:
            logger.warning(
                "Could not find attributes matching existing attributes on the platform: "
                f"[{', '.join(self._report.missing_attrs)}]"
            )

        if self.reporter.custom_messages.get("invalid_jsons"):
            logger.warning(
                f"Couldn't validate {len(self.reporter.custom_messages['invalid_jsons'])}/"
                f"{len(self._annotation_paths)} annotations from {self._folder_path}. "
                f"{constants.USE_VALIDATE_MESSAGE}"
            )

    @staticmethod
    def get_annotation_from_s3(bucket, path: str):
        session = boto3.Session().resource("s3")
        file = io.BytesIO()
        s3_object = session.Object(bucket, path)
        s3_object.download_fileobj(file)
        file.seek(0)
        return file

    def prepare_annotation(self, annotation: dict, size) -> dict:
        errors = None
        if size < BIG_FILE_THRESHOLD:
            use_case = ValidateAnnotationUseCase(
                reporter=self.reporter,
                team_id=self._project.team_id,
                project_type=self._project.type.value,
                annotation=annotation,
                service_provider=self._service_provider,
            )
            errors = use_case.execute().data
        if errors:
            raise AppException(errors)

        annotation = UploadAnnotationUseCase.set_defaults(
            self._team.creator_id, annotation, self._project.type
        )
        return annotation

    async def get_annotation(
        self, path: str
    ) -> (Optional[Tuple[io.StringIO]], Optional[io.BytesIO]):
        mask = None
        mask_path = path.replace(
            constants.PIXEL_ANNOTATION_POSTFIX, constants.ANNOTATION_MASK_POSTFIX
        )
        if self._client_s3_bucket:
            content = self.get_annotation_from_s3(self._client_s3_bucket, path).read()
            if self._project.type == constants.ProjectType.PIXEL.value:
                mask = self.get_annotation_from_s3(self._client_s3_bucket, mask_path)
        else:
            async with aiofiles.open(path) as file:
                content = await file.read()
            if self._project.type == constants.ProjectType.PIXEL.value:
                async with aiofiles.open(mask_path, "rb") as mask:
                    mask = await mask.read()
        if not isinstance(content, bytes):
            content = content.encode("utf8")
        file = io.BytesIO(content)
        file.seek(0)
        size = file.getbuffer().nbytes
        annotation = json.load(file)
        annotation = self.prepare_annotation(annotation, size)
        if not annotation:
            self.reporter.store_message("invalid_jsons", path)
            raise AppException("Invalid json")
        return annotation, mask, size

    @staticmethod
    def chunks(data, size: int = 10000):
        it = iter(data)
        for i in range(0, len(data), size):
            yield {k: data[k] for k in islice(it, size)}

    @staticmethod
    def extract_name(value: str):
        return os.path.basename(
            value.replace(constants.PIXEL_ANNOTATION_POSTFIX, "")
            .replace(constants.VECTOR_ANNOTATION_POSTFIX, "")
            .replace(constants.ATTACHED_VIDEO_ANNOTATION_POSTFIX, ""),
        )

    def get_existing_name_item_mapping(
        self, name_path_mappings: Dict[str, str]
    ) -> dict:
        item_names = list(name_path_mappings.keys())
        existing_name_item_mapping = {}
        for i in range(0, len(item_names), self.CHUNK_SIZE):
            items_to_check = item_names[i : i + self.CHUNK_SIZE]  # noqa: E203
            response = self._service_provider.items.list_by_names(
                project=self._project, folder=self._folder, names=items_to_check
            )
            if response.ok:
                existing_name_item_mapping.update({i.name: i for i in response.data})
        return existing_name_item_mapping

    @property
    def annotation_upload_data(self) -> UploadAnnotationAuthData:
        if not self._annotation_upload_data:
            response = self._service_provider.get_annotation_upload_data(
                project=self._project,
                folder=self._folder,
                item_ids=self._item_ids,
            )
            if response.ok:
                self._annotation_upload_data = response.data
        return self._annotation_upload_data

    @property
    def s3_bucket(self):
        if not self._s3_bucket:
            upload_data = self.annotation_upload_data
            if upload_data:
                session = boto3.Session(
                    aws_access_key_id=upload_data.access_key,
                    aws_secret_access_key=upload_data.secret_key,
                    aws_session_token=upload_data.session_token,
                    region_name=upload_data.region,
                )
                resource = session.resource("s3")
                self._s3_bucket = resource.Bucket(upload_data.bucket)
        return self._s3_bucket

    def _upload_mask(self, item_data: ItemToUpload):
        if self._project.type == constants.ProjectType.PIXEL.value:
            self.s3_bucket.put_object(
                Key=self.annotation_upload_data.images[item_data.item.id][
                    "annotation_bluemap_path"
                ],
                Body=item_data.mask,
            )

    async def distribute_queues(self, items_to_upload: List[ItemToUpload]):
        data: List[List[Any, bool]] = [[i, False] for i in items_to_upload]
        processed_count = 0
        while processed_count < len(data):
            for idx, (item_to_upload, processed) in enumerate(data):
                if not processed:
                    try:
                        (
                            annotation,
                            item_to_upload.mask,
                            item_to_upload.file_size,
                        ) = await self.get_annotation(item_to_upload.path)
                        item_to_upload.file = io.StringIO()
                        json.dump(annotation, item_to_upload.file)
                        item_to_upload.file.seek(0)
                        while True:
                            if item_to_upload.file_size > BIG_FILE_THRESHOLD:
                                if self._big_files_queue.qsize() > 32:
                                    await asyncio.sleep(3)
                                    continue
                                self._big_files_queue.put_nowait(item_to_upload)
                                break
                            else:
                                self._small_files_queue.put_nowait(item_to_upload)
                                break
                    except Exception:
                        logger.debug(traceback.format_exc())
                        self._report.failed_annotations.append(item_to_upload.item.name)
                        self.reporter.update_progress()
                        data[idx][1] = True
                        processed_count += 1
                    data[idx][1] = True
                    processed_count += 1
        self._big_files_queue.put_nowait(None)
        self._small_files_queue.put_nowait(None)

    async def run_workers(self, items_to_upload: List[ItemToUpload]):
        self._big_files_queue, self._small_files_queue = (
            asyncio.Queue(),
            asyncio.Queue(),
        )
        await asyncio.gather(
            self.distribute_queues(items_to_upload),
            *[
                upload_big_annotations(
                    project=self._project,
                    folder=self._folder,
                    queue=self._big_files_queue,
                    service_provider=self._service_provider,
                    report=self._report,
                    reporter=self.reporter,
                    callback=self._upload_mask,
                )
                for _ in range(3)
            ],
        )
        await asyncio.gather(
            upload_small_annotations(
                project=self._project,
                folder=self._folder,
                queue=self._small_files_queue,
                service_provider=self._service_provider,
                reporter=self.reporter,
                report=self._report,
                callback=self._upload_mask,
            )
        )

    def execute(self):
        missing_annotations = []
        self.reporter.start_progress(
            len(self._annotation_paths), description="Uploading Annotations"
        )
        name_path_mappings = self.get_name_path_mappings(self._annotation_paths)
        existing_name_item_mapping = self.get_existing_name_item_mapping(
            name_path_mappings
        )
        name_path_mappings_to_upload = {}
        items_to_upload: List[ItemToUpload] = []

        for name, path in name_path_mappings.items():
            try:
                item = existing_name_item_mapping.pop(name)
                name_path_mappings_to_upload[name] = path
                self._item_ids.append(item.id)
                items_to_upload.append(ItemToUpload(item=item, path=path))
            except KeyError:
                missing_annotations.append(name)
        try:
            asyncio.run(self.run_workers(items_to_upload))
        except Exception:
            logger.debug(traceback.format_exc())
            self._response.errors = AppException("Can't upload annotations.")
        self.reporter.finish_progress()
        self._log_report()
        uploaded_annotations = list(
            name_path_mappings.keys()
            - set(self._report.failed_annotations).union(set(missing_annotations))
        )
        if uploaded_annotations and not self._keep_status:
            statuses_changed = set_annotation_statuses_in_progress(
                service_provider=self._service_provider,
                project=self._project,
                folder=self._folder,
                item_names=uploaded_annotations,
            )
            if not statuses_changed:
                self._response.errors = AppException("Failed to change status.")

        if missing_annotations:
            logger.warning(
                f"Couldn't find {len(missing_annotations)}/{len(name_path_mappings.keys())} "
                "items on the platform that match the annotations you want to upload."
            )
        if self._report.failed_annotations:
            self.reporter.log_warning(
                f"Couldn't validate annotations. {constants.USE_VALIDATE_MESSAGE}"
            )

        self._response.data = (
            uploaded_annotations,
            self._report.failed_annotations,
            missing_annotations,
        )
        return self._response


class UploadAnnotationUseCase(BaseReportableUseCase):
    def __init__(
        self,
        project: ProjectEntity,
        folder: FolderEntity,
        image: ImageEntity,
        team: TeamEntity,
        service_provider: BaseServiceProvider,
        reporter: Reporter,
        annotation_upload_data: UploadAnnotationAuthData = None,
        annotations: dict = None,
        s3_bucket=None,
        client_s3_bucket=None,
        mask=None,
        verbose: bool = True,
        annotation_path: str = None,
        pass_validation: bool = False,
        keep_status: bool = False,
    ):
        super().__init__(reporter)
        self._project = project
        self._folder = folder
        self._image = image
        self._team = team
        self._service_provider = service_provider
        self._annotation_classes = service_provider.annotation_classes.list(
            Condition("project_id", project.id, EQ)
        ).data
        self._annotation_json = annotations
        self._mask = mask
        self._keep_status = keep_status
        self._verbose = verbose
        self._templates = service_provider.list_templates().data
        self._annotation_path = annotation_path
        self._annotation_upload_data = annotation_upload_data
        self._s3_bucket = s3_bucket
        self._client_s3_bucket = client_s3_bucket
        self._pass_validation = pass_validation

    @property
    def annotation_upload_data(self) -> UploadAnnotationAuthData:
        if not self._annotation_upload_data:
            response = self._service_provider.get_annotation_upload_data(
                project=self._project,
                folder=self._folder,
                item_ids=[self._image.id],
            )
            if response.ok:
                self._annotation_upload_data = response.data
        return self._annotation_upload_data

    @property
    def s3_bucket(self):
        if not self._s3_bucket:
            upload_data = self.annotation_upload_data
            if upload_data:
                session = boto3.Session(
                    aws_access_key_id=upload_data.access_key,
                    aws_secret_access_key=upload_data.secret_key,
                    aws_session_token=upload_data.session_token,
                    region_name=upload_data.region,
                )
                resource = session.resource("s3")
                self._s3_bucket = resource.Bucket(upload_data.bucket)
        return self._s3_bucket

    def get_s3_file(self, s3, path: str):
        file = io.BytesIO()
        s3_object = s3.Object(self._client_s3_bucket, path)
        s3_object.download_fileobj(file)
        file.seek(0)
        return file

    @property
    def from_s3(self):
        if self._client_s3_bucket:
            from_session = boto3.Session()
            return from_session.resource("s3")

    def _get_annotation_json(self) -> tuple:
        annotation_json, mask = None, None
        if not self._annotation_json:
            if self._client_s3_bucket:
                annotation_json = json.load(
                    self.get_s3_file(self.from_s3, self._annotation_path)
                )
                if self._project.type == constants.ProjectType.PIXEL.value:
                    self._mask = self.get_s3_file(
                        self.from_s3,
                        self._annotation_path.replace(
                            constants.PIXEL_ANNOTATION_POSTFIX,
                            constants.ANNOTATION_MASK_POSTFIX,
                        ),
                    )
            else:
                annotation_json = json.load(open(self._annotation_path))
                if self._project.type == constants.ProjectType.PIXEL.value:
                    mask = open(
                        self._annotation_path.replace(
                            constants.PIXEL_ANNOTATION_POSTFIX,
                            constants.ANNOTATION_MASK_POSTFIX,
                        ),
                        "rb",
                    )
        else:
            return self._annotation_json, self._mask
        return annotation_json, mask

    def _validate_json(self, json_data: dict) -> list:
        use_case = ValidateAnnotationUseCase(
            reporter=self.reporter,
            team_id=self._project.team_id,
            project_type=self._project.type.value,
            annotation=json_data,
            service_provider=self._service_provider,
        )
        return use_case.execute().data

    @staticmethod
    def set_defaults(team_id, annotation_data: dict, project_type: int):
        default_data = {}
        annotation_data["metadata"]["lastAction"] = {
            "email": team_id,
            "timestamp": int(round(time.time() * 1000)),
        }
        instances = annotation_data.get("instances", [])
        if project_type in constants.ProjectType.images:
            default_data["probability"] = 100

        if project_type == constants.ProjectType.VIDEO.value:
            for instance in instances:
                instance["meta"] = {
                    **default_data,
                    **instance["meta"],
                    "creationType": "Preannotation",  # noqa
                }
        else:
            for idx, instance in enumerate(instances):
                instances[idx] = {
                    **default_data,
                    **instance,
                    "creationType": "Preannotation",  # noqa
                }
        return annotation_data

    def execute(self):
        if self.is_valid():
            annotation_json, mask = self._get_annotation_json()
            errors = self._validate_json(annotation_json)
            annotation_json = UploadAnnotationUseCase.set_defaults(
                self._team.creator_id, annotation_json, self._project.type
            )
            if not errors:
                annotation_file = io.StringIO()
                json.dump(annotation_json, annotation_file)
                size = annotation_file.tell()
                annotation_file.seek(0)
                if size > BIG_FILE_THRESHOLD:
                    uploaded = asyncio.run(
                        self._service_provider.annotations.upload_big_annotation(
                            project=self._project,
                            folder=self._folder,
                            item_id=self._image.id,
                            data=annotation_file,
                            chunk_size=5 * 1024 * 1024,
                        )
                    )
                    if not uploaded:
                        self._response.errors = constants.INVALID_JSON_MESSAGE
                else:
                    response = asyncio.run(
                        self._service_provider.annotations.upload_small_annotations(
                            project=self._project,
                            folder=self._folder,
                            items_name_file_map={self._image.name: annotation_file},
                        )
                    )
                    if response.ok:
                        missing_classes = response.data.missing_resources.classes
                        missing_attr_groups = (
                            response.data.missing_resources.attribute_groups
                        )
                        missing_attrs = response.data.missing_resources.attributes
                        for class_name in missing_classes:
                            self.reporter.log_warning(
                                f"Couldn't find class {class_name}."
                            )
                        for attr_group in missing_attr_groups:
                            self.reporter.log_warning(
                                f"Couldn't find annotation group {attr_group}."
                            )
                        for attr in missing_attrs:
                            self.reporter.log_warning(
                                f"Couldn't find attribute {attr}."
                            )

                        if (
                            self._project.type == constants.ProjectType.PIXEL.value
                            and mask
                        ):
                            self.s3_bucket.put_object(
                                Key=self.annotation_upload_data.images[self._image.id][
                                    "annotation_bluemap_path"
                                ],
                                Body=mask,
                            )
                    if not self._keep_status:
                        statuses_changed = set_annotation_statuses_in_progress(
                            service_provider=self._service_provider,
                            project=self._project,
                            folder=self._folder,
                            item_names=[self._image.name],
                        )
                        if not statuses_changed:
                            self._response.errors = AppException(
                                "Failed to change status."
                            )
                    if self._verbose:
                        self.reporter.log_info(
                            f"Uploading annotations for image {str(self._image.name)} in project {self._project.name}."
                        )
            else:
                self._response.errors = constants.INVALID_JSON_MESSAGE
                self.reporter.store_message("invalid_jsons", self._annotation_path)
                self.reporter.log_warning(
                    f"Couldn't validate annotations. {constants.USE_VALIDATE_MESSAGE}"
                )
        return self._response


class GetAnnotations(BaseReportableUseCase):
    def __init__(
        self,
        reporter: Reporter,
        project: ProjectEntity,
        folder: FolderEntity,
        item_names: Optional[List[str]],
        service_provider: BaseServiceProvider,
        show_process: bool = True,
    ):
        super().__init__(reporter)
        self._project = project
        self._folder = folder
        self._service_provider = service_provider
        self._item_names = item_names
        self._show_process = show_process
        self._item_names_provided = True
        self._big_annotations_queue = None

    def validate_project_type(self):
        if self._project.type == constants.ProjectType.PIXEL.value:
            raise AppException("The function is not supported for Pixel projects.")

    def validate_item_names(self):
        if self._item_names:
            item_names = list(dict.fromkeys(self._item_names))
            len_unique_items, len_items = len(item_names), len(self._item_names)
            if len_unique_items < len_items:
                self.reporter.log_info(
                    f"Dropping duplicates. Found {len_unique_items}/{len_items} unique items."
                )
                self._item_names = item_names
        elif self._item_names is None:
            self._item_names_provided = False
            condition = Condition("project_id", self._project.id, EQ) & Condition(
                "folder_id", self._folder.id, EQ
            )

            self._item_names = [
                item.name for item in self._service_provider.items.list(condition).data
            ]
        else:
            self._item_names = []

    def _prettify_annotations(self, annotations: List[dict]):
        re_struct = {}

        if self._item_names_provided:
            for annotation in annotations:
                re_struct[annotation["metadata"]["name"]] = annotation
            try:
                return [re_struct[x] for x in self._item_names if x in re_struct]
            except KeyError:
                raise AppException("Broken data.")

        return annotations

    async def get_big_annotation(self):

        large_annotations = []
        while True:
            item = await self._big_annotations_queue.get()
            if not item:
                await self._big_annotations_queue.put(None)
                break
            large_annotation = (
                await self._service_provider.annotations.get_big_annotation(
                    project=self._project,
                    item=item,
                    reporter=self.reporter,
                )
            )
            large_annotations.append(large_annotation)
        return large_annotations

    async def get_small_annotations(self, item_names):
        return await self._service_provider.annotations.get_small_annotations(
            project=self._project,
            folder=self._folder,
            items=item_names,
            reporter=self.reporter,
        )

    async def distribute_to_queue(self, big_annotations):
        for item in big_annotations:
            await self._big_annotations_queue.put(item)
        await self._big_annotations_queue.put(None)

    async def run_workers(self, big_annotations, small_annotations):
        self._big_annotations_queue = asyncio.Queue()
        annotations = await asyncio.gather(
            self.distribute_to_queue(big_annotations),
            self.get_small_annotations(small_annotations),
            self.get_big_annotation(),
            self.get_big_annotation(),
            self.get_big_annotation(),
        )

        annotations = [i for x in annotations[1:] for i in x if x]
        return annotations

    def execute(self):
        if self.is_valid():
            items_count = len(self._item_names)
            if not items_count:
                self.reporter.log_info("No annotations to download.")
                self._response.data = []
                return self._response
            self.reporter.log_info(
                f"Getting {items_count} annotations from "
                f"{self._project.name}{f'/{self._folder.name}' if self._folder.name != 'root' else ''}."
            )
            self.reporter.start_progress(items_count, disable=not self._show_process)

            items = self._service_provider.annotations.sort_items_by_size(
                project=self._project, folder=self._folder, item_names=self._item_names
            )
            small_annotations = [x["name"] for x in items["small"]]
            try:
                annotations = asyncio.run(
                    self.run_workers(items["large"], small_annotations)
                )
            except Exception as e:
                self.reporter.log_error(str(e))
                self._response.errors = AppException("Can't get annotations.")
                return self._response
            received_items_count = len(annotations)
            self.reporter.finish_progress()
            if items_count > received_items_count:
                self.reporter.log_warning(
                    f"Could not find annotations for {items_count - received_items_count}/{items_count} items."
                )
            self._response.data = self._prettify_annotations(annotations)
        return self._response


class GetVideoAnnotationsPerFrame(BaseReportableUseCase):
    def __init__(
        self,
        reporter: Reporter,
        project: ProjectEntity,
        folder: FolderEntity,
        video_name: str,
        fps: int,
        service_provider: BaseServiceProvider,
    ):
        super().__init__(reporter)
        self._project = project
        self._folder = folder
        self._video_name = video_name
        self._fps = fps
        self._service_provider = service_provider

    def validate_project_type(self):
        if self._project.type != constants.ProjectType.VIDEO.value:
            raise AppException(
                "The function is not supported for"
                f" {constants.ProjectType.get_name(self._project.type)} projects."
            )

    def execute(self):
        if self.is_valid():
            self.reporter.disable_info()
            response = GetAnnotations(
                reporter=self.reporter,
                project=self._project,
                folder=self._folder,
                item_names=[self._video_name],
                service_provider=self._service_provider,
                show_process=False,
            ).execute()
            self.reporter.enable_info()
            if response.data:
                generator = VideoFrameGenerator(response.data[0], fps=self._fps)
                self.reporter.log_info(
                    f"Getting annotations for {generator.frames_count} frames from {self._video_name}."
                )
                if response.errors:
                    self._response.errors = response.errors
                    return self._response
                if not response.data:
                    self._response.errors = AppException(
                        f"Video {self._video_name} not found."
                    )
                annotations = response.data
                if annotations:
                    self._response.data = list(generator)
                else:
                    self._response.data = []
            else:
                self._response.errors = "Couldn't get annotations."
        return self._response


class UploadPriorityScoresUseCase(BaseReportableUseCase):
    CHUNK_SIZE = 100

    def __init__(
        self,
        reporter,
        project: ProjectEntity,
        folder: FolderEntity,
        scores: List[PriorityScore],
        project_folder_name: str,
        service_provider: BaseServiceProvider,
    ):
        super().__init__(reporter)
        self._project = project
        self._folder = folder
        self._scores = scores
        self._service_provider = service_provider
        self._project_folder_name = project_folder_name

    @staticmethod
    def get_clean_priority(priority):
        if len(str(priority)) > 8:
            priority = float(str(priority)[:8])
        if priority > 1000000:
            priority = 1000000
        if priority < 0:
            priority = 0
        if str(float(priority)).split(".")[1:2]:
            if len(str(float(priority)).split(".")[1]) > 5:
                priority = float(
                    str(float(priority)).split(".")[0]
                    + "."
                    + str(float(priority)).split(".")[1][:5]
                )
        return priority

    @property
    def folder_path(self):
        return f"{self._project.name}{f'/{self._folder.name}' if self._folder.name != 'root' else ''}"

    @property
    def uploading_info(self):
        data_len: int = len(self._scores)
        return (
            f"Uploading  priority scores for {data_len} item(s) to {self.folder_path}."
        )

    def execute(self):
        if self.is_valid():
            priorities = []
            initial_scores = []
            for i in self._scores:
                priorities.append(
                    {
                        "name": i.name,
                        "entropy_value": self.get_clean_priority(i.priority),
                    }
                )
                initial_scores.append(i.name)
            uploaded_score_names = []
            self.reporter.log_info(self.uploading_info)
            iterations = range(0, len(priorities), self.CHUNK_SIZE)
            self.reporter.start_progress(iterations, "Uploading priority scores")
            if iterations:
                for i in iterations:
                    priorities_to_upload = priorities[
                        i : i + self.CHUNK_SIZE
                    ]  # noqa: E203
                    res = self._service_provider.projects.upload_priority_scores(
                        project=self._project,
                        folder=self._folder,
                        priorities=priorities_to_upload,
                    )
                    _data = res.data["data"]
                    if not _data:
                        _data = []
                    self.reporter.update_progress(len(priorities_to_upload))
                    uploaded_score_names.extend(list(map(lambda x: x["name"], _data)))
                self.reporter.finish_progress()
                skipped_score_names = list(
                    set(initial_scores) - set(uploaded_score_names)
                )
                self._response.data = (uploaded_score_names, skipped_score_names)
            else:
                self.reporter.warning_messages("Empty scores.")
        return self._response


class DownloadAnnotations(BaseReportableUseCase):
    def __init__(
        self,
        reporter: Reporter,
        project: ProjectEntity,
        folder: FolderEntity,
        destination: str,
        recursive: bool,
        item_names: List[str],
        service_provider: BaseServiceProvider,
        callback: Callable = None,
    ):
        super().__init__(reporter)
        self._project = project
        self._folder = folder
        self._destination = destination
        self._recursive = recursive
        self._item_names = item_names
        self._service_provider = service_provider
        self._callback = callback
        self._big_file_queues = []
        self._small_file_queues = []

    def validate_item_names(self):
        if self._item_names:
            item_names = list(dict.fromkeys(self._item_names))
            len_unique_items, len_items = len(item_names), len(self._item_names)
            if len_unique_items < len_items:
                self.reporter.log_info(
                    f"Dropping duplicates. Found {len_unique_items}/{len_items} unique items."
                )
                self._item_names = item_names

    def validate_destination(self):
        if self._destination:
            destination = str(self._destination)
            if not os.path.exists(destination) or not os.access(
                destination, os.X_OK | os.W_OK
            ):
                raise AppException(
                    f"Local path {destination} is not an existing directory or access denied."
                )

    @property
    def destination(self) -> Path:
        return Path(self._destination if self._destination else "")

    def get_postfix(self):
        if self._project.type == constants.ProjectType.VECTOR:
            return "___objects.json"
        elif self._project.type == constants.ProjectType.PIXEL.value:
            return "___pixel.json"
        return ".json"

    def download_annotation_classes(self, path: str):
        response = self._service_provider.annotation_classes.list(
            Condition("project_id", self._project.id, EQ)
        )
        if response.ok:
            classes_path = Path(path) / "classes"
            classes_path.mkdir(parents=True, exist_ok=True)
            with open(classes_path / "classes.json", "w+") as file:
                json.dump(
                    [
                        i.dict(
                            exclude_unset=True,
                            by_alias=True,
                            exclude={
                                "attribute_groups": {"__all__": {"is_multiselect"}}
                            },
                        )
                        for i in response.data
                    ],
                    file,
                    indent=4,
                )
        else:
            self._response.errors = AppException("Cant download classes.")

    @staticmethod
    def get_items_count(path: str):
        return sum([len(files) for r, d, files in os.walk(path)])

    @staticmethod
    def coroutine_wrapper(coroutine):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        count = loop.run_until_complete(coroutine)
        loop.close()
        return count

    async def download_big_annotations(self, queue_idx, export_path):
        while True:
            cur_queue = self._big_file_queues[queue_idx]
            item = await cur_queue.get()
            cur_queue.task_done()
            if item:
                postfix = self.get_postfix()
                await self._service_provider.annotations.download_big_annotation(
                    project=self._project,
                    item=item,
                    download_path=f"{export_path}{'/' + self._folder.name if not self._folder.is_root else ''}",
                    postfix=postfix,
                    callback=self._callback,
                )
            else:
                cur_queue.put_nowait(None)
                break

    async def download_small_annotations(
        self, queue_idx, export_path, folder: FolderEntity
    ):
        cur_queue = self._small_file_queues[queue_idx]
        items = []
        item = ""
        postfix = self.get_postfix()
        while item is not None:
            item = await cur_queue.get()
            if item:
                items.append(item)
        await self._service_provider.annotations.download_small_annotations(
            project=self._project,
            folder=folder,
            items=items,
            reporter=self.reporter,
            download_path=f"{export_path}{'/' + self._folder.name if not self._folder.is_root else ''}",
            postfix=postfix,
            callback=self._callback,
        )

    async def distribute_to_queues(
        self, item_names, sm_queue_id, l_queue_id, folder: FolderEntity
    ):
        try:
            resp = self._service_provider.annotations.sort_items_by_size(
                project=self._project, folder=folder, item_names=item_names
            )

            for item in resp["large"]:
                await self._big_file_queues[l_queue_id].put(item)

            for item in resp["small"]:
                await self._small_file_queues[sm_queue_id].put(item["name"])
        finally:
            await self._big_file_queues[l_queue_id].put(None)
            await self._small_file_queues[sm_queue_id].put(None)

    async def run_workers(self, item_names, folder: FolderEntity, export_path):
        try:
            self._big_file_queues.append(asyncio.Queue())
            self._small_file_queues.append(asyncio.Queue())
            small_file_queue_idx = len(self._small_file_queues) - 1
            big_file_queue_idx = len(self._big_file_queues) - 1
            res = await asyncio.gather(
                self.distribute_to_queues(
                    item_names, small_file_queue_idx, big_file_queue_idx, folder
                ),
                self.download_big_annotations(big_file_queue_idx, export_path),
                self.download_big_annotations(big_file_queue_idx, export_path),
                self.download_big_annotations(big_file_queue_idx, export_path),
                self.download_small_annotations(
                    small_file_queue_idx, export_path, folder
                ),
                return_exceptions=True,
            )
            if any(res):
                self.reporter.log_error(f"Error {str([i for i in res if i])}")
        except Exception as e:
            self.reporter.log_error(f"Error {str(e)}")

    def execute(self):
        if self.is_valid():
            export_path = str(
                self.destination
                / Path(
                    f"{self._project.name} {datetime.now().strftime('%B %d %Y %H_%M')}"
                )
            )
            self.reporter.log_info(
                f"Downloading the annotations of the requested items to {export_path}\nThis might take a while…"
            )
            self.reporter.start_spinner()

            folders = []
            if self._folder.is_root and self._recursive:
                folders = self._service_provider.folders.list(
                    Condition("project_id", self._project.id, EQ)
                ).data
            if not folders:
                folders.append(self._folder)
            with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
                futures = []
                for folder in folders:
                    if not self._item_names:
                        condition = Condition(
                            "project_id", self._project.id, EQ
                        ) & Condition("folder_id", folder.id, EQ)
                        item_names = [
                            item.name
                            for item in self._service_provider.items.list(
                                condition
                            ).data
                        ]
                    else:
                        item_names = self._item_names
                    new_export_path = export_path
                    if not folder.is_root and self._folder.is_root:
                        new_export_path += f"/{folder.name}"
                    if not item_names:
                        continue
                    futures.append(
                        executor.submit(
                            asyncio.run,
                            self.run_workers(item_names, folder, new_export_path),
                        )
                    )

            for future in concurrent.futures.as_completed(futures):
                exception = future.exception()
                if exception:
                    self._response.errors = exception

            self.reporter.stop_spinner()
            count = self.get_items_count(export_path)
            self.reporter.log_info(f"Downloaded annotations for {count} items.")
            self.download_annotation_classes(export_path)
            self._response.data = os.path.abspath(export_path)
        return self._response


class ValidateAnnotationUseCase(BaseReportableUseCase):
    DEFAULT_VERSION = "V1.00"
    SCHEMAS: Dict[str, Draft7Validator] = {}
    PATTERN_MAP = {
        "\\d{4}-[01]\\d-[0-3]\\dT[0-2]\\d:[0-5]\\d:[0-5]\\d(?:\\.\\d{3})Z": "does not match YYYY-MM-DDTHH:MM:SS.fffZ",
        "^(?=.{1,254}$)(?=.{1,64}@)[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$": "invalid email",
    }

    def __init__(
        self,
        reporter: Reporter,
        team_id: int,
        project_type: int,
        annotation: dict,
        service_provider: BaseServiceProvider,
    ):
        super().__init__(reporter)
        self._team_id = team_id
        self._project_type = project_type
        self._annotation = annotation
        self._service_provider = service_provider

    @staticmethod
    def _get_const(items, path=()):
        properties = items.get("properties", {})
        _type, _meta = properties.get("type"), properties.get("meta")
        if _meta and _meta.get("type"):
            path = path + ("meta",)
            path, _type = ValidateAnnotationUseCase._get_const(_meta, path)
        if _type and properties.get("type", {}).get("const"):
            path = path + ("type",)
            path, _type = path, properties["type"]["const"]
        return path, _type

    @staticmethod
    def _get_by_path(path: tuple, data: dict):
        tmp = data
        for i in path:
            tmp = tmp.get(i, {})
        return tmp

    @staticmethod
    def oneOf(validator, oneOf, instance, schema):  # noqa
        sub_schemas = enumerate(oneOf)
        const_key = None
        for index, sub_schema in sub_schemas:

            const_key, _type = ValidateAnnotationUseCase._get_const(sub_schema)
            if const_key:
                instance_type = ValidateAnnotationUseCase._get_by_path(
                    const_key, instance
                )
                if not instance_type:
                    yield ValidationError("type required")
                    return
                if const_key and instance_type == _type:
                    errs = list(
                        validator.descend(instance, sub_schema, schema_path=index)
                    )
                    if not errs:
                        return
                    yield ValidationError("invalid instance", context=errs)
                    return
            else:
                subschemas = enumerate(oneOf)
                all_errors = []
                for index, subschema in subschemas:
                    errs = list(
                        validator.descend(instance, subschema, schema_path=index)
                    )
                    if not errs:
                        break
                    all_errors.extend(errs)
                else:
                    yield ValidationError(
                        f"{instance!r} is not valid under any of the given schemas",
                        context=all_errors[:1],
                    )
                # yield from jsonschema._validators.oneOf(  # noqa
                #     validator, oneOf, instance, schema
                # )
        if const_key:
            yield ValidationError(f"invalid {'.'.join(const_key)}")

    @staticmethod
    def _pattern(validator, patrn, instance, schema):
        if validator.is_type(instance, "string") and not re.search(patrn, instance):
            _patrn = ValidateAnnotationUseCase.PATTERN_MAP.get(patrn)
            if _patrn:
                yield ValidationError(f"{instance}  {_patrn}")
            else:
                yield ValidationError(f"{instance} does not match {patrn}")

    @staticmethod
    def iter_errors(self, instance, _schema=None):
        if _schema is None:
            _schema = self.schema
        if _schema is True:
            return
        elif _schema is False:
            yield jsonschema.exceptions.ValidationError(
                f"False schema does not allow {instance!r}",
                validator=None,
                validator_value=None,
                instance=instance,
                schema=_schema,
            )
            return

        scope = jsonschema.validators._id_of(_schema)  # noqa
        _schema = copy.copy(_schema)
        if scope:
            self.resolver.push_scope(scope)
        try:
            validators = []
            if "$ref" in _schema:
                ref = _schema.pop("$ref")
                validators.append(("$ref", ref))

            validators.extend(jsonschema.validators.iteritems(_schema))

            for k, v in validators:
                validator = self.VALIDATORS.get(k)
                if validator is None:
                    continue
                errors = validator(self, v, instance, _schema) or ()
                for error in errors:
                    # set details if not already set by the called fn
                    error._set(
                        validator=k,
                        validator_value=v,
                        instance=instance,
                        schema=_schema,
                    )
                    if k != "$ref":
                        error.schema_path.appendleft(k)
                    yield error
        finally:
            if scope:
                self.resolver.pop_scope()

    @staticmethod
    def extract_path(path):
        path = copy.copy(path)
        real_path = []
        for _ in range(len(path)):
            item = path.popleft()
            if isinstance(item, int):
                real_path.append(f"[{item}]")
            else:
                if real_path and not real_path[-1].endswith("]"):
                    real_path.extend([".", item])
                else:
                    real_path.append(item)
        return real_path

    def _get_validator(self, version: str) -> Draft7Validator:
        key = f"{self._project_type}__{version}"
        validator = ValidateAnnotationUseCase.SCHEMAS.get(key)
        if not validator:
            schema_response = self._service_provider.annotations.get_schema(
                self._project_type, version
            )
            if not schema_response.ok:
                raise AppException(f"Schema {version} does not exist.")
            validator = jsonschema.Draft7Validator(schema_response.data)
            from functools import partial

            iter_errors = partial(self.iter_errors, validator)
            validator.iter_errors = iter_errors
            validator.VALIDATORS["oneOf"] = self.oneOf
            validator.VALIDATORS["pattern"] = self._pattern
            ValidateAnnotationUseCase.SCHEMAS[key] = validator
        return validator

    def extract_messages(self, path, error, report):
        for sub_error in sorted(error.context, key=lambda e: e.schema_path):
            tmp_path = sub_error.path  # if sub_error.path else real_path
            _path = (
                f"{''.join(path)}"
                + ("." if tmp_path else "")
                + "".join(ValidateAnnotationUseCase.extract_path(tmp_path))
            )
            if sub_error.context:
                self.extract_messages(_path, sub_error, report)
            else:
                report.add(
                    (
                        _path,
                        sub_error.message,
                    )
                )

    def execute(self) -> Response:
        try:
            version = self._annotation["version"]
        except KeyError:
            version = self.DEFAULT_VERSION

        extract_path = ValidateAnnotationUseCase.extract_path
        validator = self._get_validator(version)
        errors = sorted(validator.iter_errors(self._annotation), key=lambda e: e.path)
        errors_report: Set[Tuple[str, str]] = set()
        if errors:
            for error in errors:
                if not error:
                    continue
                real_path = extract_path(error.path)
                if not error.context:
                    errors_report.add(("".join(real_path), error.message))
                self.extract_messages(real_path, error, errors_report)

        self._response.data = list(sorted(errors_report, key=lambda x: x[0]))
        return self._response
