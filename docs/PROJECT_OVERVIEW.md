# Aider Development Guide
Markdown Styling Rendered to PDF MCP Build 

## Overview 

When you preview markdown documents in Cursor or VS Code, it is really pretty. Why do none of these tools make it easy to print or export to PDF? Who knows. 

What we do know is that their markdown styling CSS code is totally available. We also know that OfficialMCP.io has some super fast and easy MCP frameworks out there. 

So, let's use the CSS code from Cursor and VS Code, plus the MCP framework from OfficialMCP.io, and make our own MCP server that will pump out the prettiest PDFs know to Claude. 

This will be a stand alone MCP, but we'll also be able to plug it into the MCP-Agent framework for our cover letter agent MCP. 

## Key Resources
1. **VS Code's MIT Licensed Open Source Markdown CSS**
	- `/Users/seanivore/Development/mdpdf-mcp/src/styles/markdown.css`
	- Good as is, no changes needed. 

2. **Markdown-It Node.js for Parsing** 
	- NPM: `https://www.npmjs.com/package/markdown-it?activeTab=readme` 
	- Dependencies: `https://www.npmjs.com/package/markdown-it?activeTab=dependencies`
	- Dev Docs: `https://github.com/markdown-it/markdown-it/tree/master/docs` 
	- Github Home: `https://github.com/markdown-it/markdown-it#readme` 

3. **WeasyPrint for HTML+CSS to PDF Coversion**
	- Docs: `https://doc.courtbouillon.org/weasyprint/stable/first_steps.html`
	- Dependencies: `https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#macports` 
	- Issues & tests: `https://github.com/Kozea/WeasyPrint` 

4. **Simple MCP Wrapper**
	- Guide for LLMs building MCPs: `/Users/seanivore/Development/_llms-full.txt` 
	- SDKs, typescript: `https://github.com/modelcontextprotocol/typescript-sdk` or python: `https://github.com/modelcontextprotocol/python-sdk` 
	- Official inspector: `https://modelcontextprotocol.io/docs/tools/inspector` 
	- Debugging: `https://modelcontextprotocol.io/docs/tools/debugging` 
	- MCP Server Template, python: `https://github.com/modelcontextprotocol/create-python-server` or typescript: `https://github.com/modelcontextprotocol/create-typescript-server` 
	- Suggested typescriptframeworks, easy: `https://github.com/zcaceres/easy-mcp/` or fast: `https://github.com/punkpeye/fastmcp`
	   ```javascript
   convert_markdown({
     markdown: string,
     theme: 'light' | 'dark',
     outputPath: string
   })
   ```
## Development 
1. Review and select frameworks 
2. Create a DEVELOPMENT_PLAN.md document 
3. Create a SPECIFICATION.md document and record as you go 
4. Integration of tools
5. Core MCP conventions 
6. File structure 
7. Error handling 
8. Testing 
9. Any other documentation 
10. Publication! 

### Project Structure 
- Repository: `mdpdf-mcp`
- Branch: `mdpdf-mcp`
- Path: /Users/seanivore/Development/mdpdf-mcp
```
mdpdf-mcp/
├── src/
│   ├── styles/
│   │   ├── markdown.css 		# VS Code's CSS
│   │   └── themes.css 			# Light/dark themes
│   └── index.js 				# MCP implementation
└── docs/
    └── AIDER_NEXT.md 			# You are here
```

### Thoughts
- No need to improve VS Code's styling, it's perfect. 
- Keep the MCP interface simple 
- Focus on reliable PDF conversion 
- Add proper error handling 
- Set up nice template system 
- Add to cover letter project 

Remember: Our goal is to make it trivial to turn any markdown into a beautifully styled PDF. VS Code already solved the styling problem - we're just making it exportable! 🚀

Companies literally charge subscription fees for you to be able to print a Markdown Rendered PDF Document. Let's democratize this yeah! 