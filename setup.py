'''Python setup.py for PyScalix'''
from setuptools import setup
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


# Setting up
setup(
    name="PyScalix",
    version="0.0.7",
    description="Python Package to convert csv files to SQLite database and SQLite database to csv files",
    long_description_content_type="text/markdown",
    long_description=read('README.md'),
    url="https://github.com/husnainkhurshiid/PyScalix.git",
    keywords=['python', 'PyScalix', 'csv to sqlite',
              'sqlite to csv', 'csv', 'husnain khurshid'],
    author="Husnain Khurshid",
    author_email="muhammadhusnainkh@gmail.com",
    packages=["PyScalix"],
    include_package_data=True,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
