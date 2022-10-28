#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import WangxingZhangyimingZhangxiaolongLeijunWenzhang
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('WangxingZhangyimingZhangxiaolongLeijunWenzhang'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="wangxing-zhangyiming-zhangxiaolong-leijun-wenzhang",
    version=WangxingZhangyimingZhangxiaolongLeijunWenzhang.__version__,
    url="https://github.com/apachecn/wangxing-zhangyiming-zhangxiaolong-leijun-wenzhang",
    author=WangxingZhangyimingZhangxiaolongLeijunWenzhang.__author__,
    author_email=WangxingZhangyimingZhangxiaolongLeijunWenzhang.__email__,
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
    description="有关王兴、张一鸣、黄峥、张小龙、雷军最好文章整理",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "wangxing-zhangyiming-zhangxiaolong-leijun-wenzhang=WangxingZhangyimingZhangxiaolongLeijunWenzhang.__main__:main",
            "WangxingZhangyimingZhangxiaolongLeijunWenzhang=WangxingZhangyimingZhangxiaolongLeijunWenzhang.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
