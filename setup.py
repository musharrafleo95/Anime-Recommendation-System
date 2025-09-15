from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setup(
    name="MLOPS-PROJECT-2",
    version="0.1",
    author="syed",
    packages=find_packages(), # automatically find packages in utils, config, src
    install_requires=requirements
),
