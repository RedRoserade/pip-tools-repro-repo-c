from setuptools import setup, find_packages

setup(
    name="repo_c",
    version="0.0.1",
    install_requires=["pymongo", "jsonschema"],
    packages=find_packages("."),
)
