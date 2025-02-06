# VS Code's Markdown Styling → PDF MCP

Hello Claude! We're creating perfectly formatted PDFs using VS Code's gorgeous markdown styling and Python's ReportLab.

## What We Have
1. VS Code's markdown.css in docs/ (MIT licensed!)
2. Direct conversion to ReportLab styles
3. Simple Python-based approach

## Key Style Elements
- Base font size: 14px
- Line height: 1.6
- Perfect spacing between elements
- Clean blockquote styling
- Consistent heading hierarchy

## Project Structure
```
md-pdf-mcp/
├── src/
│   ├── vscode_styles.py    # ReportLab style conversion
│   └── __init__.py        # Package initialization
├── tests/
│   └── test_pdf.py        # Tests and demos
├── docs/
│   ├── markdown.css       # Original VS Code CSS
│   ├── PROJECT_MAP.md
│   ├── SPECIFICATION.md
│   └── mcp-core-documentation/
│       ├── concepts/
│       │   ├── architecture.mdx
│       │   ├── prompts.mdx
│       │   ├── resources.mdx
│       │   ├── roots.mdx
│       │   └── sampling.mdx
│       └── testing/
│           ├── inspector.mdx
│           └── debugging.mdx
├── CLAUDEME.md           # You are here!
├── README.md
├── .env.example
└── .gitignore
```

## Implementation Notes
1. VS Code's CSS converted exactly to ReportLab styles - no modifications!
2. Using ReportLab - Python's trusted PDF library
3. Simple MCP interface that's easy to use
4. Clean project structure

## Resources
- VS Code repo: microsoft/vscode (for markdown.css)
- ReportLab docs: https://www.reportlab.com/docs/reportlab-userguide.pdf
- Python MCP framework docs

## Tips for Other Claudes
- Don't modify VS Code's styling - it's perfect as is
- Keep the MCP interface simple
- Focus on reliable PDF conversion
- Use sequential thinking to verify changes
- Keep commits focused and clear

Remember: Our goal is to make it trivial to turn any markdown into a beautifully styled PDF. VS Code solved the styling, ReportLab solved the PDF generation - we're just connecting them elegantly! 🚀