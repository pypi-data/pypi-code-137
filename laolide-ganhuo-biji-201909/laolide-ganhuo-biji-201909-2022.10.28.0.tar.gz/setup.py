#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import LaolideGanhuoBiji201909
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('LaolideGanhuoBiji201909'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="laolide-ganhuo-biji-201909",
    version=LaolideGanhuoBiji201909.__version__,
    url="https://github.com/apachecn/laolide-ganhuo-biji-201909",
    author=LaolideGanhuoBiji201909.__author__,
    author_email=LaolideGanhuoBiji201909.__email__,
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
    description="老李的干货笔记知识星球精华 20190908",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "laolide-ganhuo-biji-201909=LaolideGanhuoBiji201909.__main__:main",
            "LaolideGanhuoBiji201909=LaolideGanhuoBiji201909.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
