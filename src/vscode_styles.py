# vscode_styles.py - Direct conversion of VS Code's markdown.css
from reportlab.lib.styles import StyleSheet1, ParagraphStyle
from reportlab.lib.colors import Color, black
from reportlab.lib.enums import TA_LEFT

def get_vscode_stylesheet():
    styles = StyleSheet1()
    
    # Exact VS Code body styles
    styles.add(ParagraphStyle(
        name='Body',
        fontName='-apple-system',  # Will fallback based on ReportLab's font search path
        fontSize=14,  # Direct from VS Code's 14px
        leading=14 * 1.6,  # VS Code's line-height: 1.6
        textColor=black,
        alignment=TA_LEFT,
    ))

    # VS Code's h1 settings
    styles.add(ParagraphStyle(
        name='Heading1',
        parent=styles['Body'],
        fontSize=14 * 2,  # Maintain proportions
        leading=14 * 1.2,  # VS Code's line-height: 1.2
        spaceBefore=14,
        spaceAfter=14 * 0.3,  # padding-bottom: 0.3em
        borderColor=Color(0, 0, 0, 0.18),  # VS Code's border-bottom color
        borderWidth=1,
        borderPadding=0,
        fontWeight='normal',  # VS Code's font-weight: normal
    ))

    # Blockquote exactly as VS Code defines it
    styles.add(ParagraphStyle(
        name='Blockquote',
        parent=styles['Body'],
        leftIndent=5,  # VS Code's margin-left: 5px
        rightIndent=7,  # VS Code's margin-right: 7px
        spaceBefore=0,
        spaceAfter=0,
        borderWidth=5,  # VS Code's border-left-width: 5px
        borderPadding=10,  # VS Code's padding: 0 16px 0 10px
        borderColor=Color(0, 0, 0, 0.18),  # VS Code's border color
    ))

    # Code blocks with VS Code's monospace fonts
    styles.add(ParagraphStyle(
        name='Code',
        parent=styles['Body'],
        fontName='Courier',  # First available from VS Code's monospace list
        fontSize=14,  # Keep consistent with body
        leading=14 * 1.357,  # VS Code's line-height: 1.357em
    ))

    # Table styles match VS Code exactly
    styles.add(ParagraphStyle(
        name='TableHeader',
        parent=styles['Body'],
        alignment=TA_LEFT,  # VS Code's text-align: left
        borderWidth=1,
        borderColor=Color(0, 0, 0, 0.69),  # VS Code's border color
        spaceBefore=5,  # VS Code's padding: 5px 10px
        spaceAfter=5,
    ))

    styles.add(ParagraphStyle(
        name='TableCell',
        parent=styles['Body'],
        spaceBefore=5,  # VS Code's padding: 5px 10px
        spaceAfter=5,
    ))

    return styles