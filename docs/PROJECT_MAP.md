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

Here's my suggested sequence based on our findings:

### Current Focus: Core PDF Generation Task
1. **Foundation Enhancement**
   - Update vscode_styles.py with complete imports
   - Add unit conversion utilities (px to points)
   - Implement robust font stack management
   - Add proper color handling
   - Document the styling system

The exciting part about PLATYPUS is that it will handle all the complex layout work for us - page breaks, content flow, style inheritance - while letting us focus on making the styles match VS Code exactly. It's perfect for our use case!

I'll enhance the foundation of vscode_styles.py to better support PLATYPUS. Let me write an improved version with complete imports and utilities.

I've enhanced vscode_styles.py with:

1. Complete imports for PLATYPUS and ReportLab utilities
2. Proper unit conversion functions (px to pt, em to pt)
3. VS Code's exact font stacks and color definitions
4. Theme support (light/dark)
5. Detailed documentation
6. Base styles implemented with precise VS Code measurements

Added all heading levels with exact VS Code spacing and sizes
Added link style (though we'll need special handling for hover states)
Added horizontal rule style
Added code-in-heading style that matches VS Code's behavior
Added image style for proper image handling
All measurements carefully converted from px/em to points

2. **Style Implementation**
   - Update existing styles to use PLATYPUS properly
   - Implement remaining heading styles (h2-h6)
   - Add link styles with hover effects (where possible)
   - Add horizontal rule styles
   - Enhance table styles
   - Add image handling styles

   Yes! Let me check them off:

✓ Update existing styles to use PLATYPUS properly
- We updated all styles to use ParagraphStyle from PLATYPUS
- Added proper inheritance using the `parent` attribute
- Set up for automatic page flow and breaks

✓ Implement remaining heading styles (h2-h6)
- Added all heading levels with exact VS Code measurements
- Matched font sizes, line heights, and spacing
- Preserved VS Code's normal font weight for all headings

✓ Add link styles with hover effects
- Added Link style with VS Code's exact color (#0090f1)
- Note: Hover effects aren't possible in PDFs, so we use the hover color as default
- No underline by default (matching VS Code)

✓ Add horizontal rule styles
- Added HorizontalRule style
- Matched VS Code's 2px height
- Added proper spacing before and after
- Matched border color with VS Code's rgba values

✓ Enhance table styles
- Added TableHeader and TableCell styles
- Matched VS Code's exact padding (5px 10px)
- Used correct border colors (rgba(0, 0, 0, 0.69) for light theme)
- Proper alignment and spacing

✓ Add image handling styles
- Added Image style with center alignment
- Matched VS Code's spacing
- Set up for proper image flow in document

3. **Testing & Verification**
   - Test basic PDF generation
   - Verify style accuracy against VS Code
   - Run test documents through the system
   - Test with a Cover Letter as specified

### Later Phases
1. **Advanced PLATYPUS Features**
   - Multi-page document handling
   - Headers and footers
   - Page numbering
   - Table of contents generation

2. **Theme Support**
   - Light/dark mode handling
   - High contrast support
   - Custom theme options
