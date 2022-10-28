#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import MactalkdePengyoumen201907
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('MactalkdePengyoumen201907'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="mactalkde-pengyoumen-201907",
    version=MactalkdePengyoumen201907.__version__,
    url="https://github.com/apachecn/mactalkde-pengyoumen-201907",
    author=MactalkdePengyoumen201907.__author__,
    author_email=MactalkdePengyoumen201907.__email__,
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
    description="MacTalk 的朋友们知识星球精华 20190725",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "mactalkde-pengyoumen-201907=MactalkdePengyoumen201907.__main__:main",
            "MactalkdePengyoumen201907=MactalkdePengyoumen201907.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
