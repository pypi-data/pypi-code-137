#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import WeiniduYingyuMeiwen201503201710
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('WeiniduYingyuMeiwen201503201710'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="weinidu-yingyu-meiwen-201503-201710",
    version=WeiniduYingyuMeiwen201503201710.__version__,
    url="https://github.com/apachecn/weinidu-yingyu-meiwen-201503-201710",
    author=WeiniduYingyuMeiwen201503201710.__author__,
    author_email=WeiniduYingyuMeiwen201503201710.__email__,
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
    description="为你读英语美文 2015.3~2017.10",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "weinidu-yingyu-meiwen-201503-201710=WeiniduYingyuMeiwen201503201710.__main__:main",
            "WeiniduYingyuMeiwen201503201710=WeiniduYingyuMeiwen201503201710.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
