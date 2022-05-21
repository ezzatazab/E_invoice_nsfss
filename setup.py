from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in e_invoice_nsfss/__init__.py
from e_invoice_nsfss import __version__ as version

setup(
	name="e_invoice_nsfss",
	version=version,
	description="e invoice egypt",
	author="nsfss",
	author_email="ezzat.orc@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
