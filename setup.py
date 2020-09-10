# You can provide further setup options in the setup.cfg configuration file!
# Below, replace "" with a suitable package name to import even top directory
# modules as <package_name>.<module_name>, etc.

from setuptools import setup, Extension
# from setuptools import find_packages
from Cython.Build import cythonize
import codecs
import os.path


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            return line.split('"')[1]
    else:
        raise RuntimeError("Unable to find version string.")


version = get_version("py_src/__init__.py")
ext = [
    Extension("extension1",
              sources=["py_src/extension1.pyx", "py_src/hello.c"])
]


def readme():
    with open("README.rst", 'r') as f:
        return f.read()


setup(
    name="mypackagingtest",
    version=version,
    description="This is a test for Python packaging",
    long_description=readme(),
    long_description_content_type="text/x-rst",
    url="https://github.com/PhilippSchuette/PackagingTest",
    download_url="",  # PyPI URL
    author="Philipp Schuette",
    author_email="pschuet2@math.upb.de",
    license="MIT",
    package_dir={"": "py_src"},  # could replace "" with package name here
    py_modules=[
        "module1", "module2", "module3", "sub_module.module4",
        "sub_module.__main__"
    ],  # replacing "" would mean <package>.<module> syntax here also!
    package_data={
        'py_src': ['py.typed']
    },
    include_package_data=True,
    ext_modules=cythonize(ext),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "matplotlib",
        "numpy",
        "cython",
        "numba",
        "scipy"
    ],
    extras_require={
        "dev": ["mypy", "mypy-extensions", "hypothesis", "flake8", "pytest",
                "pytest-cov", "docstr-coverage"]
    },
    entry_points={
        "console_scripts": ["test_pack_test=sub_module.__main__:main"]
    },
    zip_safe=False
)
