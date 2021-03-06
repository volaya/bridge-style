import os
from setuptools import setup, find_packages

exec(open('bridgestyle/version.py').read())
setup(
    name="bridgestyle",
    version=__version__,
    author="GeoCat",
    author_email="volaya@geocat.net",
    description="A library to convert between different map style formats",
    license="MIT",
    keywords="GeoCat",
    url="",
    packages=find_packages(),
    entry_points={"console_scripts": ["style2style=bridgestyle.style2style:main"]},
)
