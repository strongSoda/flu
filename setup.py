import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="flu",
    version="0.0.4",
    description="CLI to generate beautiful & optimised website scaffolds",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/strongSoda/flu",
    author="Imran Khan",
    author_email="ikhan77727@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["flu"],
    include_package_data=True,
    install_requires=["Click", "colorama"],
    entry_points={
        "console_scripts": [
            "flu=flu.__main__:main",
        ]
    },
)