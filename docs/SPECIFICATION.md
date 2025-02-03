# Markdown PDF MCP Specification

## Overview
MCP server for converting Markdown documents to styled PDFs using VS Code's styling.

## API

### convert_markdown
Converts a markdown document to PDF with VS Code-style rendering.

Input:
```typescript
{
  markdown: string,      // Markdown content to convert
  theme: 'light'|'dark', // Color theme to use
  outputPath: string     // Where to save the PDF
}
```

Output:
```typescript
{
  success: boolean,      // Whether conversion succeeded
  path?: string,         // Path to generated PDF if successful
  error?: string        // Error message if failed
}
```

## Implementation Details

### Dependencies
- markdown-it: Markdown parsing
- WeasyPrint: HTML/CSS to PDF conversion
- MCP TypeScript SDK: Protocol implementation

### Processing Flow
1. Parse markdown to HTML using markdown-it
2. Apply VS Code CSS styling and selected theme
3. Convert to PDF using WeasyPrint
4. Return result via MCP response

### Error Handling
- Invalid markdown: Return parse error
- PDF generation failure: Return WeasyPrint error
- File system errors: Return IO error message
