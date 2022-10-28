#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import QijunjiedeFensiqun2019
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('QijunjiedeFensiqun2019'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="qijunjiede-fensiqun-2019",
    version=QijunjiedeFensiqun2019.__version__,
    url="https://github.com/apachecn/qijunjiede-fensiqun-2019",
    author=QijunjiedeFensiqun2019.__author__,
    author_email=QijunjiedeFensiqun2019.__email__,
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
    description="齐俊杰的粉丝群知识星球精华 2019",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "qijunjiede-fensiqun-2019=QijunjiedeFensiqun2019.__main__:main",
            "QijunjiedeFensiqun2019=QijunjiedeFensiqun2019.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
