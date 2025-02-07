from setuptools import setup, find_packages 

setup(
    name="md-pdf-mcp",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "markdown>=3.7",
        "reportlab>=4.3.0",
        "pillow>=9.0.0",  # Required by ReportLab
        "setuptools>=69.0.0",  # Added to fix import error
    ],
    extras_require={
        'dev': [
            'pytest>=8.3.4',
            'pytest-cov>=4.1.0',
            'black>=24.2.0',
        ]
    },
    python_requires='>=3.8',  # Using modern Python features
)