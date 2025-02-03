# MD-PDF-MCP Specification

## Overview
MCP server for converting Markdown documents to styled PDFs using VS Code's styling and ReportLab.

## API

### convert_markdown
Converts a markdown document to PDF using VS Code styling.

Input:
```python
{
    "markdown": str,     # Markdown content to convert
    "output_path": str,  # Where to save the PDF
}
```

Output:
```python
{
    "success": bool,     # Whether conversion succeeded
    "path": str,        # Path to generated PDF if successful
    "error": str       # Error message if failed
}
```

## Implementation Details

### Dependencies
- reportlab: PDF generation
- MCP Python SDK: Protocol implementation

### Processing Flow
1. Parse markdown text
2. Apply VS Code styling (via ReportLab styles)
3. Generate PDF using ReportLab
4. Return result via MCP response

### Error Handling
- Invalid markdown: Return parse error
- PDF generation failure: Return error message
- File system errors: Return IO error message

### Style Conversion
VS Code's markdown.css styles are converted to ReportLab's format while maintaining:
- Typography
- Spacing
- Colors
- Element styling