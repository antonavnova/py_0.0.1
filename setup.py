"""
Product: BaseProject
Description: Setup configuration for package distribution
Module: setup
Version: 0.0
Build: 1
Created: 2024-10-06
Modified: 2024-10-06
Author: Anton AV Nova (team Stitch In Da House)
License: MIT
Status: Development
"""

# ДОБАВЛЯЕМ импорт setuptools
from setuptools import setup, find_packages

__version__ = "0.0.1"
__author__ = "Anton AV Nova (team Stitch In Da House)"
__license__ = "MIT"
__status__ = "Development"

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="baseproject",
    version=__version__,
    author=__author__,
    description="Basic Python project structure for GitHub deployment",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.12",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "baseproject=main:main",
        ],
    },
)