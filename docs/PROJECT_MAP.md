# MD-PDF-MCP Project Map

## Overview
This MCP server is a specialized PDF generation component in a larger agent-based framework:
- Part of a workflow including RAG for background/history
- Works with web fetching agents for job listings
- Handles the final output stage: converting to professional PDFs

## Core Components

### MCP Server Interface
- **Resources** - File types we can handle:
  - Markdown files (input) - `markdown://local/{path}`
  - PDF files (output) - `pdf://local/{path}`
- **Roots** - Directory access configuration:
  - Configured through MCP Inspector
  - Controls where files can be read from/written to

### Markdown to PDF Conversion
- VS Code-styled PDF generation
- Bernina font family integration
- Theme support:
  - Light theme
  - High-contrast theme

## Project Structure
```
md_pdf_mcp/
├── __init__.py      # Package initialization
├── __main__.py      # Entry point
├── server.py        # MCP server implementation
├── converter.py     # PDF conversion logic
└── vscode_styles.py # Typography & styling
```

## Future Enhancements
- Integration with other MCP agents in the framework
- Extended markdown feature support
- Custom font configurations
- Additional theme options
