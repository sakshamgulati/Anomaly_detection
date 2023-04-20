import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r") as requirements_file:
    external_packages = requirements_file.read()

setuptools.setup(
    name="SmartPrice",
    version="0.0.1",
    author="SakshamGulati",
    description="This app is used to showcase the real true price for a used car and can allow users to avoid getting ripped off",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    project_urls={"Bug Tracker": ""},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=external_packages,
    package_dir={"": "src"},
    packages=setuptools.find_namespace_packages(where="src"),
    package_data={"": ["*.yaml"]},
    include_package_data=True,
    python_requires=">=3.7",
)