# -*- coding: utf-8 -*-
"""
---------------------------------------------
Created on 2024/11/5 下午5:32
@author: ZhangYundi
@email: yundi.xxii@outlook.com
---------------------------------------------
"""

import os
from setuptools import setup, find_packages

def read(rel_path: str) -> str:
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, rel_path), encoding="utf-8") as fp:
        return fp.read()


def get_version(rel_path: str) -> str:
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")

VERSION = get_version("empyrical/__init__.py")

setup(
    name='empyrical',
    version=VERSION,
    install_requires=['pandas',
                      'six',  # yck
                      'numpy',
                      'scipy',],

    author='ZhangYundi',
    author_email='yundi.xxii@outlook.com',
    packages=find_packages(include=['empyrical', 'empyrical.*']),
    description='empyrical fix version',
    long_description='',
    long_description_content_type='text/markdown',
    url='https://github.com/link-yundi/empyrical',

    scripts=[],
    package_data={},
)
