# VS Code's Markdown to PDF MCP - Project Status

Hello Claude! We're currently working on fixing PDF generation issues we found after initial testing.

## Current State
1. Basic PDF generation works
2. Image handling mostly works
3. Found major issues in testing:
   - Dark theme completely blank (except images)
   - High-contrast theme identical to light theme
   - No formatting preserved (bold/italic)
   - Code blocks show raw markdown
   - Tables broken into inline text
   - Lists missing
   - Block quotes missing styling

## Next Steps

[sean-adding-in-cursor-identified-issues]

[{
	"resource": "/Users/seanivore/Development/md-pdf-mcp/setup.py",
	"owner": "_generated_diagnostic_collection_name_#6",
	"code": {
		"value": "reportMissingModuleSource",
		"target": {
			"$mid": 1,
			"path": "/microsoft/pyright/blob/main/docs/configuration.md",
			"scheme": "https",
			"authority": "github.com",
			"fragment": "reportMissingModuleSource"
		}
	},
	"severity": 4,
	"message": "Import \"setuptools\" could not be resolved from source",
	"source": "Pylance",
	"startLineNumber": 1,
	"startColumn": 6,
	"endLineNumber": 1,
	"endColumn": 16,
	"modelVersionId": 1
}]




### Priority 1: Fix HTML Parsing & Formatting
1. Add Python-Markdown extensions:
   ```python
   markdown.markdown(text, extensions=[
       'fenced_code',
       'tables',
       'extra'
   ])
   ```
2. Implement recursive HTML parsing to preserve formatting
3. Use ReportLab's markup language for inline styles

### Priority 2: Theme Implementation
1. Fix dark theme (currently blank)
2. Implement proper theme color switching
3. Verify high-contrast theme differs from light

### Priority 3: Complex Elements
1. Use proper ReportLab objects:
   - Table for tables
   - ListFlowable for lists
   - Code blocks with styling
   - Blockquote formatting

## Testing Strategy
1. Create small test files for each feature
2. Fix and verify one element at a time
3. Build up to full test document

## File Locations
- Main code: `md_pdf_mcp/__init__.py`
- Styles: `md_pdf_mcp/vscode_styles.py`
- Test files: `tests/test_*.py`

Remember: The markdown->HTML->PDF pipeline needs proper handling at each step to preserve formatting!

## Tips for Next Claude
1. Start with HTML parsing since it affects all themes
2. Test each change with minimal example files
3. Keep ReportLab's markup language reference handy for inline styles
4. VS Code themes are in styles.py but need proper application

Good luck with the fixes! Let's make this PDF generation gorgeous! 🚀