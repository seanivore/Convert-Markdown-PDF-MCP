# MD-PDF-MCP Specification

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

## Resources
- VS Code's markdown.css: `/docs/markdown.css`

- PythonLibrary.org's ReportLab: 
`https://www.blog.pythonlibrary.org/2021/09/28/python-101-how-to-generate-a-pdf/`

- MCP Python SDK Template Walkthrough: 
	1. Go to `cd ~/Development/mcp-guides-docs-framework/create-python-server` 
	2. Run `uvx create-mcp-server`
	3. Follow the step by step instructions. 

- Python MCP SDK README ToC Request Files You Need — OR try llm-context tool: 
`~/Development/mcp-guides-docs-framework/python-sdk/README.md`
Command Tool Guide: `~/Development/_.llm-context.md`

- Inspect Server Connection & Debug MCP Workflow
`tests/inspector.mdx`
`tests/debugging.mdx`

- MCP Core Concepts: 
`/docs/concepts/architecture.mdx`
`/docs/concepts/prompts.mdx`
`/docs/concepts/resources.mdx`
`/docs/concepts/roots.mdx`
`/docs/concepts/sampling.mdx`
`/docs/concepts/tools.mdx`
`/docs/concepts/transports.mdx`

- Guide for LLMs Building MCP Servers: 
`~/Development/_llms-dev-mcps.txt`

- See if Fetch MCP is potentially better than the *web-browser-mcp-server* 
`/Users/seanivore/Development/fetch-mcp/README.md`