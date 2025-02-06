"""VS Code Markdown Style Implementation for ReportLab PLATYPUS

This module provides an exact implementation of VS Code's markdown styling for ReportLab's
PLATYPUS (Page Layout and Typography Using Scripts) system.
"""

from reportlab.lib import colors
from reportlab.lib.styles import StyleSheet1, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.colors import Color, HexColor

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
        'border': Color(0, 0, 0, alpha=0.18),
        'link': HexColor('#0090f1'),
        'pre_background': Color(30/255, 30/255, 30/255, alpha=0.95),
        'pre_text': Color(220/255, 220/255, 220/255),
        'comment': Color(87/255, 166/255, 74/255),
        'heading6': Color(128/255, 128/255, 128/255),
        'blockquote_border': Color(0, 0, 0, alpha=0.25),
        'blockquote_background': Color(0, 0, 0, alpha=0.03),
        'widget_border': Color(0, 0, 0, alpha=0.14),
    },
    'high-contrast': {
        'text': colors.black,
        'background': colors.white,
        'border': colors.black,
        'link': HexColor('#0090f1'),
        'pre_background': colors.black,
        'pre_text': colors.white,
        'comment': Color(87/255, 166/255, 74/255),
        'heading6': colors.gray,
        'blockquote_border': colors.black,
        'blockquote_background': Color(0, 0, 0, alpha=0.08),
        'widget_border': colors.black,
    }
}

def get_vscode_stylesheet(theme: str = 'light') -> StyleSheet1:
    """Generate a ReportLab StyleSheet matching VS Code's markdown styling."""
    styles = StyleSheet1()
    colors = THEME_COLORS[theme]

    # Base style - matched to HackMD's clean look
    styles.add(ParagraphStyle(
        name='Body',
        fontName='Helvetica',
        fontSize=px_to_pt(11),      
        leading=em_to_pt(1.2),      
        textColor=colors['text'],
        backColor=colors['background'],
        alignment=TA_LEFT,
        spaceAfter=em_to_pt(0.8),   
        firstLineIndent=0,
        bulletIndent=em_to_pt(0.5),
    ))

    # Heading 1 - More prominent with decorative line
    styles.add(ParagraphStyle(
        name='Heading1',
        parent=styles['Body'],
        fontName='Helvetica-Bold',
        fontSize=px_to_pt(28),        # Increased size for more impact
        leading=em_to_pt(1.1),
        spaceBefore=em_to_pt(0.4),
        spaceAfter=em_to_pt(0.2),     # Reduced to bring line closer
        textColor=colors['text'],
        borderWidth=1,                # Add decorative line
        borderColor=colors['text'],
        borderPadding=(0, 0, em_to_pt(0.3), 0),  # Space below line
    ))

    # Role line - closer to H1
    styles.add(ParagraphStyle(
        name='HeaderInfo',
        parent=styles['Body'],
        fontSize=px_to_pt(12),
        leading=em_to_pt(1.15),
        spaceBefore=em_to_pt(0.4),   # More space from H1's line
        spaceAfter=em_to_pt(0.1),
    ))

    # Date style - stands alone
    styles.add(ParagraphStyle(
        name='DateLine',
        parent=styles['HeaderInfo'],
        fontName='Helvetica-Oblique',
        spaceAfter=em_to_pt(1.5),    # More separation before content
    ))

    # Heading 2 - clear section breaks
    styles.add(ParagraphStyle(
        name='Heading2',
        parent=styles['Body'],
        fontName='Helvetica-Bold',
        fontSize=px_to_pt(18),
        leading=em_to_pt(1.1),
        spaceBefore=em_to_pt(1.2),
        spaceAfter=em_to_pt(0.5),
        textColor=colors['text'],
    ))

    # Heading 3 - no bold, more subtle
    styles.add(ParagraphStyle(
        name='Heading3',
        parent=styles['Body'],
        fontName='Helvetica',        # Removed bold
        fontSize=px_to_pt(14),
        leading=em_to_pt(1.2),
        spaceBefore=em_to_pt(0.8),
        spaceAfter=em_to_pt(0.2),
        textColor=colors['text'],
    ))

    # Lists - clean indentation like HackMD
    styles.add(ParagraphStyle(
        name='ListItem',
        parent=styles['Body'],
        leftIndent=em_to_pt(1.2),     # Slightly less indent
        bulletIndent=em_to_pt(0.8),   # Bullets closer to text
        spaceBefore=em_to_pt(0.2),
        spaceAfter=em_to_pt(0.2),
        leading=em_to_pt(1.2),        # Match body text
    ))

    # Blockquote - cleaner look
    styles.add(ParagraphStyle(
        name='Blockquote',
        parent=styles['Body'],
        fontSize=px_to_pt(11),
        leading=em_to_pt(1.2),
        textColor=colors['text'],
        backColor=colors['blockquote_background'],
        borderLeftWidth=3,
        borderLeftColor=colors['border'],
        borderPadding=(em_to_pt(0.3), em_to_pt(0.5), em_to_pt(0.3), em_to_pt(0.5)),
        leftIndent=em_to_pt(1.0),
        alignment=TA_LEFT,           # Explicitly set left alignment
        spaceBefore=em_to_pt(0.2),
        spaceAfter=em_to_pt(0.6),
        firstLineIndent=0,
    ))

    # Emphasized text (italics)
    styles.add(ParagraphStyle(
        name='Emphasis',
        parent=styles['Body'],
        fontName='Helvetica-Oblique',
        textColor=colors['text'],
    ))

    # Strong text (bold)
    styles.add(ParagraphStyle(
        name='Strong',
        parent=styles['Body'],
        fontName='Helvetica-Bold',
        textColor=colors['text'],
    ))

    # Code blocks
    styles.add(ParagraphStyle(
        name='Code',
        parent=styles['Body'],
        fontName='Courier',
        fontSize=px_to_pt(11),
        leading=em_to_pt(1.2),
        textColor=colors['pre_text'],
    ))

    styles.add(ParagraphStyle(
        name='CodeComment',
        parent=styles['Code'],
        textColor=colors['comment'],
    ))

    styles.add(ParagraphStyle(
        name='Pre',
        parent=styles['Code'],
        backColor=colors['pre_background'],
        borderPadding=px_to_pt(12),   # Slightly less padding
        leftIndent=px_to_pt(12),
        rightIndent=px_to_pt(12),
        spaceBefore=px_to_pt(6),
        spaceAfter=px_to_pt(6),
        borderWidth=1,
        borderColor=colors['widget_border'],
        borderRadius=3,
        textColor=colors['pre_text'],
    ))

    # Links
    styles.add(ParagraphStyle(
        name='Link',
        parent=styles['Body'],
        textColor=colors['link'],
        underline=1,
    ))

    # Horizontal Rule
    styles.add(ParagraphStyle(
        name='HorizontalRule',
        parent=styles['Body'],
        borderBottomWidth=1,         # Thinner line
        borderBottomColor=colors['border'],
        spaceBefore=px_to_pt(10),
        spaceAfter=px_to_pt(10),
    ))

    # Signature style - preserve line breaks
    styles.add(ParagraphStyle(
        name='Signature',
        parent=styles['Body'],
        spaceBefore=em_to_pt(1.0),
        spaceAfter=em_to_pt(0.5),
        keepWithNext=True,           # Keep signature lines together
    ))

    return styles