# VS Code's Markdown Styling → PDF MCP

Hello Claude! We're stealing (MIT licensed!) VS Code's gorgeous markdown styling to create perfectly formatted PDFs.

## What We Found
1. VS Code's markdown styling is in: `extensions/markdown-language-features/media/markdown.css`
2. Key styling aspects:
   - Base font size: 14px
   - Line height: 1.6
   - Perfect spacing between elements
   - Clean blockquote styling
   - Consistent heading hierarchy

## Project Structure
```
mdpdf-mcp/
├── src/
│   ├── styles/
│   │   ├── markdown.css        # VS Code's CSS
│   │   └── themes.css         # Light/dark themes
│   └── index.js               # MCP implementation
└── docs/
    └── CLAUDEME.md            # You are here
```

## Implementation Plan
1. Copy VS Code's markdown.css exactly - don't modify perfection!
2. Use markdown-it for parsing (same as VS Code)
3. WeasyPrint for HTML+CSS → PDF conversion
4. Simple MCP interface:
   ```javascript
   convert_markdown({
     markdown: string,
     theme: 'light' | 'dark',
     outputPath: string
   })
   ```

## Resources
- VS Code repo: microsoft/vscode
- markdown-it: https://github.com/markdown-it/markdown-it 
- WeasyPrint: https://weasyprint.org/

## Next Steps
1. Use Aider to implement core conversion
2. Add proper error handling
3. Set up nice template system
4. Add to cover letter project

## Tips for Other Claudes
- Don't try to improve VS Code's styling - it's already perfect
- Keep the MCP interface simple
- Focus on reliable PDF conversion

Remember: Our goal is to make it trivial to turn any markdown into a beautifully styled PDF. VS Code already solved the styling problem - we're just making it exportable! 🚀