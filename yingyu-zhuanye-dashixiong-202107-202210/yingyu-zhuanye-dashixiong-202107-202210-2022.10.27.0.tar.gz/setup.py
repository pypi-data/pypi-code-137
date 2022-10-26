#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import YingyuZhuanyeDashixiong202107202210
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('YingyuZhuanyeDashixiong202107202210'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="yingyu-zhuanye-dashixiong-202107-202210",
    version=YingyuZhuanyeDashixiong202107202210.__version__,
    url="https://github.com/apachecn/yingyu-zhuanye-dashixiong-202107-202210",
    author=YingyuZhuanyeDashixiong202107202210.__author__,
    author_email=YingyuZhuanyeDashixiong202107202210.__email__,
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
    description="英语专业大师兄 2021.7~2022.10",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "yingyu-zhuanye-dashixiong-202107-202210=YingyuZhuanyeDashixiong202107202210.__main__:main",
            "YingyuZhuanyeDashixiong202107202210=YingyuZhuanyeDashixiong202107202210.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
