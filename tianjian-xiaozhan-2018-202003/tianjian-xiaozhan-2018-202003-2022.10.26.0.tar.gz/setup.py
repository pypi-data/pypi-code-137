#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import TianjianXiaozhan2018202003
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('TianjianXiaozhan2018202003'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="tianjian-xiaozhan-2018-202003",
    version=TianjianXiaozhan2018202003.__version__,
    url="https://github.com/apachecn/tianjian-xiaozhan-2018-202003",
    author=TianjianXiaozhan2018202003.__author__,
    author_email=TianjianXiaozhan2018202003.__email__,
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
    description="田间小站 2018~2020.3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "tianjian-xiaozhan-2018-202003=TianjianXiaozhan2018202003.__main__:main",
            "TianjianXiaozhan2018202003=TianjianXiaozhan2018202003.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
