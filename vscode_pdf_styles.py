"""
VSCode-style PDF stylesheet for ReportLab.
This is a pure stylesheet that can be imported and used by PDF generation code.
No execution code - just style definitions.
"""

from reportlab.lib import colors
from reportlab.lib.styles import StyleSheet1, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.colors import Color, HexColor

def px_to_pt(px: float) -> float:
    """Convert pixels to points (1px = 0.75pt)"""
    return px * 0.75

def em_to_pt(em: float, base_size: float = 14) -> float:
    """Convert em to points based on base font size"""
    return em * base_size

# VSCode's exact colors
THEME_COLORS = {
    'light': {
        'text': colors.black,
        'background': colors.white,
        'link': HexColor('#0090f1'),
        'pre_background': Color(30/255, 30/255, 30/255, alpha=0.95),
        'pre_text': Color(220/255, 220/255, 220/255),
        'comment': Color(87/255, 166/255, 74/255),
        'widget_border': Color(0, 0, 0, alpha=0.14),
    },
    'dark': {
        'text': colors.white,
        'background': Color(30/255, 30/255, 30/255),
        'link': HexColor('#4ec9b0'),
        'pre_background': Color(0, 0, 0, alpha=0.95),
        'pre_text': Color(220/255, 220/255, 220/255),
        'comment': Color(87/255, 166/255, 74/255),
        'widget_border': colors.white,
    }
}

def get_stylesheet(theme: str = 'light') -> StyleSheet1:
    """Get a ReportLab StyleSheet matching VSCode's markdown styling.
    
    Args:
        theme: 'light' or 'dark' theme
        
    Returns:
        StyleSheet1: A ReportLab stylesheet with VSCode-like styles
    """
    styles = StyleSheet1()
    theme_colors = THEME_COLORS[theme]

    # Base style for normal document flow
    styles.add(ParagraphStyle(
        name='Body',
        fontName='Helvetica',  # Using standard font instead of custom fonts
        fontSize=px_to_pt(14),  # VSCode default size
        leading=em_to_pt(1.5),  # Line height
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
        fontSize=px_to_pt(32),  # Larger for main titles
        leading=em_to_pt(1.6),
        spaceBefore=em_to_pt(1.0),
        spaceAfter=em_to_pt(0.8),
    ))

    styles.add(ParagraphStyle(
        name='Heading2',
        parent=styles['Body'],
        fontName='Helvetica-Bold',
        fontSize=px_to_pt(24),
        leading=em_to_pt(1.4),
        spaceBefore=em_to_pt(0.8),
        spaceAfter=em_to_pt(0.6),
    ))

    styles.add(ParagraphStyle(
        name='Heading3',
        parent=styles['Body'],
        fontName='Helvetica-Bold',
        fontSize=px_to_pt(18.72),  # VSCode's scaling
        leading=em_to_pt(1.3),
        spaceBefore=em_to_pt(0.6),
        spaceAfter=em_to_pt(0.4),
    ))

    styles.add(ParagraphStyle(
        name='Heading4',
        parent=styles['Body'],
        fontName='Helvetica-Bold',
        fontSize=px_to_pt(16),
        leading=em_to_pt(1.2),
        spaceBefore=em_to_pt(0.4),
        spaceAfter=em_to_pt(0.3),
    ))

    # Code styles
    styles.add(ParagraphStyle(
        name='Code',
        parent=styles['Body'],
        fontName='Courier',
        fontSize=px_to_pt(13.5),  # VSCode's monospace size
        leading=em_to_pt(1.2),
        textColor=theme_colors['pre_text'],
        backColor=theme_colors['pre_background'],
    ))

    # List styles
    styles.add(ParagraphStyle(
        name='ListItem',
        parent=styles['Body'],
        leftIndent=em_to_pt(1.0),
        firstLineIndent=em_to_pt(0.5),
    ))

    # Link style
    styles.add(ParagraphStyle(
        name='Link',
        parent=styles['Body'],
        textColor=theme_colors['link'],
        underline=True,
    ))

    # Blockquote style
    styles.add(ParagraphStyle(
        name='Blockquote',
        parent=styles['Body'],
        leftIndent=em_to_pt(2.0),
        textColor=Color(128/255, 128/255, 128/255),  # Gray text
        fontName='Helvetica-Oblique',
    ))

    return styles 