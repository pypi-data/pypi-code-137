#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import ShuaizhangHetadePengyoumenJinghuaVol1
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('ShuaizhangHetadePengyoumenJinghuaVol1'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="shuaizhang-hetade-pengyoumen-jinghua-vol1",
    version=ShuaizhangHetadePengyoumenJinghuaVol1.__version__,
    url="https://github.com/apachecn/shuaizhang-hetade-pengyoumen-jinghua-vol1",
    author=ShuaizhangHetadePengyoumenJinghuaVol1.__author__,
    author_email=ShuaizhangHetadePengyoumenJinghuaVol1.__email__,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: Other/Proprietary License",
        "Natural Language :: Chinese (Simplified)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Text Processing :: Markup :: Markdown",
        "Topic :: Text Processing :: Markup :: HTML",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Documentation",
        "Topic :: Documentation",
    ],
    description="「帅张和他的朋友们」第一期精华电子书",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "shuaizhang-hetade-pengyoumen-jinghua-vol1=ShuaizhangHetadePengyoumenJinghuaVol1.__main__:main",
            "ShuaizhangHetadePengyoumenJinghuaVol1=ShuaizhangHetadePengyoumenJinghuaVol1.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
