# You can provide further setup options in the setup.cfg configuration file!
# Below, replace "" with a suitable package name to import even top directory
# modules as <package_name>.<module_name>, etc.
from setuptools import setup, Extension
# from setuptools import find_packages
# from Cython.Build import cythonize

version = "v0.1.0"
ext = [Extension("extension1", ["py_src/extension1.pyx"])]


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
    ext_modules=ext,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "matplotlib",
        "numpy",
        "cython"
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
