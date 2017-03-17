# -*-coding:utf-8-*-

# Author: Guo Zhang
# Reference:
#   https://setuptools.readthedocs.io/en/latest/setuptools.html#developer-s-guide
#   https://packaging.python.org/distributing/#uploading-your-project-to-pypi

# Update:
#   sudo python setup.py sdist
#   twine upload dist/*

from setuptools import setup, find_packages


setup(
    name='texcleaning',
    version='0.0.1.dev4',

    packages=find_packages(
        exclude=['tests', 'tests.*', '*.tests', '*.tests.*']),
    scripts=['texcleaning.py'],

    description='Clean temporary files by tex engines',
    author='Guo Zhang',
    author_email='zhangguo@stu.xmu.edu.cn',

    entry_points={
        'console_scripts': [
            'texcleaning=texcleaning:main',
        ],
    },
)
