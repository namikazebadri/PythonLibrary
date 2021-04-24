import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ecs_pip_test_lib",
    version="1.0.0",
    author="Unis Badri",
    author_email="unis.badri@elementcreativestudio.com",
    description="Test library example for pypi.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/namikazebadri/PIPTestLib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)