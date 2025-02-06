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
    'dark': {
        'text': colors.black,
        'background': colors.white,
        'border': Color(0, 0, 0, alpha=0.6),
        'link': HexColor('#0090f1'),
        'pre_background': Color(30/255, 30/255, 30/255, alpha=0.95),
        'pre_text': Color(220/255, 220/255, 220/255),
        'comment': Color(87/255, 166/255, 74/255),
        'heading6': colors.gray,
        'blockquote_border': Color(0, 0, 0, alpha=0.6),
        'blockquote_background': Color(0, 0, 0, alpha=0.05),  # Slightly darker for dark theme
        'widget_border': Color(0, 0, 0, alpha=0.3),
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
        'blockquote_background': Color(0, 0, 0, alpha=0.08),  # More visible for high contrast
        'widget_border': colors.black,
    }
}

def get_vscode_stylesheet(theme: str = 'light') -> StyleSheet1:
    """Generate a ReportLab StyleSheet matching VS Code's markdown styling."""
    styles = StyleSheet1()
    colors = THEME_COLORS[theme]
    
    # Base style (VS Code body)
    styles.add(ParagraphStyle(
        name='Body',
        fontName='Helvetica',
        fontSize=px_to_pt(14),
        leading=em_to_pt(1.5),  # Refined line height
        textColor=colors['text'],
        backColor=colors['background'],
        alignment=TA_LEFT,
        spaceAfter=em_to_pt(0.8),  # Tighter paragraph spacing
        firstLineIndent=0,
    ))

    # Heading 1 - adjusted for cover letter
    styles.add(ParagraphStyle(
        name='Heading1',
        parent=styles['Body'],
        fontSize=px_to_pt(36),  # Larger for better hierarchy
        leading=em_to_pt(1.2),  # Tighter for headings
        spaceBefore=em_to_pt(0.5),
        spaceAfter=em_to_pt(1.2),
        borderPadding=(0, 0, em_to_pt(0.3), 0),
        borderBottomWidth=1,
        borderBottomColor=colors['border'],
        textColor=colors['text'],
    ))

    # Heading 2
    styles.add(ParagraphStyle(
        name='Heading2',
        parent=styles['Body'],
        fontSize=px_to_pt(21),  # 1.5em
        leading=em_to_pt(1.4),
        spaceBefore=em_to_pt(1.8),
        spaceAfter=em_to_pt(0.8),
        borderBottomWidth=0.5,  # Add subtle border
        borderBottomColor=colors['border'],
    ))

    # Heading 3
    styles.add(ParagraphStyle(
        name='Heading3',
        parent=styles['Body'],
        fontSize=px_to_pt(17.5),  # 1.25em
        leading=em_to_pt(1.4),
        spaceBefore=em_to_pt(1.5),
        spaceAfter=em_to_pt(0.6),
        borderLeftWidth=3,  # Add vertical line
        borderLeftColor=colors['border'],
        borderPadding=(0, 0, 0, em_to_pt(0.5)),  # Padding for the line
        leftIndent=em_to_pt(0.7),  # Indent to accommodate the line
    ))

    # Heading 4
    styles.add(ParagraphStyle(
        name='Heading4',
        parent=styles['Body'],
        fontSize=px_to_pt(15.4),  # 1.1em
        leading=em_to_pt(1.2),
        spaceBefore=em_to_pt(1.25),
        spaceAfter=px_to_pt(14),
    ))

    # Heading 5
    styles.add(ParagraphStyle(
        name='Heading5',
        parent=styles['Body'],
        fontSize=px_to_pt(14),  # 1em
        leading=em_to_pt(1.2),
        spaceBefore=em_to_pt(1),
        spaceAfter=px_to_pt(14),
    ))

    # Heading 6
    styles.add(ParagraphStyle(
        name='Heading6',
        parent=styles['Body'],
        fontSize=px_to_pt(14),  # 1em
        leading=em_to_pt(1.2),
        spaceBefore=em_to_pt(1),
        spaceAfter=px_to_pt(14),
        textColor=colors['heading6'],
    ))

    # Lists with proper indentation and spacing
    styles.add(ParagraphStyle(
        name='ListItem',
        parent=styles['Body'],
        leftIndent=em_to_pt(1.5),  # Adjusted for better alignment
        bulletIndent=em_to_pt(1),
        spaceBefore=em_to_pt(0.3),  # Tighter list spacing
        spaceAfter=em_to_pt(0.3),
        leading=em_to_pt(1.4),
    ))

    # Blockquote
    styles.add(ParagraphStyle(
        name='Blockquote',
        parent=styles['Body'],
        fontSize=px_to_pt(14),
        leading=em_to_pt(1.4),  # Slightly tighter for quotes
        textColor=colors['text'],
        backColor=colors['blockquote_background'],
        borderLeftWidth=4,  # Slightly thicker border
        borderLeftColor=colors['border'],
        borderPadding=(em_to_pt(0.6), em_to_pt(0.8), em_to_pt(0.6), em_to_pt(1)),
        leftIndent=em_to_pt(1),  # Reduced indent
        rightIndent=em_to_pt(1),
        spaceBefore=em_to_pt(0.8),
        spaceAfter=em_to_pt(0.8),
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

    # Code blocks with VS Code styling
    styles.add(ParagraphStyle(
        name='Code',
        parent=styles['Body'],
        fontName='Courier',  # Standard monospace font
        fontSize=px_to_pt(13),
        leading=em_to_pt(1.357),  # VS Code's exact line height for code
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
        borderPadding=px_to_pt(16),
        leftIndent=px_to_pt(16),
        rightIndent=px_to_pt(16),
        spaceBefore=px_to_pt(8),
        spaceAfter=px_to_pt(8),
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
        borderBottomWidth=2,
        borderBottomColor=colors['border'],
        spaceBefore=px_to_pt(14),
        spaceAfter=px_to_pt(14),
    ))

    return styles