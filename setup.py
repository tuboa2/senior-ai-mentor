#!/usr/bin/env python3
"""Setup script for senior-ai-mentor."""

from setuptools import setup, find_packages

setup(
    name="senior-ai-mentor",
    version="1.2.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "mentor = senior_mentor.cli:main",
            "agy-mentor = senior_mentor.cli:main",
        ],
    },
    python_requires=">=3.10",
)
