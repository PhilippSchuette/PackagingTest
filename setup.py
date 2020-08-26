# You can provide further setup options in the setup.cfg configuration file!
from setuptools import setup
# from setuptools import find_packages

version = "v0.1.0"


def readme():
    with open("README.rst", 'r') as f:
        return f.read()


setup(
    name="mypackagingtest",
    version=version,
    description="This is a test for Python packaging",
    long_description=readme(),
    long_description_content_type="text/plain",
    url="https://github.com/PhilippSchuette/PackagingTest",
    download_url="",  # PyPI URL
    author="Philipp Schuette",
    author_email="pschuet2@math.upb.de",
    license="MIT",
    py_modules=["module1", "module2", "module3", "sub_module.module4"],
    package_dir={"": "py_src"},
    package_data={
        'py_src': ['py.typed']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "matplotlib",
        "numpy"
    ],
    extras_require={
        "dev": ["mypy", "mypy-extensions", "hypothesis", "flake8", "pytest",
                "pytest-cov", "docstr-coverage"]
    },
    zip_safe=False
)
