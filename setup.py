from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in sign_rfq/__init__.py
from sign_rfq import __version__ as version

setup(
	name="sign_rfq",
	version=version,
	description="Signature in supplier rfq mail",
	author="craft",
	author_email="craft2interactive.ae",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
