import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pylcom",
    version="0.0.1",
    author="Warren Gray",
    author_email="warren@warren-gray.com",
    description="An experiment in calculating LCOM values for Python files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sl5r0/pylcom",
    packages=setuptools.find_packages(),
    install_requires=[
        'astroid>=2.0,<3.0'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
