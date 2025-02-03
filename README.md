# md-pdf-mcp

A Model Context Protocol (MCP) server that converts Markdown to gorgeously styled PDFs using VS Code's markdown styling and Python's ReportLab.

## Why?
VS Code has some of the most beautiful markdown rendering out there - clean typography, perfect spacing, and just the right amount of styling. This MCP server lets you generate PDFs with that exact same styling, powered by Python's industry-standard PDF library, ReportLab.

## Features
- Uses VS Code's markdown CSS (MIT licensed)
- Powered by ReportLab - Python's battle-tested PDF library
- Perfect typography and spacing
- Code syntax highlighting
- Simple MCP interface

## Quick Start
```bash
# Clone the repository
git clone https://github.com/yourusername/md-pdf-mcp
cd md-pdf-mcp

# Set up environment
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install dependencies
pip install -r requirements.txt

# Copy example environment file and edit as needed
cp .env.example .env
```

## Usage
The server exposes a single tool:
```python
convert_markdown(
    markdown: str,       # Markdown content to convert
    output_path: str,    # Where to save the PDF
) -> bool:              # Returns True if successful
```

## Development
- Python 3.10+
- ReportLab for PDF generation
- VS Code markdown styling
- MCP server framework

## Acknowledgments
- VS Code markdown styling (MIT licensed)
- ReportLab team for their amazing PDF library