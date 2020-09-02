import setuptools
from pathlib import Path
from eliminate_newlines import __version__

with open(Path(__file__).parent / "README.md") as f:
    long_description = f.read()

setuptools.setup(
    name="eliminate-newlines",
    version=__version__,
    author="Patrik Hlobil",
    author_email="patrik.hlobil@googlemail.com",
    description="CLI that formats Python code in such a way that after the function definition header all newlines will be deleted",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PatrikHlobil/Eliminate-Newlines-After-Function-Definition",
    packages=["eliminate_newlines"],
    install_requires=["click>=7.1.2", "colorama>=0.4.3"],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points="""
        [console_scripts]
        eliminate_newlines=eliminate_newlines.cli:cli
    """,
)
