from setuptools import setup, find_packages

setup(
    name="simconnect_mobiflight",
    version="0.3.0",
    packages=find_packages(include=["simconnect_mobiflight*"]),
    install_requires=["SimConnect>=0.1.0"],
    author="Koseng",
    description="SimConnect Python extension for MobiFlight InputEvents",
    url="https://github.com/Koseng/MSFSPythonSimConnectMobiFlightExtension",
    classifiers=["Programming Language :: Python :: 3"],
    python_requires=">=3.10",
)
