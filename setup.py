import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="commonlib",
    version="0.0.1",
    author="mumahade",
    author_email="mumahade@cisco.com",
    description="Install common lib for Python micro services",
    long_description_content_type="text/markdown",
    url='https://bitbucket-eng-sjc1.cisco.com/bitbucket/projects/CF-BPA/repos/common-python-library',
    project_urls = {
        "Bug Tracker": "https://bitbucket-eng-sjc1.cisco.com/bitbucket/projects/CF-BPA/repos/common-python-library"
    },
    license='CISCO',
    packages=['commonlib'],
    install_requires=['requests'],
)