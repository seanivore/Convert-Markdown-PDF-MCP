from setuptools import setup, find_packages 

setup(
    name="md_pdf_mcp",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "markdown",
        "reportlab",
    ],
)