#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import YingyuXuexiJinghua202006202102
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('YingyuXuexiJinghua202006202102'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="yingyu-xuexi-jinghua-202006-202102",
    version=YingyuXuexiJinghua202006202102.__version__,
    url="https://github.com/apachecn/yingyu-xuexi-jinghua-202006-202102",
    author=YingyuXuexiJinghua202006202102.__author__,
    author_email=YingyuXuexiJinghua202006202102.__email__,
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
    description="英语学习精华 2020.6~2021.2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "yingyu-xuexi-jinghua-202006-202102=YingyuXuexiJinghua202006202102.__main__:main",
            "YingyuXuexiJinghua202006202102=YingyuXuexiJinghua202006202102.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
