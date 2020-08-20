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
    py_modules=["module1", "module2", "module3"],
    package_dir={"": "py_src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "matplotlib",
        "numpy"
    ],
    zip_safe=False
)
