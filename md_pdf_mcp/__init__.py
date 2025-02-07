"""
MD-PDF-MCP: VS Code-styled Markdown to PDF converter

This module provides the core functionality for converting markdown documents to PDFs
using VS Code's exact styling through ReportLab's PLATYPUS framework.
"""

import asyncio
from .server import serve
from .converter import (
    convert_markdown_to_pdf,
    MDPDFError,
    InvalidMarkdownError,
    PDFGenerationError,
    ImageError
)

__version__ = "0.1.0"

async def _async_main():
    """Async entry point for the MCP server."""
    await serve()

def main():
    """Synchronous entry point for the MCP server.
    
    This is the entry point used by the console script defined in pyproject.toml.
    It wraps the async entry point in asyncio.run().
    """
    asyncio.run(_async_main())

if __name__ == '__main__':
    main()