# setup.py
from setuptools import setup, find_packages

setup(
    name="pdf-content-extractor",
    version="1.0.0",
    description="A tool to extract text, tables, and images from PDF files.",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "PyPDF2",
        "pdfplumber",
        "pillow",
        "pandas",
    ],
    entry_points={
        "console_scripts": [
            "pdf-extract=main:main",
        ],
    },
)
