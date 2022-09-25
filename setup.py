import os

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="pytest-sqlalchemy-mock",
    license="MIT",
    description="pytest sqlalchemy plugin for mock",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    version="0.1.3",
    author="Resul Yurttakalan",
    author_email="resulyrt93@gmail.com",
    url="https://github.com/resulyrt93/pytest-sqlalchemy-mock",
    package_dir={"": "pytest_sqlalchemy_mock"},
    entry_points={"pytest11": ["sqlalchemy = pytest_sqlalchemy_mock"]},
    install_requires=["pytest>=2.0", "sqlalchemy"],
    classifiers=[
        "Framework :: Pytest",
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development :: Testing",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
