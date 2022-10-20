from contextlib import contextmanager, suppress
from io import BytesIO
from pathlib import Path
from typing import ContextManager, Union, overload
from uuid import uuid4

from cloudinary import CloudinaryImage, Config, api, config, uploader

from w.services.abstract_service import AbstractService


class CloudinaryService(AbstractService):
    _is_init = False

    @classmethod
    def init(
        cls,
        cloud_name: str = None,
        api_key: str = None,
        api_secret: str = None,
        **kwargs,
    ) -> None:
        """
        Initialize service with Django settings if possible
        """
        with suppress(ModuleNotFoundError):
            from django.conf import settings

            if not cloud_name:
                cloud_name = getattr(settings, "CLOUDINARY_CLOUD_NAME", None)
            if not api_key:
                api_key = getattr(settings, "CLOUDINARY_API_KEY", None)
            if not api_secret:
                api_secret = getattr(settings, "CLOUDINARY_API_SECRET", None)

        cls.update_configuration(
            cloud_name=cloud_name,
            api_key=api_key,
            api_secret=api_secret,
            **kwargs,
        )
        cls._is_init = True

    @classmethod
    def _is_initialized(cls) -> bool:
        return cls._is_init

    @classmethod
    def clear(cls) -> None:
        super(CloudinaryService, cls).clear()
        cls.update_configuration(cloud_name=None, api_key=None, api_secret=None)
        cls._is_init = False

    @staticmethod
    def update_configuration(**kwargs) -> Config:
        """
        Update global Cloudinary configuration and return it
        """
        return config(**kwargs)

    @staticmethod
    @overload
    def upload(file_bytes: BytesIO, **kwargs) -> None:
        ...

    @staticmethod
    @overload
    def upload(file_path: Union[Path, str], **kwargs) -> None:
        ...

    @classmethod
    def upload(cls, file, **kwargs) -> None:
        cls._check_is_initialized()
        uploader.upload(file, **kwargs)

    @classmethod
    def delete(cls, *public_ids: str, **kwargs) -> None:
        cls._check_is_initialized()
        if not public_ids:
            return

        api.delete_resources(public_ids, **kwargs)

    @classmethod
    def get_image(cls, public_id: str) -> CloudinaryImage:
        cls._check_is_initialized()
        return CloudinaryImage(public_id)

    @classmethod
    def get_image_url(cls, public_id: str, **kwargs) -> str:
        cls._check_is_initialized()
        return cls.get_image(public_id).build_url(**kwargs)

    @classmethod
    @contextmanager
    @overload
    def upload_temporary_file(
        cls, file_bytes: BytesIO, folder: str = None
    ) -> ContextManager[CloudinaryImage]:
        ...

    @classmethod
    @contextmanager
    @overload
    def upload_temporary_file(
        cls, file_path: Union[Path, str], folder: str = None
    ) -> ContextManager[CloudinaryImage]:
        ...

    @classmethod
    @contextmanager
    def upload_temporary_file(
        cls, file, folder: str = None
    ) -> ContextManager[CloudinaryImage]:
        cls._check_is_initialized()
        folder = folder.strip("/ ")
        identifier = str(uuid4())
        public_id = "/".join((folder, identifier))
        cls.upload(file, folder=folder, public_id=identifier)
        yield cls.get_image(public_id)
        cls.delete(public_id)
