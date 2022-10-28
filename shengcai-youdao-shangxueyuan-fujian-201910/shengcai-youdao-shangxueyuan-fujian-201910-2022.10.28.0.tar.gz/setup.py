#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import ShengcaiYoudaoShangxueyuanFujian201910
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('ShengcaiYoudaoShangxueyuanFujian201910'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="shengcai-youdao-shangxueyuan-fujian-201910",
    version=ShengcaiYoudaoShangxueyuanFujian201910.__version__,
    url="https://github.com/apachecn/shengcai-youdao-shangxueyuan-fujian-201910",
    author=ShengcaiYoudaoShangxueyuanFujian201910.__author__,
    author_email=ShengcaiYoudaoShangxueyuanFujian201910.__email__,
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
    description="生财有道商学院知识星球附件 20190611-20191003",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "shengcai-youdao-shangxueyuan-fujian-201910=ShengcaiYoudaoShangxueyuanFujian201910.__main__:main",
            "ShengcaiYoudaoShangxueyuanFujian201910=ShengcaiYoudaoShangxueyuanFujian201910.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
