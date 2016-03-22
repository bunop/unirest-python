
import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

sys.path.insert(0, os.path.join(os.getcwd(), "unirest"))

from version import __version__

setup(
    name='Unirest',
    version=__version__,
    author='Mashape',
    author_email='opensource@mashape.com',
    packages=['unirest'],
    url='https://github.com/Mashape/unirest-python',
    license='LICENSE',
    description='Simplified, lightweight HTTP client library',
    install_requires=[
        "poster >= 0.8.1"
    ],
    
    # testing modules
    test_suite = "test"
)
