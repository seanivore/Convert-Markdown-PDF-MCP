# MD-PDF-MCP: VS Code-Styled Markdown to PDF Converter

Hello fellow Claudes! This is a Python package that converts Markdown to PDF using VS Code's styling. We've just done a major cleanup of the project structure.

## What We Found
- The project was carrying unnecessary Python environment files in the project directory
- Configuration files were scattered
- Documentation was duplicated between README.md and DEVELOPMENT.md
- We had multiple Python versions (3.11 and 3.13) causing confusion

## Project Structure
```
md-pdf-mcp/
├── setup.py           # Build configuration
├── requirements.txt   # Dependencies
├── fonts/            # Font assets and conversion scripts
├── md_pdf_mcp/       # Core package code
├── tests/            # Test files
└── docs/             # Documentation
```

## Implementation Plan
Current status:
- ✅ Cleaned up project structure
- ✅ Removed redundant Python environments
- ✅ Consolidated documentation
- ✅ Standardized on Python 3.13

Next steps:
- Improve font handling
- Refine PDF styling
- Add more test cases

## Resources
Key files:
- `/md_pdf_mcp/vscode_styles.py` - Core styling logic
- `/md_pdf_mcp/__init__.py` - Main conversion logic
- `/tests/cv-text-test.md` - Test document

## Tips for Other Claudes
1. Keep virtual environments outside project directory (e.g., `~/.venvs/md-pdf-mcp`)
2. Use `setup.py` and `requirements.txt` in root (standard Python practice)
3. The fonts directory needs to stay in project as it contains assets used by the code
4. Watch for font path references in `vscode_styles.py` when making changes

Remember: This project is about matching VS Code's beautiful markdown styling in PDF output. Focus on typography and spacing! 🎨