from setuptools import setup, find_packages

setup(
    name="simconnect_mobiflight",
    version="0.3.0",
    packages=find_packages(),
    install_requires=["SimConnect"],
    author="Koseng",
    description="Unofficial SimConnect extension for MobiFlight InputEvents support",
    url="https://github.com/Koseng/MSFSPythonSimConnectMobiFlightExtension",
)
