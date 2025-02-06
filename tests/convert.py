from md_pdf_mcp import convert_markdown_to_pdf

# Read the input file
with open('/Users/seanivore/Development/md-pdf-mcp/tests/cv-text-test.md', 'r') as f:
    content = f.read()

# Convert to PDF
convert_markdown_to_pdf(content, '/Users/seanivore/Development/md-pdf-mcp/tests/test_output.pdf', theme='high-contrast')