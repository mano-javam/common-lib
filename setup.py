import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="src",
    version="0.0.2",
    author="mumahade",
    author_email="mumahade@cisco.com",
    description="Install common lib for Python micro services",
    url='https://github.com/mano-javam/common-lib.git',
    license='CISCO',
    packages=['src']
)


