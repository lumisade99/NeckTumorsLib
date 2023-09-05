from setuptools import find_packages, setup

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name='RadImaLib',
    packages=find_packages(include=['RadImaLib']),
    version='0.0.1',
    description='Python library for radiological image processing and analysing',
    author='Ekaterina Zhabrovets',
    long_description=readme,

)