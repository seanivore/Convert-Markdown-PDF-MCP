# mdpdf-mcp

A Model Context Protocol (MCP) server that converts Markdown to gorgeously styled PDFs using VS Code's markdown styling.

## Why?
VS Code and Cursor have some of the most beautiful markdown rendering out there - clean typography, perfect spacing, and just the right amount of styling. This MCP lets you generate PDFs with that exact same styling.

## Features
- Uses VS Code's markdown CSS (MIT licensed)
- Perfect typography and spacing
- Code syntax highlighting
- Light & dark themes
- Simple MCP interface

## Quick Start
```bash
# Install
npm install mdpdf-mcp

# Start the MCP server
mdpdf-mcp
```

## Usage
The server exposes a single tool:
```javascript
{
  name: 'convert_markdown',
  description: 'Convert markdown to PDF using VS Code styling',
  inputSchema: {
    type: 'object',
    properties: {
      markdown: { type: 'string' },
      theme: { 
        type: 'string',
        enum: ['light', 'dark'],
        default: 'light'
      },
      outputPath: { type: 'string' }
    },
    required: ['markdown', 'outputPath']
  }
}
```

## Acknowledgments
Uses markdown styling from VS Code (MIT licensed)