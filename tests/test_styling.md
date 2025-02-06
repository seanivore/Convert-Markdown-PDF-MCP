# VS Code Markdown Styling Test
This document tests all styling elements implemented in the MD-PDF-MCP converter.

## Typography & Text Formatting

### Regular Text
This is a standard paragraph with regular text. It should use the base font size of 14px and a line height of 1.6em. The text should be crisp and clear with proper spacing.

### Emphasis and Strong
*This text is italicized* and **this text is bold**. You can also _italicize_ or __bold__ text this way.

### Links
Here's [a link to our repository](https://github.com/yourusername/md-pdf-mcp). Links should be in VS Code's signature blue color.

## Headings
# Heading 1
Should be 28px (2em) with normal weight and a bottom border

## Heading 2
Should be 21px (1.5em) with normal weight

### Heading 3
Should be 17.5px (1.25em) with normal weight

#### Heading 4
Should be 15.4px (1.1em) with normal weight

##### Heading 5
Should be 14px (same as base) with normal weight

###### Heading 6
Should be 14px in a lighter gray color

## Code Formatting

### Inline Code
Use the `print("Hello World!")` function to output text.

### Code Blocks
```python
def hello_world():
    """Print a friendly greeting."""
    print("Hello from VS Code styling!")
    return True

# Function call
result = hello_world()
```

## Block Elements

### Blockquotes
> This is a blockquote. It should have VS Code's signature left border and proper padding.
> 
> Multiple paragraphs in blockquotes should maintain consistent styling.

### Lists

#### Unordered Lists
- First item
- Second item
  - Nested item one
  - Nested item two
- Third item

#### Ordered Lists
1. First ordered item
2. Second ordered item
   1. Nested ordered item
   2. Another nested item
3. Third ordered item

### Tables
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
| Cell 4   | Cell 5   | Cell 6   |

### Horizontal Rules

Above the rule
***
Below the rule

---

## Extended Elements

### Task Lists
- [x] Completed task
- [ ] Incomplete task
- [x] Another done task

### Images
![VS Code Logo](https://code.visualstudio.com/assets/images/code-stable.png)

### Mixed Content
> Here's a blockquote with mixed content:
> - List item in blockquote
> - Another item with `inline code`
> 
> ```python
> # Code block in blockquote
> print("Nested styling test")
> ```

## Final Notes
This document should comprehensively test our PDF generation capabilities. Each element should maintain VS Code's exact styling specifications.