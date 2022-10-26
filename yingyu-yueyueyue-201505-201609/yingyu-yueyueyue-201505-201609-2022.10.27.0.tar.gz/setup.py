#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import YingyuYueyueyue201505201609
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('YingyuYueyueyue201505201609'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="yingyu-yueyueyue-201505-201609",
    version=YingyuYueyueyue201505201609.__version__,
    url="https://github.com/apachecn/yingyu-yueyueyue-201505-201609",
    author=YingyuYueyueyue201505201609.__author__,
    author_email=YingyuYueyueyue201505201609.__email__,
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
    description="英语曰曰曰 2015.5~2016.9",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "yingyu-yueyueyue-201505-201609=YingyuYueyueyue201505201609.__main__:main",
            "YingyuYueyueyue201505201609=YingyuYueyueyue201505201609.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
