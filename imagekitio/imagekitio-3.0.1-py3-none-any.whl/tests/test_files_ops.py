import base64
import json
import os

import responses
from responses import matchers

from imagekitio.client import ImageKit
from imagekitio.constants.url import URL
from imagekitio.exceptions.BadRequestException import BadRequestException
from imagekitio.exceptions.ConflictException import ConflictException
from imagekitio.exceptions.ForbiddenException import ForbiddenException
from imagekitio.exceptions.NotFoundException import NotFoundException
from imagekitio.exceptions.UnknownException import UnknownException
from imagekitio.models.CopyFileRequestOptions import CopyFileRequestOptions
from imagekitio.models.MoveFileRequestOptions import MoveFileRequestOptions
from imagekitio.models.RenameFileRequestOptions import RenameFileRequestOptions
from imagekitio.models.UpdateFileRequestOptions import UpdateFileRequestOptions
from imagekitio.models.UploadFileRequestOptions import UploadFileRequestOptions
from imagekitio.utils.formatter import camel_dict_to_snake_dict
from tests.helpers import (
    ClientTestCase,
    create_headers_for_test,
    get_auth_headers_for_test,
)

imagekit_obj = ImageKit(
    private_key="private_fake:",
    public_key="public_fake123:",
    url_endpoint="fake.com",
)


class TestUpload(ClientTestCase):
    """
    TestUpload class used to test upload method
    """

    image = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "dummy_data/image.png"
    )

    sample_image = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "sample.jpg"
    )
    filename = "test"

    @responses.activate
    def test_upload_fails_on_unauthenticated_request(self):
        """
        Tests if the unauthenticated request restricted
        """
        URL.UPLOAD_BASE_URL = "http://test.com"
        url = "%s%s" % (URL.UPLOAD_BASE_URL, "/api/v1/files/upload")
        try:
            responses.add(
                responses.POST,
                url,
                status=403,
                body="""{"message": "Your account cannot be authenticated."
                                    , "help": "For support kindly contact us at support@imagekit.io ."}""",
            )
            self.client.upload_file(
                file=self.image,
                file_name=self.filename,
                options=UploadFileRequestOptions(
                    use_unique_file_name=False,
                    tags=["abc", "def"],
                    folder="/testing-python-folder/",
                    is_private_file=False,
                    custom_coordinates="10,10,20,20",
                    response_fields=[
                        "tags",
                        "custom_coordinates",
                        "is_private_file",
                        "embedded_metadata",
                        "custom_metadata",
                    ],
                    extensions=(
                        {
                            "name": "remove-bg",
                            "options": {"add_shadow": True, "bg_color": "pink"},
                        },
                        {
                            "name": "google-auto-tagging",
                            "minConfidence": 80,
                            "maxTags": 10,
                        },
                    ),
                    webhook_url="https://webhook.site/c78d617f-33bc-40d9-9e61-608999721e2e",
                    overwrite_file=True,
                    overwrite_ai_tags=False,
                    overwrite_tags=False,
                    overwrite_custom_metadata=True,
                    custom_metadata={"testss": 12},
                ),
            )
            self.assertRaises(ForbiddenException)
        except ForbiddenException as e:
            self.assertEqual(e.message, "Your account cannot be authenticated.")
            self.assertEqual(e.response_metadata.http_status_code, 403)

    @responses.activate
    def test_binary_upload_succeeds(self):
        """
        Tests if  upload succeeds
        """
        URL.UPLOAD_BASE_URL = "http://test.com"
        url = "%s%s" % (URL.UPLOAD_BASE_URL, "/api/v1/files/upload")
        headers = create_headers_for_test()
        responses.add(
            responses.POST,
            url,
            body="""{
                        "fileId": "fake_file_id1234",
                        "name": "file_name.jpg",
                        "size": 102117,
                        "versionInfo": {
                            "id": "62d670648cdb697522602b45",
                            "name": "Version 11"
                        },
                        "filePath": "/testing-python-folder/file_name.jpg",
                        "url": "https://ik.imagekit.io/your_imagekit_id/testing-python-folder/file_name.jpg",
                        "fileType": "image",
                        "height": 700,
                        "width": 1050,
                        "thumbnailUrl": "https://ik.imagekit.io/your_imagekit_id/tr:n-ik_ml_thumbnail/testing-python-folder/file_name.jpg",
                        "tags": [
                            "abc",
                            "def"
                        ],
                        "AITags": [
                            {
                                "name": "Computer",
                                "confidence": 97.66,
                                "source": "google-auto-tagging"
                            },
                            {
                                "name": "Personal computer",
                                "confidence": 94.96,
                                "source": "google-auto-tagging"
                            }
                        ],
                        "isPrivateFile": true,
                        "extensionStatus": {
                            "remove-bg": "pending",
                            "google-auto-tagging": "success"
                        }
                    }""",
            headers=headers,
        )

        with open(self.sample_image, mode="rb") as img:
            imgstr = base64.b64encode(img.read())
        resp = self.client.upload_file(
            file=imgstr,
            file_name="file_name.jpg",
            options=UploadFileRequestOptions(
                use_unique_file_name=False,
                tags=["abc", "def"],
                folder="/testing-python-folder/",
                is_private_file=True,
                response_fields=["is_private_file", "tags"],
                extensions=(
                    {
                        "name": "remove-bg",
                        "options": {"add_shadow": True, "bg_color": "pink"},
                    },
                    {"name": "google-auto-tagging", "minConfidence": 80, "maxTags": 10},
                ),
                webhook_url="url",
                overwrite_file=True,
                overwrite_ai_tags=False,
                overwrite_tags=False,
                overwrite_custom_metadata=True,
                custom_metadata={"test100": 11},
            ),
        )
        mock_response_metadata = {
            "headers": {
                "Content-Type": "text/plain",
                "Accept-Encoding": "gzip, deflate",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
            "http_status_code": 200,
            "raw": {
                "AITags": [
                    {
                        "confidence": 97.66,
                        "name": "Computer",
                        "source": "google-auto-tagging",
                    },
                    {
                        "confidence": 94.96,
                        "name": "Personal computer",
                        "source": "google-auto-tagging",
                    },
                ],
                "extensionStatus": {
                    "google-auto-tagging": "success",
                    "remove-bg": "pending",
                },
                "fileId": "fake_file_id1234",
                "filePath": "/testing-python-folder/file_name.jpg",
                "fileType": "image",
                "height": 700,
                "isPrivateFile": True,
                "name": "file_name.jpg",
                "size": 102117,
                "tags": ["abc", "def"],
                "thumbnailUrl": "https://ik.imagekit.io/your_imagekit_id/tr:n-ik_ml_thumbnail/testing-python-folder/file_name.jpg",
                "url": "https://ik.imagekit.io/your_imagekit_id/testing-python-folder/file_name.jpg",
                "versionInfo": {"id": "62d670648cdb697522602b45", "name": "Version 11"},
                "width": 1050,
            },
        }
        request_body = b'----randomBoundary---------------------\r\nContent-Disposition: form-data; name="file"\r\n\r\n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\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="fileName"\r\n\r\nfile_name.jpg\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="useUniqueFileName"\r\n\r\nfalse\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="tags"\r\n\r\nabc,def\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="folder"\r\n\r\n/testing-python-folder/\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="isPrivateFile"\r\n\r\ntrue\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="responseFields"\r\n\r\nisPrivateFile,tags\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="extensions"\r\n\r\n[{"name": "remove-bg", "options": {"add_shadow": true, "bg_color": "pink"}}, {"name": "google-auto-tagging", "minConfidence": 80, "maxTags": 10}]\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="webhookUrl"\r\n\r\nurl\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="overwriteFile"\r\n\r\ntrue\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="overwriteTags"\r\n\r\nfalse\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="overwriteCustomMetadata"\r\n\r\ntrue\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="customMetadata"\r\n\r\n{"test100": 11}\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="overwriteAITags"\r\n\r\nfalse\r\n----randomBoundary-----------------------\r\n'
        self.assertEqual(request_body, responses.calls[0].request.body)
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual(url, responses.calls[0].request.url)

    @responses.activate
    def test_upload_succeeds_with_url(self):
        """
        Tests if  upload succeeds
        """
        URL.UPLOAD_BASE_URL = "http://test.com"
        url = "%s%s" % (URL.UPLOAD_BASE_URL, "/api/v1/files/upload")
        headers = create_headers_for_test()
        responses.add(
            responses.POST,
            url,
            body="""{
                        "fileId": "fake_file_id1234",
                        "name": "file_name.jpg",
                        "size": 102117,
                        "versionInfo": {
                            "id": "62d670648cdb697522602b45",
                            "name": "Version 11"
                        },
                        "filePath": "/testing-python-folder/file_name.jpg",
                        "url": "https://ik.imagekit.io/your_imagekit_id/testing-python-folder/file_name.jpg",
                        "fileType": "image",
                        "height": 700,
                        "width": 1050,
                        "thumbnailUrl": "https://ik.imagekit.io/your_imagekit_id/tr:n-ik_ml_thumbnail/testing-python-folder/file_name.jpg",
                        "tags": [
                            "abc",
                            "def"
                        ],
                        "AITags": [
                            {
                                "name": "Computer",
                                "confidence": 97.66,
                                "source": "google-auto-tagging"
                            },
                            {
                                "name": "Personal computer",
                                "confidence": 94.96,
                                "source": "google-auto-tagging"
                            }
                        ],
                        "isPrivateFile": true,
                        "extensionStatus": {
                            "remove-bg": "pending",
                            "google-auto-tagging": "success"
                        }
                    }""",
            headers=headers,
        )

        file_upload_url = "https://file-examples.com/wp-content/uploads/2017/10/file_example_JPG_100kB.jpg"
        resp = self.client.upload_file(
            file=file_upload_url,
            file_name="file_name.jpg",
            options=UploadFileRequestOptions(
                use_unique_file_name=False,
                tags=["abc", "def"],
                folder="/testing-python-folder/",
                is_private_file=True,
                response_fields=["is_private_file", "tags"],
                extensions=(
                    {
                        "name": "remove-bg",
                        "options": {"add_shadow": True, "bg_color": "pink"},
                    },
                    {"name": "google-auto-tagging", "minConfidence": 80, "maxTags": 10},
                ),
                webhook_url="url",
                overwrite_file=True,
                overwrite_ai_tags=False,
                overwrite_tags=False,
                overwrite_custom_metadata=True,
                custom_metadata={"test100": 11},
            ),
        )
        mock_response_metadata = {
            "headers": {
                "Content-Type": "text/plain",
                "Accept-Encoding": "gzip, deflate",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
            "http_status_code": 200,
            "raw": {
                "AITags": [
                    {
                        "confidence": 97.66,
                        "name": "Computer",
                        "source": "google-auto-tagging",
                    },
                    {
                        "confidence": 94.96,
                        "name": "Personal computer",
                        "source": "google-auto-tagging",
                    },
                ],
                "extensionStatus": {
                    "google-auto-tagging": "success",
                    "remove-bg": "pending",
                },
                "fileId": "fake_file_id1234",
                "filePath": "/testing-python-folder/file_name.jpg",
                "fileType": "image",
                "height": 700,
                "isPrivateFile": True,
                "name": "file_name.jpg",
                "size": 102117,
                "tags": ["abc", "def"],
                "thumbnailUrl": "https://ik.imagekit.io/your_imagekit_id/tr:n-ik_ml_thumbnail/testing-python-folder/file_name.jpg",
                "url": "https://ik.imagekit.io/your_imagekit_id/testing-python-folder/file_name.jpg",
                "versionInfo": {"id": "62d670648cdb697522602b45", "name": "Version 11"},
                "width": 1050,
            },
        }
        request_body = b'----randomBoundary---------------------\r\nContent-Disposition: form-data; name="file"\r\n\r\nhttps://file-examples.com/wp-content/uploads/2017/10/file_example_JPG_100kB.jpg\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="fileName"\r\n\r\nfile_name.jpg\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="useUniqueFileName"\r\n\r\nfalse\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="tags"\r\n\r\nabc,def\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="folder"\r\n\r\n/testing-python-folder/\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="isPrivateFile"\r\n\r\ntrue\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="responseFields"\r\n\r\nisPrivateFile,tags\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="extensions"\r\n\r\n[{"name": "remove-bg", "options": {"add_shadow": true, "bg_color": "pink"}}, {"name": "google-auto-tagging", "minConfidence": 80, "maxTags": 10}]\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="webhookUrl"\r\n\r\nurl\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="overwriteFile"\r\n\r\ntrue\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="overwriteTags"\r\n\r\nfalse\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="overwriteCustomMetadata"\r\n\r\ntrue\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="customMetadata"\r\n\r\n{"test100": 11}\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="overwriteAITags"\r\n\r\nfalse\r\n----randomBoundary-----------------------\r\n'

        self.assertEqual(request_body, responses.calls[0].request.body)
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual(url, responses.calls[0].request.url)

    def test_upload_fails_without_file_name(self) -> None:
        """Test upload raises error on missing required params"""
        try:
            with open(self.sample_image, mode="rb") as img:
                imgstr = base64.b64encode(img.read())
            self.client.upload_file(file=imgstr)
        except TypeError as e:
            self.assertEqual(
                {"message": "Missing fileName parameter for upload", "help": ""},
                e.args[0],
            )

    def test_upload_fails_without_file(self) -> None:
        """Test upload raises error on missing required params"""
        try:
            self.client.upload_file(file_name="file_name.jpg")
        except TypeError as e:
            self.assertEqual(
                {"message": "Missing file parameter for upload", "help": ""}, e.args[0]
            )

    @responses.activate
    def test_upload_fails_with_400_exception(self) -> None:
        """Test upload raises 400 error"""

        URL.UPLOAD_BASE_URL = "http://test.com"
        url = "%s%s" % (URL.UPLOAD_BASE_URL, "/api/v1/files/upload")
        try:
            responses.add(
                responses.POST,
                url,
                status=400,
                body="""{
                        "message": "A file with the same name already exists at the exact location. We "
                        "could not overwrite it because both overwriteFile and "
                        "useUniqueFileName are set to false."
                    }""",
            )
            self.client.upload_file(
                file=self.image,
                file_name=self.filename,
                options=UploadFileRequestOptions(
                    use_unique_file_name=False,
                    tags=["abc", "def"],
                    folder="/testing-python-folder/",
                    is_private_file=False,
                    custom_coordinates="10,10,20,20",
                    response_fields=[
                        "tags",
                        "custom_coordinates",
                        "is_private_file",
                        "embedded_metadata",
                        "custom_metadata",
                    ],
                    extensions=(
                        {
                            "name": "remove-bg",
                            "options": {"add_shadow": True, "bg_color": "pink"},
                        },
                        {
                            "name": "google-auto-tagging",
                            "minConfidence": 80,
                            "maxTags": 10,
                        },
                    ),
                    webhook_url="https://webhook.site/c78d617f-33bc-40d9-9e61-608999721e2e",
                    overwrite_file=True,
                    overwrite_ai_tags=False,
                    overwrite_tags=False,
                    overwrite_custom_metadata=True,
                    custom_metadata={"testss": 12},
                ),
            )
            self.assertRaises(BadRequestException)
        except BadRequestException as e:
            self.assertEqual(
                "A file with the same name already exists at the exact location. We could not overwrite "
                "it because both overwriteFile and useUniqueFileName are set to false.",
                e.message,
            )
            self.assertEqual(400, e.response_metadata.http_status_code)


class TestListFiles(ClientTestCase):
    """
    TestListFiles class used to test list_files method
    """

    @responses.activate
    def test_list_files_fails_on_unauthenticated_request(self) -> None:
        """Tests unauthenticated request restricted for list_files method"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files".format(URL.API_BASE_URL)
        try:
            responses.add(
                responses.GET,
                url,
                status=403,
                body="""{'message': 'Your account cannot be authenticated.'
                                    , 'help': 'For support kindly contact us at support@imagekit.io .'}""",
            )
            self.client.list_files(self.options)
            self.assertRaises(ForbiddenException)
        except ForbiddenException as e:
            self.assertEqual("Your account cannot be authenticated.", e.message)
            self.assertEqual(403, e.response_metadata.http_status_code)

    @responses.activate
    def test_list_files_succeeds_with_basic_request_tags_with_array(self) -> None:
        """
        Tests if list_files work with options which contains type, sort, path, searchQuery, fileType, limit, skip and tags
        """

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files".format(URL.API_BASE_URL)

        headers = create_headers_for_test()
        responses.add(
            responses.GET,
            url,
            body="""[{
                "type": "file",
                "name": "sample-cat-image_gr64HPlJS.jpg",
                "createdAt": "2022-06-15T08:19:00.843Z",
                "updatedAt": "2022-06-15T08:19:45.169Z",
                "fileId": "62a995f4d875ec08dc587b72",
                "tags": ["Tag_1", " Tag_2", " Tag_3", "tag-to-add-2"],
                "AITags": "",
                "versionInfo": {
                    "id": "62a995f4d875ec08dc587b72",
                    "name": "Version 1"
                },
                "embeddedMetadata": {
                    "XResolution": 250,
                    "YResolution": 250,
                    "DateCreated": "2022-06-15T08:19:01.523Z",
                    "DateTimeCreated": "2022-06-15T08:19:01.524Z"
                },
                "customCoordinates": "10,10,20,20",
                "customMetadata": {
                    "test100": 10
                },
                "isPrivateFile": false,
                "url": "https://ik.imagekit.io/your_imagekit_id/sample-cat-image_gr64HPlJS.jpg",
                "thumbnail": "https://ik.imagekit.io/your_imagekit_id/tr:n-ik_ml_thumbnail/sample-cat-image_gr64HPlJS.jpg",
                "fileType": "image",
                "filePath": "/sample-cat-image_gr64HPlJS.jpg",
                "height": 354,
                "width": 236,
                "size": 23023,
                "hasAlpha": false,
                "mime": "image/jpeg"
            }]""",
            headers=headers,
            match=[
                matchers.query_string_matcher("type=file&sort=ASC_CREATED&path=%2F&searchQuery=created_at+%3E%3D+%272d%27+OR+size+%3C+%272mb%27+OR+format%3D%27png%27&fileType=all&limit=1&skip=0&tags=Tag-1%2C+Tag-2%2C+Tag-3"
                )
            ],
        )

        resp = self.client.list_files(self.opt)

        mock_response_metadata = {
            "headers": {
                "Content-Type": "text/plain",
                "Accept-Encoding": "gzip, deflate",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
            "httpStatusCode": 200,
            "raw": [
                {
                    "AITags": "",
                    "createdAt": "2022-06-15T08:19:00.843Z",
                    "customCoordinates": "10,10,20,20",
                    "customMetadata": {"test100": 10},
                    "embeddedMetadata": {
                        "DateCreated": "2022-06-15T08:19:01.523Z",
                        "DateTimeCreated": "2022-06-15T08:19:01.524Z",
                        "XResolution": 250,
                        "YResolution": 250,
                    },
                    "fileId": "62a995f4d875ec08dc587b72",
                    "filePath": "/sample-cat-image_gr64HPlJS.jpg",
                    "fileType": "image",
                    "hasAlpha": False,
                    "height": 354,
                    "isPrivateFile": False,
                    "mime": "image/jpeg",
                    "name": "sample-cat-image_gr64HPlJS.jpg",
                    "size": 23023,
                    "tags": ["Tag_1", " Tag_2", " Tag_3", "tag-to-add-2"],
                    "thumbnail": "https://ik.imagekit.io/your_imagekit_id/tr:n-ik_ml_thumbnail/sample-cat-image_gr64HPlJS.jpg",
                    "type": "file",
                    "updatedAt": "2022-06-15T08:19:45.169Z",
                    "url": "https://ik.imagekit.io/your_imagekit_id/sample-cat-image_gr64HPlJS.jpg",
                    "versionInfo": {
                        "id": "62a995f4d875ec08dc587b72",
                        "name": "Version " "1",
                    },
                    "width": 236,
                }
            ],
        }
        self.assertEqual(
            "http://test.com/v1/files?type=file&sort=ASC_CREATED&path=%2F&searchQuery=created_at+%3E%3D+%272d%27+OR+size+%3C+%272mb%27+OR+format%3D%27png%27&fileType=all&limit=1&skip=0&tags=Tag-1%2C+Tag-2%2C+Tag-3",
            responses.calls[0].request.url,
        )
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )

    @responses.activate
    def test_list_files_succeeds_with_basic_request(self) -> None:
        """
        Tests if list_files work with options which contains type, sort, path, searchQuery, fileType, limit, skip and tags
        """

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files".format(URL.API_BASE_URL)

        headers = create_headers_for_test()
        responses.add(
            responses.GET,
            url,
            body="""[{
                "type": "file",
                "name": "sample-cat-image_gr64HPlJS.jpg",
                "createdAt": "2022-06-15T08:19:00.843Z",
                "updatedAt": "2022-06-15T08:19:45.169Z",
                "fileId": "62a995f4d875ec08dc587b72",
                "tags": ["Tag_1", " Tag_2", " Tag_3", "tag-to-add-2"],
                "AITags": "",
                "versionInfo": {
                    "id": "62a995f4d875ec08dc587b72",
                    "name": "Version 1"
                },
                "embeddedMetadata": {
                    "XResolution": 250,
                    "YResolution": 250,
                    "DateCreated": "2022-06-15T08:19:01.523Z",
                    "DateTimeCreated": "2022-06-15T08:19:01.524Z"
                },
                "customCoordinates": "10,10,20,20",
                "customMetadata": {
                    "test100": 10
                },
                "isPrivateFile": false,
                "url": "https://ik.imagekit.io/your_imagekit_id/sample-cat-image_gr64HPlJS.jpg",
                "thumbnail": "https://ik.imagekit.io/your_imagekit_id/tr:n-ik_ml_thumbnail/sample-cat-image_gr64HPlJS.jpg",
                "fileType": "image",
                "filePath": "/sample-cat-image_gr64HPlJS.jpg",
                "height": 354,
                "width": 236,
                "size": 23023,
                "hasAlpha": false,
                "mime": "image/jpeg"
            }]""",
            headers=headers,
            match=[
                matchers.query_string_matcher("type=file&sort=ASC_CREATED&path=%2F&searchQuery=created_at+%3E%3D+%272d%27+OR+size+%3C+%272mb%27+OR+format%3D%27png%27&fileType=all&limit=1&skip=0&tags=Tag-1%2C+Tag-2%2C+Tag-3"
                )
            ],
        )

        resp = self.client.list_files(self.options)

        mock_response_metadata = {
            "headers": {
                "Content-Type": "text/plain",
                "Accept-Encoding": "gzip, deflate",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
            "httpStatusCode": 200,
            "raw": [
                {
                    "AITags": "",
                    "createdAt": "2022-06-15T08:19:00.843Z",
                    "customCoordinates": "10,10,20,20",
                    "customMetadata": {"test100": 10},
                    "embeddedMetadata": {
                        "DateCreated": "2022-06-15T08:19:01.523Z",
                        "DateTimeCreated": "2022-06-15T08:19:01.524Z",
                        "XResolution": 250,
                        "YResolution": 250,
                    },
                    "fileId": "62a995f4d875ec08dc587b72",
                    "filePath": "/sample-cat-image_gr64HPlJS.jpg",
                    "fileType": "image",
                    "hasAlpha": False,
                    "height": 354,
                    "isPrivateFile": False,
                    "mime": "image/jpeg",
                    "name": "sample-cat-image_gr64HPlJS.jpg",
                    "size": 23023,
                    "tags": ["Tag_1", " Tag_2", " Tag_3", "tag-to-add-2"],
                    "thumbnail": "https://ik.imagekit.io/your_imagekit_id/tr:n-ik_ml_thumbnail/sample-cat-image_gr64HPlJS.jpg",
                    "type": "file",
                    "updatedAt": "2022-06-15T08:19:45.169Z",
                    "url": "https://ik.imagekit.io/your_imagekit_id/sample-cat-image_gr64HPlJS.jpg",
                    "versionInfo": {
                        "id": "62a995f4d875ec08dc587b72",
                        "name": "Version " "1",
                    },
                    "width": 236,
                }
            ],
        }
        self.assertEqual(
            "http://test.com/v1/files?type=file&sort=ASC_CREATED&path=%2F&searchQuery=created_at+%3E%3D+%272d%27+OR+size+%3C+%272mb%27+OR+format%3D%27png%27&fileType=all&limit=1&skip=0&tags=Tag-1%2C+Tag-2%2C+Tag-3",
            responses.calls[0].request.url,
        )
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )

    @responses.activate
    def test_list_files_fails_with_400_exception(self) -> None:
        """Test get list of files raises 400 error"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files".format(URL.API_BASE_URL)
        try:
            responses.add(
                responses.GET,
                url,
                status=400,
                body="""{"message": "Invalid search query - createdAt field must have a valid date value. Make "
                                            "sure the value is enclosed within quotes. Please refer to the "
                                            "documentation for syntax specification.",
                                 "help": "For support kindly contact us at support@imagekit.io ."}""",
                match=[
                    matchers.query_string_matcher("type=file&sort=ASC_CREATED&path=%2F&searchQuery=created_at+%3E%3D+%272d%27+OR+size+%3C+%272mb%27+OR+format%3D%27png%27&fileType=all&limit=1&skip=0&tags=Tag-1%2C+Tag-2%2C+Tag-3"
                    )
                ],
            )
            self.client.list_files(self.options)
            self.assertRaises(BadRequestException)
        except BadRequestException as e:
            self.assertEqual(
                "Invalid search query - createdAt field must have a valid date value. Make "
                "sure the value is enclosed within quotes. Please refer to the "
                "documentation for syntax specification.",
                e.message,
            )
            self.assertEqual(400, e.response_metadata.http_status_code)


class TestGetFileDetails(ClientTestCase):
    """
    TestGetFileDetails class used to test get_file_details method
    """

    file_id = "fake_file_id1234"
    file_url = "https://example.com/default.jpg"

    @responses.activate
    def test_get_file_details_fails_on_unauthenticated_request(self) -> None:
        """Tests of get_file_details raise error on unauthenticated request"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/details".format(URL.API_BASE_URL, self.file_id)
        try:
            responses.add(
                responses.GET,
                url,
                status=403,
                body="""{'message': 'Your account cannot be authenticated.'
                                    , 'help': 'For support kindly contact us at support@imagekit.io .'}""",
            )
            self.client.get_file_details(self.file_id)
            self.assertRaises(ForbiddenException)
        except ForbiddenException as e:
            self.assertEqual(e.message, "Your account cannot be authenticated.")
            self.assertEqual(403, e.response_metadata.http_status_code)

    @responses.activate
    def test_file_details_succeeds_with_id(self) -> None:
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/details".format(URL.API_BASE_URL, self.file_id)

        headers = create_headers_for_test()
        responses.add(
            responses.GET,
            url,
            body="""{
                        "type": "file",
                        "name": "default-image.jpg",
                        "createdAt": "2022-06-15T08:19:00.843Z",
                        "updatedAt": "2022-08-19T12:19:22.726Z",
                        "fileId": "fake_file_id1234",
                        "tags": [
                            "{Software",
                            " Developer",
                            " Engineer}",
                            "tag-to-add-2"
                        ],
                        "AITags": null,
                        "versionInfo": {
                            "id": "62a995f4d875ec08dc587b72",
                            "name": "Version 1"
                        },
                        "embeddedMetadata": {
                            "XResolution": 250,
                            "YResolution": 250,
                            "DateCreated": "2022-06-15T08:19:01.523Z",
                            "DateTimeCreated": "2022-06-15T08:19:01.524Z"
                        },
                        "customCoordinates": "10,10,20,20",
                        "customMetadata": {
                            "test100": 10
                        },
                        "isPrivateFile": false,
                        "url": "https://ik.imagekit.io/xyxt2lnil/default-image.jpg",
                        "thumbnail": "https://ik.imagekit.io/xyxt2lnil/tr:n-ik_ml_thumbnail/default-image.jpg",
                        "fileType": "image",
                        "filePath": "/default-image.jpg",
                        "height": 354,
                        "width": 236,
                        "size": 23023,
                        "hasAlpha": false,
                        "mime": "image/jpeg"
                    }""",
            headers=headers,
        )
        resp = self.client.get_file_details(self.file_id)

        mock_response_metadata = {
            "headers": {
                "Content-Type": "text/plain",
                "Accept-Encoding": "gzip, deflate",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
            "http_status_code": 200,
            "raw": {
                "AITags": None,
                "createdAt": "2022-06-15T08:19:00.843Z",
                "customCoordinates": "10,10,20,20",
                "customMetadata": {"test100": 10},
                "embeddedMetadata": {
                    "DateCreated": "2022-06-15T08:19:01.523Z",
                    "DateTimeCreated": "2022-06-15T08:19:01.524Z",
                    "XResolution": 250,
                    "YResolution": 250,
                },
                "fileId": "fake_file_id1234",
                "filePath": "/default-image.jpg",
                "fileType": "image",
                "hasAlpha": False,
                "height": 354,
                "isPrivateFile": False,
                "mime": "image/jpeg",
                "name": "default-image.jpg",
                "size": 23023,
                "tags": ["{Software", " Developer", " Engineer}", "tag-to-add-2"],
                "thumbnail": "https://ik.imagekit.io/xyxt2lnil/tr:n-ik_ml_thumbnail/default-image.jpg",
                "type": "file",
                "updatedAt": "2022-08-19T12:19:22.726Z",
                "url": "https://ik.imagekit.io/xyxt2lnil/default-image.jpg",
                "versionInfo": {"id": "62a995f4d875ec08dc587b72", "name": "Version 1"},
                "width": 236,
            },
        }

        self.assertEqual(
            "http://test.com/v1/files/fake_file_id1234/details",
            responses.calls[0].request.url,
        )
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual("fake_file_id1234", resp.file_id)

    @responses.activate
    def test_file_details_fails_with_400_exception(self) -> None:
        """Test get file details raises 400 error"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/details".format(URL.API_BASE_URL, self.file_id)
        try:
            responses.add(
                responses.GET,
                url,
                status=400,
                body="""{"message": "Your request contains invalid fileId parameter.",
                                 "help": "For support kindly contact us at support@imagekit.io ."}""",
            )
            self.client.get_file_details(self.file_id)
            self.assertRaises(BadRequestException)
        except BadRequestException as e:
            self.assertEqual(
                "Your request contains invalid fileId parameter.", e.message
            )
            self.assertEqual(400, e.response_metadata.http_status_code)


class TestDeleteFile(ClientTestCase):
    file_id = "fax_abx1223"
    bulk_delete_ids = ["fake_123", "fake_222"]

    @responses.activate
    def test_bulk_file_delete_fails_on_unauthenticated_request(self) -> None:
        """Test bulk_file_delete on unauthenticated request
        this function checks if raises error on unauthenticated request
        to check if bulk_delete is only restricted to authenticated
        requests
        """

        URL.API_BASE_URL = "http://test.com"
        url = URL.API_BASE_URL + "/v1/files" + URL.BULK_FILE_DELETE
        try:
            responses.add(
                responses.POST,
                url,
                status=403,
                body="""{'message': 'Your account cannot be authenticated.'
                                    , 'help': 'For support kindly contact us at support@imagekit.io .'}""",
            )
            self.client.bulk_file_delete(self.bulk_delete_ids)
            self.assertRaises(ForbiddenException)
        except ForbiddenException as e:
            self.assertEqual(e.message, "Your account cannot be authenticated.")
            self.assertEqual(e.response_metadata.http_status_code, 403)

    @responses.activate
    def test_bulk_file_delete_succeeds(self):
        """Test bulk_delete  on authenticated request
        this function tests if bulk_file_delete working properly
        """

        URL.API_BASE_URL = "http://test.com"
        url = URL.API_BASE_URL + "/v1/files" + URL.BULK_FILE_DELETE
        headers = {"Content-Type": "application/json"}
        headers.update(get_auth_headers_for_test())

        responses.add(
            responses.POST,
            url,
            body='{"successfullyDeletedFileIds": ["fake_123", "fake_222"]}',
            headers=headers,
        )

        resp = self.client.bulk_file_delete(self.bulk_delete_ids)

        mock_response_metadata = {
            "raw": {"successfullyDeletedFileIds": ["fake_123", "fake_222"]},
            "httpStatusCode": 200,
            "headers": {
                "Content-Type": "text/plain, application/json",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
        }
        self.assertEqual(
            '{"fileIds": ["fake_123", "fake_222"]}', responses.calls[0].request.body
        )
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual(["fake_123", "fake_222"], resp.successfully_deleted_file_ids)
        self.assertEqual(
            "http://test.com/v1/files/batch/deleteByFileIds",
            responses.calls[0].request.url,
        )

    @responses.activate
    def test_bulk_file_delete_fails_with_404_exception(self) -> None:
        """Test bulk_file_delete raises 404 error"""

        URL.API_BASE_URL = "http://test.com"
        url = URL.API_BASE_URL + "/v1/files" + URL.BULK_FILE_DELETE
        headers = {"Content-Type": "application/json"}
        headers.update(get_auth_headers_for_test())
        try:
            responses.add(
                responses.POST,
                url,
                status=404,
                body="""{
                    "message": "The requested file(s) does not exist.",
                    "help": "For support kindly contact us at support@imagekit.io .",
                    "missingFileIds": ["fake_123", "fake_222"]
                }""",
                headers=headers,
            )
            self.client.bulk_file_delete(self.bulk_delete_ids)
            self.assertRaises(NotFoundException)
        except NotFoundException as e:
            self.assertEqual("The requested file(s) does not exist.", e.message)
            self.assertEqual(404, e.response_metadata.http_status_code)
            self.assertEqual(
                ["fake_123", "fake_222"], e.response_metadata.raw["missingFileIds"]
            )

    @responses.activate
    def test_file_delete_fails_with_400_exception(self):
        """Test delete_file on unavailable content
        this function raising 400 if the file
        is not available
        """

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}".format(URL.API_BASE_URL, self.file_id)
        headers = {"Content-Type": "application/json"}
        headers.update(get_auth_headers_for_test())
        try:
            responses.add(
                responses.DELETE,
                url,
                status=400,
                body="""{
                    "message": "Your request contains invalid fileId parameter.",
                    "help": "For support kindly contact us at support@imagekit.io ."
                }""",
                headers=headers,
            )
            self.client.delete_file(self.file_id)
            self.assertRaises(BadRequestException)
        except BadRequestException as e:
            self.assertEqual(
                "Your request contains invalid fileId parameter.", e.message
            )
            self.assertEqual(400, e.response_metadata.http_status_code)

    @responses.activate
    def test_file_delete_succeeds(self):
        """Test delete file on authenticated request
        this function tests if delete_file working properly
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}".format(URL.API_BASE_URL, self.file_id)
        headers = {"Content-Type": "application/json"}
        headers.update(get_auth_headers_for_test())

        responses.add(responses.DELETE, url, body="{}", status=204, headers=headers)

        resp = self.client.delete_file(self.file_id)

        mock_response_metadata = {
            "headers": {
                "Content-Type": "text/plain, application/json",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
            "httpStatusCode": 204,
            "raw": None,
        }
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual(
            "http://test.com/v1/files/fax_abx1223", responses.calls[0].request.url
        )


class TestPurgeCache(ClientTestCase):
    fake_image_url = "https://example.com/fakeid/fakeimage.jpg"

    @responses.activate
    def test_purge_file_cache_fails_on_unauthenticated_request(self):
        """
        Tests if the unauthenticated request restricted
        """
        URL.API_BASE_URL = "http://test.com"
        url = URL.API_BASE_URL + "/v1/files/purge"
        try:
            responses.add(
                responses.POST,
                url,
                status=403,
                body="""{'message': 'Your account cannot be authenticated.'
                                    , 'help': 'For support kindly contact us at support@imagekit.io .'}""",
            )
            self.client.purge_file_cache(self.fake_image_url)
            self.assertRaises(ForbiddenException)
        except ForbiddenException as e:
            self.assertEqual(e.message, "Your account cannot be authenticated.")
            self.assertEqual(403, e.response_metadata.http_status_code)

    @responses.activate
    def test_purge_file_cache_fails_with_400(self):
        """
        Tests if the purge_file_cache fails with 400
        """
        URL.API_BASE_URL = "http://test.com"
        url = URL.API_BASE_URL + "/v1/files/purge"
        try:
            responses.add(
                responses.POST,
                url,
                status=400,
                body='{"message": "Invalid url"}',
            )
            self.client.purge_file_cache("url")
            self.assertRaises(BadRequestException)
        except BadRequestException as e:
            self.assertEqual("Invalid url", e.message)
            self.assertEqual(400, e.response_metadata.http_status_code)

    @responses.activate
    def test_purge_file_cache_succeeds(self):
        """
        Tests if purge_file_cache succeeds
        """
        URL.API_BASE_URL = "http://test.com"
        url = URL.API_BASE_URL + "/v1/files/purge"
        responses.add(
            responses.POST,
            url,
            status=201,
            body='{"requestId": "requestId"}',
        )
        resp = self.client.purge_file_cache(self.fake_image_url)
        mock_response_metadata = {
            "raw": {"requestId": "requestId"},
            "httpStatusCode": 201,
            "headers": {"Content-Type": "text/plain"},
        }
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual("requestId", resp.request_id)
        self.assertEqual(
            "http://test.com/v1/files/purge", responses.calls[0].request.url
        )
        self.assertEqual(
            '{"url": "https://example.com/fakeid/fakeimage.jpg"}',
            responses.calls[0].request.body,
        )


class TestPurgeCacheStatus(ClientTestCase):
    cache_request_id = "fake1234"

    @responses.activate
    def test_purge_file_cache_status_fails_with_400(self):
        """
        Tests if the purge_file_cache_status fails with 400
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/purge/{}".format(URL.API_BASE_URL, self.cache_request_id)
        try:
            responses.add(
                responses.GET,
                url,
                status=400,
                body="""{"message": "No request found for this requestId.",
                                 "help": "For support kindly contact us at support@imagekit.io ."}""",
            )
            self.client.get_purge_file_cache_status(self.cache_request_id)
            self.assertRaises(BadRequestException)
        except BadRequestException as e:
            self.assertEqual("No request found for this requestId.", e.message)
            self.assertEqual(400, e.response_metadata.http_status_code)

    @responses.activate
    def test_purge_file_cache_status_succeeds(self):
        """
        Tests if purge_file_cache_status succeeds
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/purge/{}".format(URL.API_BASE_URL, self.cache_request_id)
        responses.add(
            responses.GET,
            url,
            body="""{"status": "Completed"}""",
        )
        resp = self.client.get_purge_file_cache_status(self.cache_request_id)
        mock_response_metadata = {
            "headers": {"Content-Type": "text/plain"},
            "httpStatusCode": 200,
            "raw": {"status": "Completed"},
        }
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual("Completed", resp.status)
        self.assertEqual(
            "http://test.com/v1/files/purge/fake1234", responses.calls[0].request.url
        )


class TestGetMetaData(ClientTestCase):
    file_id = "fake_file_xbc"

    fake_image_url = "https://example.com/fakeid/fakeimage.jpg"

    @responses.activate
    def test_get_file_metadata_fails_with_400(self):
        """
        Tests if the get_file_metadata fails with 400
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/metadata".format(URL.API_BASE_URL, self.file_id)
        try:
            responses.add(
                responses.GET,
                url,
                status=400,
                body="""{"message": "Your request contains invalid fileId parameter.",
                                 "help": "For support kindly contact us at support@imagekit.io .",
                                 "type": "INVALID_PARAM_ERROR"}""",
            )
            self.client.get_file_metadata(self.file_id)
            self.assertRaises(BadRequestException)
        except BadRequestException as e:
            self.assertEqual(
                "Your request contains invalid fileId parameter.", e.message
            )
            self.assertEqual(400, e.response_metadata.http_status_code)
            self.assertEqual("INVALID_PARAM_ERROR", e.response_metadata.raw["type"])

    @responses.activate
    def test_get_file_metadata_succeeds(self):
        """
        Tests if get_file_metadata succeeds
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/metadata".format(URL.API_BASE_URL, self.file_id)
        responses.add(
            responses.GET,
            url,
            body="""{
                "height": 354,
                "width": 236,
                "size": 7390,
                "format": "jpg",
                "hasColorProfile": false,
                "quality": 0,
                "density": 250,
                "hasTransparency": false,
                "exif": {},
                "pHash": "2e0ed1f12eda9525"
            }""",
        )
        resp = self.client.get_file_metadata(self.file_id)
        mock_response_metadata = {
            "headers": {"Content-Type": "text/plain"},
            "httpStatusCode": 200,
            "raw": {
                "density": 250,
                "exif": {},
                "format": "jpg",
                "hasColorProfile": False,
                "hasTransparency": False,
                "height": 354,
                "pHash": "2e0ed1f12eda9525",
                "quality": 0,
                "size": 7390,
                "width": 236,
            },
        }
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual(
            "http://test.com/v1/files/fake_file_xbc/metadata",
            responses.calls[0].request.url,
        )

    @responses.activate
    def test_get_remote_file_url_metadata_fails_with_400(self):
        """
        Tests if the get_remote_file_url_metadata fails with 400
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/metadata".format(URL.API_BASE_URL)
        try:
            responses.add(
                responses.GET,
                url,
                status=400,
                body="""{
                    "message": "https://example.com/fakeid/fakeimage.jpg should be accessible using your ImageKit.io account.",
                    "help": "For support kindly contact us at support@imagekit.io ."
                }""",
                match=[
                    matchers.query_string_matcher(
                        "url=https://example.com/fakeid/fakeimage.jpg"
                    )
                ],
            )
            self.client.get_remote_file_url_metadata(self.fake_image_url)
            self.assertRaises(BadRequestException)
        except BadRequestException as e:
            self.assertEqual(
                "https://example.com/fakeid/fakeimage.jpg should be accessible using your ImageKit.io account.",
                e.message,
            )
            self.assertEqual(400, e.response_metadata.http_status_code)

    @responses.activate
    def test_get_remote_file_url_metadata_succeeds(self):
        """
        Tests if get_remote_file_url_metadata succeeds
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/metadata".format(URL.API_BASE_URL)
        responses.add(
            responses.GET,
            url,
            body="""{
                "height": 354,
                "width": 236,
                "size": 7390,
                "format": "jpg",
                "hasColorProfile": false,
                "quality": 0,
                "density": 250,
                "hasTransparency": false,
                "exif": {},
                "pHash": "2e0ed1f12eda9525"
            }""",
            match=[
                matchers.query_string_matcher(
                    "url=https://example.com/fakeid/fakeimage.jpg"
                )
            ],
        )
        resp = self.client.get_remote_file_url_metadata(self.fake_image_url)
        mock_response_metadata = {
            "headers": {"Content-Type": "text/plain"},
            "httpStatusCode": 200,
            "raw": {
                "density": 250,
                "exif": {},
                "format": "jpg",
                "hasColorProfile": False,
                "hasTransparency": False,
                "height": 354,
                "pHash": "2e0ed1f12eda9525",
                "quality": 0,
                "size": 7390,
                "width": 236,
            },
        }
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual(
            "http://test.com/v1/metadata?url=https%3A%2F%2Fexample.com%2Ffakeid%2Ffakeimage.jpg",
            responses.calls[0].request.url,
        )


class TestUpdateFileDetails(ClientTestCase):
    """
    TestUpdateFileDetails class used to update file details method
    """

    file_id = "fake_123"

    valid_options = UpdateFileRequestOptions(
        tags=["tag1", "tag2"], custom_coordinates="10,10,100,100"
    )

    @responses.activate
    def test_update_file_details_fails_on_unauthenticated_request(self):
        """
        Tests if the unauthenticated request restricted
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/details/".format(URL.API_BASE_URL, self.file_id)
        try:
            responses.add(
                responses.PATCH,
                url,
                status=403,
                body="""{'message': 'Your account cannot be authenticated.'
                                    , 'help': 'For support kindly contact us at support@imagekit.io .'}""",
            )
            self.client.update_file_details(
                file_id=self.file_id, options=self.valid_options
            )
            self.assertRaises(ForbiddenException)
        except ForbiddenException as e:
            self.assertEqual(e.message, "Your account cannot be authenticated.")
            self.assertEqual(403, e.response_metadata.http_status_code)

    @responses.activate
    def test_update_file_details_succeeds_with_id(self):
        """
        Tests if  update file details succeeds with file id
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/details/".format(URL.API_BASE_URL, self.file_id)
        headers = {"Content-Type": "application/json"}
        headers.update(get_auth_headers_for_test())
        responses.add(
            responses.PATCH,
            url,
            body="""{
                    "type": "file",
                    "name": "default-image.jpg",
                    "createdAt": "2022-07-21T10:31:22.529Z",
                    "updatedAt": "2022-07-21T10:37:11.848Z",
                    "fileId": "fake_123",
                    "tags": ["tag1", "tag2"],
                    "AITags": [{
                        "name": "Corridor",
                        "confidence": 99.39,
                        "source": "aws-auto-tagging"
                    }, {
                        "name": "Floor",
                        "confidence": 97.59,
                        "source": "aws-auto-tagging"
                    }],
                    "versionInfo": {
                        "id": "versionId",
                        "name": "Version 2"
                    },
                    "embeddedMetadata": {
                        "XResolution": 1,
                        "YResolution": 1,
                        "DateCreated": "2022-07-21T10:35:34.497Z",
                        "DateTimeCreated": "2022-07-21T10:35:34.500Z"
                    },
                    "customCoordinates": "10,10,100,100",
                    "customMetadata": {
                        "test": 11
                    },
                    "isPrivateFile": false,
                    "url": "https://ik.imagekit.io/your_imagekit_id/default-image.jpg",
                    "thumbnail": "https://ik.imagekit.io/your_imagekit_id/tr:n-ik_ml_thumbnail/default-image.jpg",
                    "fileType": "image",
                    "filePath": "/default-image.jpg",
                    "height": 1000,
                    "width": 1000,
                    "size": 184425,
                    "hasAlpha": false,
                    "mime": "image/jpeg",
                    "extensionStatus": {
                        "remove-bg": "pending",
                        "google-auto-tagging": "success"
                    }
                }""",
            headers=headers,
        )

        request_body = json.dumps(
            json.loads(
                """{
                "removeAITags": ["ai-tag1", "ai-tag2"],
                "webhookUrl": "url",
                "extensions": [{
                    "name": "remove-bg",
                    "options": {
                        "add_shadow": true,
                        "bg_color": "red"
                    }
                }, {
                    "name": "google-auto-tagging",
                    "minConfidence": 80,
                    "maxTags": 10
                }],
                "tags": ["tag1", "tag2"],
                "customCoordinates": "10,10,100,100",
                "customMetadata": {
                    "test": 11
                }
            }"""
            )
        )
        resp = self.client.update_file_details(
            file_id=self.file_id,
            options=UpdateFileRequestOptions(
                remove_ai_tags=["ai-tag1", "ai-tag2"],
                webhook_url="url",
                extensions=[
                    {
                        "name": "remove-bg",
                        "options": {"add_shadow": True, "bg_color": "red"},
                    },
                    {"name": "google-auto-tagging", "minConfidence": 80, "maxTags": 10},
                ],
                tags=["tag1", "tag2"],
                custom_coordinates="10,10,100,100",
                custom_metadata={"test": 11},
            ),
        )
        mock_response_metadata = {
            "headers": {
                "Content-Type": "text/plain, application/json",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
            "http_status_code": 200,
            "raw": {
                "AITags": [
                    {
                        "confidence": 99.39,
                        "name": "Corridor",
                        "source": "aws-auto-tagging",
                    },
                    {
                        "confidence": 97.59,
                        "name": "Floor",
                        "source": "aws-auto-tagging",
                    },
                ],
                "createdAt": "2022-07-21T10:31:22.529Z",
                "customCoordinates": "10,10,100,100",
                "customMetadata": {"test": 11},
                "embeddedMetadata": {
                    "DateCreated": "2022-07-21T10:35:34.497Z",
                    "DateTimeCreated": "2022-07-21T10:35:34.500Z",
                    "XResolution": 1,
                    "YResolution": 1,
                },
                "extensionStatus": {
                    "google-auto-tagging": "success",
                    "remove-bg": "pending",
                },
                "fileId": "fake_123",
                "filePath": "/default-image.jpg",
                "fileType": "image",
                "hasAlpha": False,
                "height": 1000,
                "isPrivateFile": False,
                "mime": "image/jpeg",
                "name": "default-image.jpg",
                "size": 184425,
                "tags": ["tag1", "tag2"],
                "thumbnail": "https://ik.imagekit.io/your_imagekit_id/tr:n-ik_ml_thumbnail/default-image.jpg",
                "type": "file",
                "updatedAt": "2022-07-21T10:37:11.848Z",
                "url": "https://ik.imagekit.io/your_imagekit_id/default-image.jpg",
                "versionInfo": {"id": "versionId", "name": "Version 2"},
                "width": 1000,
            },
        }
        self.assertEqual(request_body, responses.calls[0].request.body)
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual("fake_123", resp.file_id)
        self.assertEqual(
            "http://test.com/v1/files/fake_123/details/", responses.calls[0].request.url
        )

    @responses.activate
    def test_update_file_details_fails_with_404_exception(self) -> None:
        """Test update file details raises 404 error"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/details/".format(URL.API_BASE_URL, self.file_id)
        try:
            responses.add(
                responses.PATCH,
                url,
                status=404,
                body="""{"message": "The requested file does not exist.",
                                 "help": "For support kindly contact us at support@imagekit.io ."}""",
            )
            self.client.update_file_details(
                file_id=self.file_id,
                options=UpdateFileRequestOptions(
                    remove_ai_tags=["ai-tag1", "ai-tag2"],
                    webhook_url="url",
                    extensions=[
                        {
                            "name": "remove-bg",
                            "options": {"add_shadow": True, "bg_color": "red"},
                        },
                        {
                            "name": "google-auto-tagging",
                            "minConfidence": 80,
                            "maxTags": 10,
                        },
                    ],
                    tags=["tag1", "tag2"],
                    custom_coordinates="10,10,100,100",
                    custom_metadata={"test": 11},
                ),
            )
            self.assertRaises(UnknownException)
        except UnknownException as e:
            self.assertEqual("The requested file does not exist.", e.message)
            self.assertEqual(404, e.response_metadata.http_status_code)


class TestGetFileVersions(ClientTestCase):
    """
    TestGetFileVersions class used to get file versions and it's details
    """

    file_id = "fake_123"

    version_id = "fake_version_123"

    valid_options = {"tags": ["tag1", "tag2"], "custom_coordinates": "10,10,100,100"}

    @responses.activate
    def test_get_file_versions_fails_on_unauthenticated_request(self):
        """
        Tests if the unauthenticated request restricted
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/versions".format(URL.API_BASE_URL, self.file_id)
        try:
            responses.add(
                responses.GET,
                url,
                status=403,
                body="""{'message': 'Your account cannot be authenticated.'
                                    , 'help': 'For support kindly contact us at support@imagekit.io .'}""",
            )
            self.client.get_file_versions(self.file_id)
            self.assertRaises(ForbiddenException)
        except ForbiddenException as e:
            self.assertEqual(e.message, "Your account cannot be authenticated.")
            self.assertEqual(403, e.response_metadata.http_status_code)

    @responses.activate
    def test_get_file_versions_succeeds_with_id(self):
        """
        Tests if get file versions succeeds with file id
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/versions".format(URL.API_BASE_URL, self.file_id)

        headers = {"Content-Type": "application/json"}
        headers.update(get_auth_headers_for_test())
        responses.add(
            responses.GET,
            url,
            body="""[{
                "type": "file",
                "name": "new_car.jpg",
                "createdAt": "2022-06-15T11:34:36.294Z",
                "updatedAt": "2022-07-04T10:15:50.067Z",
                "fileId": "fake_123",
                "tags": ["Tag_1", "Tag_2", "Tag_3"],
                "AITags": [{
                    "name": "Clothing",
                    "confidence": 98.77,
                    "source": "google-auto-tagging"
                }, {
                    "name": "Smile",
                    "confidence": 95.31,
                    "source": "google-auto-tagging"
                }, {
                    "name": "Shoe",
                    "confidence": 95.2,
                    "source": "google-auto-tagging"
                }],
                "versionInfo": {
                    "id": "versionId",
                    "name": "Version 4"
                },
                "embeddedMetadata": {
                    "DateCreated": "2022-07-04T10:15:50.066Z",
                    "DateTimeCreated": "2022-07-04T10:15:50.066Z"
                },
                "customCoordinates": "",
                "customMetadata": {
                    "test100": 10,
                    "test10": 11
                },
                "isPrivateFile": false,
                "url": "https://ik.imagekit.io/your_imagekit_id/new_car.jpg",
                "thumbnail": "https://ik.imagekit.io/your_imagekit_id/tr:n-ik_ml_thumbnail/new_car.jpg",
                "fileType": "image",
                "filePath": "/new_car.jpg",
                "height": 354,
                "width": 236,
                "size": 7390,
                "hasAlpha": false,
                "mime": "image/jpeg"
            }, {
                "type": "file-version",
                "name": "new_car.jpg",
                "createdAt": "2022-07-04T10:15:49.698Z",
                "updatedAt": "2022-07-04T10:15:49.734Z",
                "fileId": "fileId",
                "tags": ["Tag_1", "Tag_2", "Tag_3"],
                "AITags": [{
                    "name": "Clothing",
                    "confidence": 98.77,
                    "source": "google-auto-tagging"
                }, {
                    "name": "Smile",
                    "confidence": 95.31,
                    "source": "google-auto-tagging"
                }, {
                    "name": "Shoe",
                    "confidence": 95.2,
                    "source": "google-auto-tagging"
                }, {
                    "name": "Street light",
                    "confidence": 91.05,
                    "source": "google-auto-tagging"
                }],
                "versionInfo": {
                    "id": "62c2bdd5872375c6b8f40fd4",
                    "name": "Version 1"
                },
                "embeddedMetadata": {
                    "XResolution": 250,
                    "YResolution": 250,
                    "DateCreated": "2022-06-15T11:34:36.702Z",
                    "DateTimeCreated": "2022-06-15T11:34:36.702Z"
                },
                "customCoordinates": "10,10,40,40",
                "customMetadata": {
                    "test100": 10,
                    "test10": 11
                },
                "isPrivateFile": false,
                "url": "https://ik.imagekit.io/your_imagekit_id/new_car.jpg?ik-obj-version=dlkUlhiJ7I8OTejhKG38GZJBrsvDBcnz",
                "thumbnail": "https://ik.imagekit.io/your_imagekit_id/tr:n-ik_ml_thumbnail/new_car.jpg?ik-obj-version=dlkUlhiJ7I8OTejhKG38GZJBrsvDBcnz",
                "fileType": "image",
                "filePath": "/new_car.jpg",
                "height": 354,
                "width": 236,
                "size": 23023,
                "hasAlpha": false,
                "mime": "image/jpeg"
            }]""",
            headers=headers,
        )
        resp = self.client.get_file_versions(self.file_id)
        mock_response_metadata = {
            "raw": [
                {
                    "type": "file",
                    "name": "new_car.jpg",
                    "createdAt": "2022-06-15T11:34:36.294Z",
                    "updatedAt": "2022-07-04T10:15:50.067Z",
                    "fileId": "fake_123",
                    "tags": ["Tag_1", "Tag_2", "Tag_3"],
                    "AITags": [
                        {
                            "name": "Clothing",
                            "confidence": 98.77,
                            "source": "google-auto-tagging",
                        },
                        {
                            "name": "Smile",
                            "confidence": 95.31,
                            "source": "google-auto-tagging",
                        },
                        {
                            "name": "Shoe",
                            "confidence": 95.2,
                            "source": "google-auto-tagging",
                        },
                    ],
                    "versionInfo": {"id": "versionId", "name": "Version 4"},
                    "embeddedMetadata": {
                        "DateCreated": "2022-07-04T10:15:50.066Z",
                        "DateTimeCreated": "2022-07-04T10:15:50.066Z",
                    },
                    "customCoordinates": "",
                    "customMetadata": {"test100": 10, "test10": 11},
                    "isPrivateFile": False,
                    "url": "https://ik.imagekit.io/your_imagekit_id/new_car.jpg",
                    "thumbnail": "https://ik.imagekit.io/your_imagekit_id/tr:n-ik_ml_thumbnail/new_car.jpg",
                    "fileType": "image",
                    "filePath": "/new_car.jpg",
                    "height": 354,
                    "width": 236,
                    "size": 7390,
                    "hasAlpha": False,
                    "mime": "image/jpeg",
                },
                {
                    "type": "file-version",
                    "name": "new_car.jpg",
                    "createdAt": "2022-07-04T10:15:49.698Z",
                    "updatedAt": "2022-07-04T10:15:49.734Z",
                    "fileId": "fileId",
                    "tags": ["Tag_1", "Tag_2", "Tag_3"],
                    "AITags": [
                        {
                            "name": "Clothing",
                            "confidence": 98.77,
                            "source": "google-auto-tagging",
                        },
                        {
                            "name": "Smile",
                            "confidence": 95.31,
                            "source": "google-auto-tagging",
                        },
                        {
                            "name": "Shoe",
                            "confidence": 95.2,
                            "source": "google-auto-tagging",
                        },
                        {
                            "name": "Street light",
                            "confidence": 91.05,
                            "source": "google-auto-tagging",
                        },
                    ],
                    "versionInfo": {
                        "id": "62c2bdd5872375c6b8f40fd4",
                        "name": "Version 1",
                    },
                    "embeddedMetadata": {
                        "XResolution": 250,
                        "YResolution": 250,
                        "DateCreated": "2022-06-15T11:34:36.702Z",
                        "DateTimeCreated": "2022-06-15T11:34:36.702Z",
                    },
                    "customCoordinates": "10,10,40,40",
                    "customMetadata": {"test100": 10, "test10": 11},
                    "isPrivateFile": False,
                    "url": "https://ik.imagekit.io/your_imagekit_id/new_car.jpg?ik-obj-version=dlkUlhiJ7I8OTejhKG38GZJBrsvDBcnz",
                    "thumbnail": "https://ik.imagekit.io/your_imagekit_id/tr:n-ik_ml_thumbnail/new_car.jpg?ik-obj-version=dlkUlhiJ7I8OTejhKG38GZJBrsvDBcnz",
                    "fileType": "image",
                    "filePath": "/new_car.jpg",
                    "height": 354,
                    "width": 236,
                    "size": 23023,
                    "hasAlpha": False,
                    "mime": "image/jpeg",
                },
            ],
            "http_status_code": 200,
            "headers": {
                "Content-Type": "text/plain, application/json",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
        }
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual("fake_123", resp.list[0].file_id)
        self.assertEqual("fileId", resp.list[1].file_id)
        self.assertEqual(
            "http://test.com/v1/files/fake_123/versions", responses.calls[0].request.url
        )

    @responses.activate
    def test_get_file_versions_fails_with_404_exception(self) -> None:
        """Test get file versions raises 404 error"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/versions".format(URL.API_BASE_URL, self.file_id)
        try:
            responses.add(
                responses.GET,
                url,
                status=404,
                body="""{"message": "The requested asset does not exist.",
                                 "help": "For support kindly contact us at support@imagekit.io ."}""",
            )
            self.client.get_file_versions(self.file_id)
            self.assertRaises(NotFoundException)
        except NotFoundException as e:
            self.assertEqual("The requested asset does not exist.", e.message)
            self.assertEqual(404, e.response_metadata.http_status_code)

    @responses.activate
    def test_get_file_version_details_fails_on_unauthenticated_request(self):
        """
        Tests if the unauthenticated request restricted
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/versions/{}".format(
            URL.API_BASE_URL, self.file_id, self.version_id
        )
        try:
            responses.add(
                responses.GET,
                url,
                status=403,
                body="""{'message': 'Your account cannot be authenticated.'
                                    , 'help': 'For support kindly contact us at support@imagekit.io .'}""",
            )
            self.client.get_file_version_details(self.file_id, self.version_id)
            self.assertRaises(ForbiddenException)
        except ForbiddenException as e:
            self.assertEqual(e.message, "Your account cannot be authenticated.")
            self.assertEqual(403, e.response_metadata.http_status_code)

    @responses.activate
    def test_get_file_version_details_succeeds_with_id(self):
        """
        Tests if get file version details succeeds with file id
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/versions/{}".format(
            URL.API_BASE_URL, self.file_id, self.version_id
        )

        headers = {"Content-Type": "application/json"}
        headers.update(get_auth_headers_for_test())
        responses.add(
            responses.GET,
            url,
            body="""{
                        "type": "file-version",
                        "name": "new_car.jpg",
                        "createdAt": "2022-06-27T09:24:25.251Z",
                        "updatedAt": "2022-06-27T12:11:11.247Z",
                        "fileId": "fake_123",
                        "tags": ["tagg", "tagg1"],
                        "AITags": "",
                        "versionInfo": {
                            "id": "fake_version_123",
                            "name": "Version 1"
                        },
                        "embeddedMetadata": {
                            "XResolution": 250,
                            "YResolution": 250,
                            "DateCreated": "2022-06-15T11:34:36.702Z",
                            "DateTimeCreated": "2022-06-15T11:34:36.702Z"
                        },
                        "customCoordinates": "10,10,20,20",
                        "customMetadata": {
                            "test100": 10
                        },
                        "isPrivateFile": false,
                        "url": "https://ik.imagekit.io/your-imagekit-id/new_car.jpg?ik-obj-version=hzBNRjaJhZYg.JNu75L2nMDfhjJP4tJH",
                        "thumbnail": "https://ik.imagekit.io/your-imagekit-id/tr:n-ik_ml_thumbnail/new_car.jpg?ik-obj-version=hzBNRjaJhZYg.JNu75L2nMDfhjJP4tJH",
                        "fileType": "image",
                        "filePath": "/new_car.jpg",
                        "height": 354,
                        "width": 236,
                        "size": 23023,
                        "hasAlpha": false,
                        "mime": "image/jpeg"
                    }""",
            headers=headers,
        )
        resp = self.client.get_file_version_details(self.file_id, self.version_id)
        mock_response_metadata = {
            "headers": {
                "Content-Type": "text/plain, application/json",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
            "http_status_code": 200,
            "raw": {
                "AITags": "",
                "createdAt": "2022-06-27T09:24:25.251Z",
                "customCoordinates": "10,10,20,20",
                "customMetadata": {"test100": 10},
                "embeddedMetadata": {
                    "DateCreated": "2022-06-15T11:34:36.702Z",
                    "DateTimeCreated": "2022-06-15T11:34:36.702Z",
                    "XResolution": 250,
                    "YResolution": 250,
                },
                "fileId": "fake_123",
                "filePath": "/new_car.jpg",
                "fileType": "image",
                "hasAlpha": False,
                "height": 354,
                "isPrivateFile": False,
                "mime": "image/jpeg",
                "name": "new_car.jpg",
                "size": 23023,
                "tags": ["tagg", "tagg1"],
                "thumbnail": "https://ik.imagekit.io/your-imagekit-id/tr:n-ik_ml_thumbnail/new_car.jpg?ik-obj-version=hzBNRjaJhZYg.JNu75L2nMDfhjJP4tJH",
                "type": "file-version",
                "updatedAt": "2022-06-27T12:11:11.247Z",
                "url": "https://ik.imagekit.io/your-imagekit-id/new_car.jpg?ik-obj-version=hzBNRjaJhZYg.JNu75L2nMDfhjJP4tJH",
                "versionInfo": {"id": "fake_version_123", "name": "Version 1"},
                "width": 236,
            },
        }

        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual("fake_123", resp.file_id)
        self.assertEqual("fake_version_123", resp.version_info.id)
        self.assertEqual(
            "http://test.com/v1/files/fake_123/versions/fake_version_123",
            responses.calls[0].request.url,
        )

    @responses.activate
    def test_get_file_version_details_fails_with_404_exception(self) -> None:
        """Test get file version details raises 404 error"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/versions/{}".format(
            URL.API_BASE_URL, self.file_id, self.version_id
        )
        try:
            responses.add(
                responses.GET,
                url,
                status=404,
                body="""{"message": "The requested asset does not exist.",
                                 "help": "For support kindly contact us at support@imagekit.io ."}""",
            )
            self.client.get_file_version_details(self.file_id, self.version_id)
            self.assertRaises(NotFoundException)
        except NotFoundException as e:
            self.assertEqual("The requested asset does not exist.", e.message)
            self.assertEqual(404, e.response_metadata.http_status_code)

    @responses.activate
    def test_get_file_version_details_fails_with_400_exception(self) -> None:
        """Test get file version details raises 400 error"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/versions/{}".format(
            URL.API_BASE_URL, self.file_id, self.version_id
        )
        try:
            responses.add(
                responses.GET,
                url,
                status=400,
                body="""{"message": "Your request contains invalid fileId parameter.",
                                 "help": "For support kindly contact us at support@imagekit.io ."}""",
            )
            self.client.get_file_version_details(self.file_id, self.version_id)
            self.assertRaises(BadRequestException)
        except BadRequestException as e:
            self.assertEqual(
                "Your request contains invalid fileId parameter.", e.message
            )
            self.assertEqual(400, e.response_metadata.http_status_code)


class TestDeleteFileVersion(ClientTestCase):
    version_id = "fake_123_version_id"
    file_id = "fax_abx1223"

    @responses.activate
    def test_delete_file_version_fails_with_404_exception(self) -> None:
        """Test delete_file_version raises 404 error"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/versions/{}".format(
            URL.API_BASE_URL, self.file_id, self.version_id
        )
        try:
            responses.add(
                responses.DELETE,
                url,
                status=404,
                body="""{"message": "The requested file version does not exist.",
                                 "help": "For support kindly contact us at support@imagekit.io ."}""",
            )
            self.client.delete_file_version(self.file_id, self.version_id)
            self.assertRaises(NotFoundException)
        except NotFoundException as e:
            self.assertEqual("The requested file version does not exist.", e.message)
            self.assertEqual(404, e.response_metadata.http_status_code)

    @responses.activate
    def test_delete_file_version_succeeds(self) -> None:
        """Test delete_file_version succeeds with file and version Id"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/versions/{}".format(
            URL.API_BASE_URL, self.file_id, self.version_id
        )
        headers = {"Content-Type": "application/json"}
        headers.update(create_headers_for_test())
        responses.add(responses.DELETE, url, status=204, headers=headers, body="{}")
        resp = self.client.delete_file_version(self.file_id, self.version_id)

        mock_response_metadata = {
            "headers": {
                "Content-Type": "text/plain, application/json",
                "Accept-Encoding": "gzip, deflate",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
            "httpStatusCode": 204,
            "raw": None,
        }

        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual(
            "http://test.com/v1/files/fax_abx1223/versions/fake_123_version_id",
            responses.calls[0].request.url,
        )


class TestCopyFile(ClientTestCase):
    source_file_path = "/source_file.jpg"

    destination_path = "/destination_path"

    @responses.activate
    def test_copy_file_fails_with_404(self) -> None:
        """Test copy_file raises 404"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/copy".format(URL.API_BASE_URL)
        headers = {"Content-Type": "application/json"}
        headers.update(create_headers_for_test())
        responses.add(
            responses.POST,
            url,
            status=404,
            headers=headers,
            body="""{
                "message": "No file found with filePath /source_file.jpg",
                "help": "For support kindly contact us at support@imagekit.io .",
                "reason": "SOURCE_FILE_MISSING"
            }""",
        )
        try:
            self.client.copy_file(
                options=CopyFileRequestOptions(
                    source_file_path=self.source_file_path,
                    destination_path=self.destination_path,
                    include_file_versions=False,
                )
            )
            self.assertRaises(NotFoundException)
        except NotFoundException as e:
            self.assertEqual("No file found with filePath /source_file.jpg", e.message)
            self.assertEqual(404, e.response_metadata.http_status_code)

    @responses.activate
    def test_copy_file_succeeds(self) -> None:
        """Test copy_file succeeds"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/copy".format(URL.API_BASE_URL)
        headers = {"Content-Type": "application/json"}
        headers.update(create_headers_for_test())
        responses.add(responses.POST, url, status=204, headers=headers, body="{}")

        resp = self.client.copy_file(
            options=CopyFileRequestOptions(
                source_file_path=self.source_file_path,
                destination_path=self.destination_path,
                include_file_versions=True,
            )
        )

        mock_response_metadata = {
            "headers": {
                "Content-Type": "text/plain, application/json",
                "Accept-Encoding": "gzip, deflate",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
            "httpStatusCode": 204,
            "raw": None,
        }

        request_body = json.dumps(
            json.loads(
                """{
                "sourceFilePath": "/source_file.jpg",
                "destinationPath": "/destination_path",
                "includeFileVersions": true
            }"""
            )
        )

        self.assertEqual(request_body, responses.calls[0].request.body)
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual(
            "http://test.com/v1/files/copy", responses.calls[0].request.url
        )

    @responses.activate
    def test_copy_file_succeeds_without_include_file_versions(self) -> None:
        """Test copy_file succeeds"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/copy".format(URL.API_BASE_URL)
        headers = {"Content-Type": "application/json"}
        headers.update(create_headers_for_test())
        responses.add(responses.POST, url, status=204, headers=headers, body="{}")

        resp = self.client.copy_file(
            options=CopyFileRequestOptions(
                source_file_path=self.source_file_path,
                destination_path=self.destination_path,
            )
        )

        mock_response_metadata = {
            "headers": {
                "Content-Type": "text/plain, application/json",
                "Accept-Encoding": "gzip, deflate",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
            "httpStatusCode": 204,
            "raw": None,
        }

        request_body = json.dumps(
            json.loads(
                """{
                "sourceFilePath": "/source_file.jpg",
                "destinationPath": "/destination_path"
            }"""
            )
        )

        self.assertEqual(request_body, responses.calls[0].request.body)
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual(
            "http://test.com/v1/files/copy", responses.calls[0].request.url
        )


class TestMoveFile(ClientTestCase):
    source_file_path = "/source_file.jpg"

    destination_path = "/destination_path"

    @responses.activate
    def test_move_file_fails_with_404(self) -> None:
        """Test move_file raises 404"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/move".format(URL.API_BASE_URL)
        headers = {"Content-Type": "application/json"}
        headers.update(create_headers_for_test())
        responses.add(
            responses.POST,
            url,
            status=404,
            headers=headers,
            body="""{
                "message": "No file found with filePath /source_file.jpg",
                "help": "For support kindly contact us at support@imagekit.io .",
                "reason": "SOURCE_FILE_MISSING"
            }""",
        )
        try:
            self.client.move_file(
                options=MoveFileRequestOptions(
                    source_file_path=self.source_file_path,
                    destination_path=self.destination_path,
                )
            )
            self.assertRaises(NotFoundException)
        except NotFoundException as e:
            self.assertEqual("No file found with filePath /source_file.jpg", e.message)
            self.assertEqual(404, e.response_metadata.http_status_code)

    @responses.activate
    def test_move_file_succeeds(self) -> None:
        """Test move_file succeeds"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/move".format(URL.API_BASE_URL)
        headers = {"Content-Type": "application/json"}
        headers.update(create_headers_for_test())
        responses.add(responses.POST, url, status=204, headers=headers, body="{}")

        resp = self.client.move_file(
            options=MoveFileRequestOptions(
                source_file_path=self.source_file_path,
                destination_path=self.destination_path,
            )
        )
        mock_response_metadata = {
            "headers": {
                "Content-Type": "text/plain, application/json",
                "Accept-Encoding": "gzip, deflate",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
            "httpStatusCode": 204,
            "raw": None,
        }

        request_body = json.dumps(
            json.loads(
                """{
                "sourceFilePath": "/source_file.jpg",
                "destinationPath": "/destination_path"
            }"""
            )
        )

        self.assertEqual(request_body, responses.calls[0].request.body)
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual(
            "http://test.com/v1/files/move", responses.calls[0].request.url
        )


class TestRenameFile(ClientTestCase):
    file_path = "/file_path.jpg"

    new_file_name = "new_file.jpg"

    @responses.activate
    def test_rename_file_fails_with_409(self) -> None:
        """Test rename_file raises 409"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/rename".format(URL.API_BASE_URL)
        headers = {"Content-Type": "application/json"}
        headers.update(create_headers_for_test())
        try:
            responses.add(
                responses.PUT,
                url,
                status=409,
                headers=headers,
                body="""{
                    "message": "File with name testing-binary.jpg already exists at the same location.",
                    "help": "For support kindly contact us at support@imagekit.io .",
                    "reason": "FILE_ALREADY_EXISTS"
                }""",
            )
            self.client.rename_file(
                options=RenameFileRequestOptions(
                    file_path=self.file_path, new_file_name=self.new_file_name
                )
            )
            self.assertRaises(ConflictException)
        except ConflictException as e:
            self.assertEqual(
                "File with name testing-binary.jpg already exists at the same location.",
                e.message,
            )
            self.assertEqual(409, e.response_metadata.http_status_code)
            self.assertEqual("FILE_ALREADY_EXISTS", e.response_metadata.raw["reason"])

    @responses.activate
    def test_rename_file_succeeds_with_purge_cache_false(self) -> None:
        """Test rename_file succeeds with Purge cache"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/rename".format(URL.API_BASE_URL)
        headers = {"Content-Type": "application/json"}
        headers.update(create_headers_for_test())
        responses.add(
            responses.PUT,
            url,
            headers=headers,
            body="{}",
        )
        resp = self.client.rename_file(
            options=RenameFileRequestOptions(
                file_path=self.file_path,
                new_file_name=self.new_file_name,
                purge_cache=False,
            )
        )

        mock_response_metadata = {
            "headers": {
                "Content-Type": "text/plain, application/json",
                "Accept-Encoding": "gzip, deflate",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
            "httpStatusCode": 200,
            "raw": {},
        }

        request_body = json.dumps(
            json.loads(
                """{
                "filePath": "/file_path.jpg",
                "newFileName": "new_file.jpg",
                "purgeCache": false
            }"""
            )
        )

        self.assertEqual(request_body, responses.calls[0].request.body)
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual(None, resp.purge_request_id)
        self.assertEqual(
            "http://test.com/v1/files/rename", responses.calls[0].request.url
        )

    @responses.activate
    def test_rename_file_succeeds_with_purge_cache(self) -> None:
        """Test rename_file succeeds with Purge cache"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/rename".format(URL.API_BASE_URL)
        headers = {"Content-Type": "application/json"}
        headers.update(create_headers_for_test())
        responses.add(
            responses.PUT,
            url,
            headers=headers,
            body='{"purgeRequestId": "62de3e986f68334a5a3339fb"}',
        )
        resp = self.client.rename_file(
            options=RenameFileRequestOptions(
                file_path=self.file_path,
                new_file_name=self.new_file_name,
                purge_cache=True,
            )
        )

        mock_response_metadata = {
            "headers": {
                "Content-Type": "text/plain, application/json",
                "Accept-Encoding": "gzip, deflate",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
            "httpStatusCode": 200,
            "raw": {"purgeRequestId": "62de3e986f68334a5a3339fb"},
        }

        request_body = json.dumps(
            json.loads(
                """{
                "filePath": "/file_path.jpg",
                "newFileName": "new_file.jpg",
                "purgeCache": true
            }"""
            )
        )

        self.assertEqual(request_body, responses.calls[0].request.body)
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual("62de3e986f68334a5a3339fb", resp.purge_request_id)
        self.assertEqual(
            "http://test.com/v1/files/rename", responses.calls[0].request.url
        )

    @responses.activate
    def test_rename_file_succeeds(self) -> None:
        """Test rename_file succeeds"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/rename".format(URL.API_BASE_URL)
        headers = {"Content-Type": "application/json"}
        headers.update(create_headers_for_test())
        responses.add(responses.PUT, url, headers=headers, body="{}")
        resp = self.client.rename_file(
            options=RenameFileRequestOptions(
                file_path=self.file_path, new_file_name=self.new_file_name
            )
        )
        mock_response_metadata = {
            "headers": {
                "Content-Type": "text/plain, application/json",
                "Accept-Encoding": "gzip, deflate",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
            "httpStatusCode": 200,
            "raw": {},
        }

        request_body = json.dumps(
            json.loads(
                """{
                "filePath": "/file_path.jpg",
                "newFileName": "new_file.jpg"
            }"""
            )
        )

        self.assertEqual(request_body, responses.calls[0].request.body)
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual(None, resp.purge_request_id)
        self.assertEqual(
            "http://test.com/v1/files/rename", responses.calls[0].request.url
        )


class TestRestoreFileVersion(ClientTestCase):
    version_id = "fake_123_version_id"
    file_id = "fax_abx1223"

    @responses.activate
    def test_restore_file_version_fails_with_404_exception(self) -> None:
        """Test restore_file_version raises 404 error"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/versions/{}/restore".format(
            URL.API_BASE_URL, self.file_id, self.version_id
        )
        try:
            responses.add(
                responses.PUT,
                url,
                status=404,
                body="""{"message": "The requested file version does not exist.",
                                 "help": "For support kindly contact us at support@imagekit.io ."}""",
            )
            self.client.restore_file_version(self.file_id, self.version_id)
            self.assertRaises(NotFoundException)
        except NotFoundException as e:
            self.assertEqual("The requested file version does not exist.", e.message)
            self.assertEqual(404, e.response_metadata.http_status_code)

    @responses.activate
    def test_restore_file_version_succeeds(self) -> None:
        """Test restore_file_version succeeds with file and version Id"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/versions/{}/restore".format(
            URL.API_BASE_URL, self.file_id, self.version_id
        )
        headers = {"Content-Type": "application/json"}
        headers.update(create_headers_for_test())
        responses.add(
            responses.PUT,
            url,
            headers=headers,
            body="""{
                "fileId": "fileId",
                "type": "file",
                "name": "file1.jpg",
                "filePath": "/images/file.jpg",
                "tags": ["t-shirt", "round-neck", "sale2019"],
                "AITags": [
                    {
                        "confidence": 90.12,
                        "source": "google-auto-tagging"
                    }],
                "versionInfo": {
                    "id": "versionId",
                    "name": "Version 2"
                },
                "isPrivateFile": false,
                "customCoordinates": "",
                "url": "https://ik.imagekit.io/your_imagekit_id/images/products/file1.jpg",
                "thumbnail": "https://ik.imagekit.io/your_imagekit_id/tr:n-media_library_thumbnail/images/products/file1.jpg",
                "fileType": "image",
                "hasAlpha": false,
                "height": 100,
                "isPrivateFile": false,
                "mime": "image/jpeg",
                "name": "file1.jpg",
                "size": 100,
                "hasAlpha": false,
                "customMetadata": {
                    "brand": "Nike",
                    "color": "red"
                },
                "createdAt": "2019-08-24T06:14:41.313Z",
                "updatedAt": "2019-09-24T06:14:41.313Z"
            }""",
        )
        resp = self.client.restore_file_version(self.file_id, self.version_id)

        mock_response_metadata = {
            "headers": {
                "Content-Type": "text/plain, application/json",
                "Accept-Encoding": "gzip, deflate",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
            "http_status_code": 200,
            "raw": {
                "AITags": [{"confidence": 90.12, "source": "google-auto-tagging"}],
                "createdAt": "2019-08-24T06:14:41.313Z",
                "customCoordinates": "",
                "customMetadata": {"brand": "Nike", "color": "red"},
                "fileId": "fileId",
                "filePath": "/images/file.jpg",
                "fileType": "image",
                "hasAlpha": False,
                "height": 100,
                "isPrivateFile": False,
                "mime": "image/jpeg",
                "name": "file1.jpg",
                "size": 100,
                "tags": ["t-shirt", "round-neck", "sale2019"],
                "thumbnail": "https://ik.imagekit.io/your_imagekit_id/tr:n-media_library_thumbnail/images/products/file1.jpg",
                "type": "file",
                "updatedAt": "2019-09-24T06:14:41.313Z",
                "url": "https://ik.imagekit.io/your_imagekit_id/images/products/file1.jpg",
                "versionInfo": {"id": "versionId", "name": "Version 2"},
            },
        }

        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual("fileId", resp.file_id)
        self.assertEqual("versionId", resp.version_info.id)
        self.assertEqual(
            "http://test.com/v1/files/fax_abx1223/versions/fake_123_version_id/restore",
            responses.calls[0].request.url,
        )
