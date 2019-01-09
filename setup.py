import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="credential_manager",
    version="0.0.1",
    author="Harikeshav R aka TheProgrammingKid",
    author_email="r.harikeshav@gmail.com",
    description="A creddential manager for handling login, signup etc in your python projects.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
