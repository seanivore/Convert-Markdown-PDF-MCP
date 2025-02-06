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
python -m venv ~/.venvs/md-pdf-mcp
source ~/.venvs/md-pdf-mcp/bin/activate  # or `venv\Scripts\activate` on Windows

# Install dependencies
pip install -r requirements.txt
pip install -e .
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

### Running Tests
Run all tests:
```bash
pytest tests/
```

Generate test PDFs (won't be auto-deleted):
```bash
python tests/test_pdf.py
```

### Development Tips
1. The `tests/test_styling.md` file contains examples of all supported markdown elements
2. Visual test PDFs are generated in the tests directory as:
   - `sample_light_theme.pdf`
   - `sample_high-contrast_theme.pdf`
3. Use `black` for code formatting:
```bash
black md_pdf_mcp/ tests/
```

## Requirements
- Python 3.13+
- ReportLab for PDF generation
- VS Code markdown styling
- MCP server framework

## Acknowledgments
- VS Code markdown styling (MIT licensed)
- ReportLab team for their amazing PDF library