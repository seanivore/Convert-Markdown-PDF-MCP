# quick_demo.py
from reportlab.platypus import SimpleDocTemplate, Paragraph
from vscode_styles import get_vscode_stylesheet

def create_demo_pdf(output_path):
    # Get our VS Code styles
    styles = get_vscode_stylesheet()
    
    # Create the PDF
    doc = SimpleDocTemplate(output_path)
    
    # Some sample markdown-style content
    content = [
        Paragraph("# Look! It's Working!", styles['Heading1']),
        Paragraph("This is a quick demo of our markdown → PDF conversion.", styles['Body']),
        Paragraph("> And here's a quote that looks just like VS Code's markdown!", styles['Blockquote']),
        Paragraph("```python\nprint('Even code blocks work!')\n```", styles['Code']),
    ]
    
    # Build it!
    doc.build(content)

if __name__ == '__main__':
    create_demo_pdf('demo.pdf')