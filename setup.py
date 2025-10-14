"""
Installer for maintenance_gsm
"""

from setuptools import setup, find_packages

with open("requirements.txt") as f:
	requirements = f.read().strip().split("\n")

setup(
	name="maintenance_gsm",
	version="0.0.1",
	description="Maintenance GSM app for ERPNext",
	author="Mehdi khechine",
	author_email="khechine.mehdi@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=requirements
)