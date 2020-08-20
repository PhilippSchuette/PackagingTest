# You can provide further setup options in a setup.cfg configuration file!
from setuptools import setup, find_packages

version = "v0.0.1"
description = """This package explores how to document, test and distribute
a Python package."""

setup(
    name="mypackagingtest",
    version=version,
    description="This is a test for Python packaging",
    long_description=description,
    long_description_content_type="text/plain",
    url="",  # Github repo URL
    download_url="",  # PyPI URL
    author="Philipp Schuette",
    author_email="pschuet2@math.upb.de",
    license="MIT",
    package_dir={"": "py_src"},
    packages=find_packages(
        where="./py_src", exclude=["tests.*"]
    ),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "matplotlib",
        "numpy"
    ],
    zip_safe=False
)
