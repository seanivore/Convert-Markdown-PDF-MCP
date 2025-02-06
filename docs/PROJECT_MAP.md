# MD-PDF-MCP Project Map

## Current Status
Project initialized with clean structure, focused on using ReportLab for direct MD→PDF conversion.

## High Priority Tasks

### 1. Core PDF Generation
- [ ] Convert VS Code CSS to ReportLab styles `.../src/vscode_styles.py`
- [ ] Test basic PDF generation with styled content
- [ ] Add support for all markdown elements (lists, code blocks, etc)
- [ ] Run a Cover Letter through to see if any adjustments would improve the output 

### 2. Project Documentation
- [ ] Use llm-context to analyze Python MCP SDK: `~/Development/_.llm-context.md` 
  - Set up in SDK directory
  - Capture key implementation patterns
  - Document MCP integration approach
- [ ] Review and include key MCP docs:
  ```
  tests/inspector.mdx
  tests/debugging.mdx
  /docs/concepts/*.mdx
  ```
- [ ] Create implementation guide based on findings

### 3. MCP Server Implementation
- [ ] Follow create-python-mcp walkthrough
- [ ] Set up basic server structure
- [ ] Implement PDF conversion endpoint
- [ ] Add error handling

## Reference Materials
- Original VS Code CSS: `docs/markdown.css`
- Python MCP SDK: `~/Development/mcp-guides-docs-framework/python-sdk/`
- ReportLab documentation & examples
- MCP Core Concepts (from mdx files in `SPECIFICATION.md`)

## Future Enhancements
- Support for dark/light themes
- Custom styling options
- Batch processing
- Progress reporting

## Development Rules
1. Keep it simple - direct MD → PDF conversion
2. Use ReportLab's built-in features
3. Test each component before integration
4. Document as we go

## Tools & Tips
- Use llm-context for exploring large codebases
- Test PDF generation separately from MCP integration
- Keep commits focused and documented
- Use sequential thinking for complex changes