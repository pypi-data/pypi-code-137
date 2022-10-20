import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "ses-verify-identities",
    "version": "4.1.1",
    "description": "@seeebiii/ses-verify-identities",
    "license": "MIT",
    "url": "https://github.com/seeebiii/ses-verify-identities",
    "long_description_content_type": "text/markdown",
    "author": "Sebastian Hesse<info@sebastianhesse.de>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/seeebiii/ses-verify-identities"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "ses_verify_identities",
        "ses_verify_identities._jsii"
    ],
    "package_data": {
        "ses_verify_identities._jsii": [
            "ses-verify-identities@4.1.1.jsii.tgz"
        ],
        "ses_verify_identities": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.7",
    "install_requires": [
        "aws-cdk-lib>=2.22.0, <3.0.0",
        "constructs>=10.0.5, <11.0.0",
        "jsii>=1.63.2, <2.0.0",
        "publication>=0.0.3",
        "typeguard~=2.13.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Typing :: Typed",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
