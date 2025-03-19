"""
A self-contained example of converting Markdown to PDF with VS Code styling using ReportLab.
This example includes the essential elements from the md-pdf-mcp project.
"""

from reportlab.lib import colors
from reportlab.lib.styles import StyleSheet1, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.colors import Color, HexColor
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
import markdown
from xml.etree import ElementTree

def px_to_pt(px: float) -> float:
    """Convert pixels to points (1px = 0.75pt)"""
    return px * 0.75

def em_to_pt(em: float, base_size: float = 14) -> float:
    """Convert em to points based on base font size"""
    return em * base_size

# VS Code's exact colors
THEME_COLORS = {
    'light': {
        'text': colors.black,
        'background': colors.white,
        'link': HexColor('#0090f1'),
        'pre_background': Color(30/255, 30/255, 30/255, alpha=0.95),
        'pre_text': Color(220/255, 220/255, 220/255),
        'comment': Color(87/255, 166/255, 74/255),
        'widget_border': Color(0, 0, 0, alpha=0.14),
    }
}

def get_vscode_stylesheet(theme: str = 'light') -> StyleSheet1:
    """Generate a ReportLab StyleSheet matching VS Code's markdown styling."""
    styles = StyleSheet1()
    theme_colors = THEME_COLORS[theme]

    # Base style for normal document flow
    styles.add(ParagraphStyle(
        name='Body',
        fontName='Helvetica',  # Using standard font instead of custom fonts
        fontSize=px_to_pt(11),
        leading=em_to_pt(1.2),
        textColor=theme_colors['text'],
        backColor=theme_colors['background'],
        alignment=TA_LEFT,
        spaceAfter=em_to_pt(1.0),
    ))

    # Heading styles
    styles.add(ParagraphStyle(
        name='Heading1',
        parent=styles['Body'],
        fontName='Helvetica-Bold',
        fontSize=px_to_pt(28),
        leading=em_to_pt(1.5),
        spaceBefore=em_to_pt(0.2),
        spaceAfter=em_to_pt(0.5),
    ))

    styles.add(ParagraphStyle(
        name='Heading2',
        parent=styles['Body'],
        fontName='Helvetica-Bold',
        fontSize=px_to_pt(21),
        leading=em_to_pt(1.15),
        spaceBefore=em_to_pt(0.2),
        spaceAfter=em_to_pt(0.5),
    ))

    styles.add(ParagraphStyle(
        name='Heading3',
        parent=styles['Body'],
        fontName='Helvetica-Bold',
        fontSize=px_to_pt(16),
        leading=em_to_pt(1.2),
        spaceBefore=em_to_pt(0.2),
        spaceAfter=em_to_pt(0.5),
    ))

    # Emphasized text (italics)
    styles.add(ParagraphStyle(
        name='Emphasis',
        parent=styles['Body'],
        fontName='Helvetica-Oblique',
    ))

    # Strong text (bold)
    styles.add(ParagraphStyle(
        name='Strong',
        parent=styles['Body'],
        fontName='Helvetica-Bold',
    ))

    return styles

def process_inline_text(element) -> str:
    """Process inline text formatting (bold, italic, etc.)"""
    if element.text is None:
        element.text = ''
        
    text = element.text
    
    for child in element:
        if child.text:
            if child.tag == 'strong' or child.tag == 'b':
                text += f'<b>{child.text}</b>'
            elif child.tag == 'em' or child.tag == 'i':
                text += f'<i>{child.text}</i>'
            else:
                text += child.text
                
        if child.tail:
            text += child.tail
            
    return text.strip()

def convert_markdown_to_pdf(markdown_text: str, output_path: str, theme: str = 'light') -> None:
    """Convert markdown to PDF using VS Code styling."""
    # Parse markdown to HTML with extensions
    html = markdown.markdown(
        markdown_text,
        extensions=['extra'],
        output_format='xhtml'
    )
    
    # Create PDF document with styles
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=72
    )
    
    styles = get_vscode_stylesheet(theme)
    elements = []
    
    # Convert HTML to flowables
    root = ElementTree.fromstring(f"<root>{html}</root>")
    
    for element in root.iter():
        if element.tag == 'root':
            continue
        
        if element.tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            text = process_inline_text(element)
            style = f'Heading{element.tag[1]}'
            elements.append(Paragraph(text, styles[style]))
            
        elif element.tag == 'p':
            text = process_inline_text(element)
            elements.append(Paragraph(text, styles['Body']))
            
    # Build the PDF
    doc.build(elements)

# Example usage
if __name__ == '__main__':
    # Sample markdown text
    markdown_text = """
# Main Title

## Section 1
This is a paragraph with **bold** and *italic* text.

## Section 2
Another paragraph with some text.
"""
    
    # Convert to PDF
    convert_markdown_to_pdf(markdown_text, 'output.pdf')
    print("PDF has been created as 'output.pdf'") 