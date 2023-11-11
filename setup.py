from pathlib import Path
from setuptools import find_packages, setup

setup_args = {
    "name": "python-ezconfig",
    "version": "0.1.3",
    "author_email": "zrxmax@icloud.com",
    "url": "https://github.com/zrxmax/python-ezconfig",
    "license": "MIT",
    "author": "zrxmax",
    "description": "Super easy access to configuration file, by pretty interface",
    "long_description": Path("README.md").read_text(encoding="utf-8"),
    "long_description_content_type": "text/markdown",
    "install_requires": [
        "rich>=11.0.0",
    ],
    "keywords": ["ezconfig", "python-ezconfig", "easyconfig", "easy", "pretty", "beatiful", "beauti", "config", "env"],
    "classifiers": [
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    "packages": find_packages(),
    "python_requires": ">=3.7"
}

if __name__ == "__main__":
    setup(**setup_args)