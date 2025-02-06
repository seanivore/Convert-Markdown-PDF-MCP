"""VS Code Markdown Style Implementation for ReportLab PLATYPUS

This module provides an exact implementation of VS Code's markdown styling for ReportLab's
PLATYPUS (Page Layout and Typography Using Scripts) system. It converts VS Code's CSS to 
ReportLab's ParagraphStyle while maintaining precise visual fidelity.
"""

from reportlab.lib import colors
from reportlab.lib.styles import StyleSheet1, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT, TA_CENTER

# Utility functions for unit conversion
def px_to_pt(px: float) -> float:
    """Convert pixels to points (1px = 0.75pt)"""
    return px * 0.75

def em_to_pt(em: float, base_size: float = 14) -> float:
    """Convert em to points based on base font size"""
    return em * base_size

# VS Code's font stack with ReportLab fallbacks
FONT_STACK = {
    'default': [
        '-apple-system',
        'BlinkMacSystemFont', 
        'Segoe WPC',
        'Segoe UI', 
        'system-ui', 
        'Ubuntu',
        'Droid Sans',
        'sans-serif'
    ],
    'monospace': [
        'SF Mono',
        'Monaco',
        'Menlo',
        'Consolas',
        'Ubuntu Mono',
        'Liberation Mono',
        'DejaVu Sans Mono',
        'Courier New',
        'monospace'
    ]
}

# VS Code's exact colors
THEME_COLORS = {
    'light': {
        'text': colors.black,
        'border': colors.Color(0, 0, 0, alpha=0.18),
        'table_border': colors.Color(0, 0, 0, alpha=0.69),
        'link': colors.HexColor('#0090f1'),
        'pre_background': colors.Color(220/255, 220/255, 220/255, alpha=0.4),
        'heading6': colors.gray
    },
    'dark': {
        'text': colors.white,
        'border': colors.Color(1, 1, 1, alpha=0.18),
        'table_border': colors.Color(1, 1, 1, alpha=0.69),
        'link': colors.HexColor('#0090f1'),
        'pre_background': colors.Color(10/255, 10/255, 10/255, alpha=0.4),
        'heading6': colors.gray
    },
    'high-contrast': {
        'text': colors.black,
        'border': colors.black,
        'table_border': colors.black,
        'link': colors.HexColor('#0090f1'),
        'pre_background': colors.black,
        'heading6': colors.gray
    }
}

def get_vscode_stylesheet(theme: str = 'light') -> StyleSheet1:
    """Generate a ReportLab StyleSheet matching VS Code's markdown styling.
    
    Args:
        theme: Either 'light', 'dark', or 'high-contrast' to match VS Code's themes
        
    Returns:
        A StyleSheet1 instance with all necessary styles defined
    """
    styles = StyleSheet1()
    colors = THEME_COLORS[theme]
    
    # Base style (VS Code body)
    styles.add(ParagraphStyle(
        name='Body',
        fontName='Helvetica',
        fontSize=px_to_pt(14),  # VS Code's 14px
        leading=em_to_pt(1.6),  # VS Code's line-height: 1.6
        textColor=colors['text'],
        alignment=TA_LEFT,
        spaceAfter=px_to_pt(14),
    ))

    # Heading 1
    styles.add(ParagraphStyle(
        name='Heading1',
        parent=styles['Body'],
        fontSize=px_to_pt(28),  # 2em
        leading=em_to_pt(1.2),
        spaceBefore=px_to_pt(21),
        spaceAfter=em_to_pt(0.3),
        borderColor=colors['border'],
        borderWidth=1,
        borderPadding=0,
    ))

    # Headings 2-6
    styles.add(ParagraphStyle(
        name='Heading2',
        parent=styles['Body'],
        fontSize=px_to_pt(21),  # 1.5em
        leading=em_to_pt(1.2),
        spaceBefore=em_to_pt(2),
        spaceAfter=px_to_pt(14),
    ))

    styles.add(ParagraphStyle(
        name='Heading3',
        parent=styles['Body'],
        fontSize=px_to_pt(17.5),  # 1.25em
        leading=em_to_pt(1.2),
        spaceBefore=em_to_pt(1.5),
        spaceAfter=px_to_pt(14),
    ))

    styles.add(ParagraphStyle(
        name='Heading4',
        parent=styles['Body'],
        fontSize=px_to_pt(15.4),  # 1.1em
        leading=em_to_pt(1.2),
        spaceBefore=em_to_pt(1.25),
        spaceAfter=px_to_pt(14),
    ))

    styles.add(ParagraphStyle(
        name='Heading5',
        parent=styles['Body'],
        fontSize=px_to_pt(14),  # 1em
        leading=em_to_pt(1.2),
        spaceBefore=em_to_pt(1),
        spaceAfter=px_to_pt(14),
    ))

    styles.add(ParagraphStyle(
        name='Heading6',
        parent=styles['Body'],
        fontSize=px_to_pt(14),  # 1em
        leading=em_to_pt(1.2),
        spaceBefore=em_to_pt(1),
        spaceAfter=px_to_pt(14),
        textColor=colors['heading6'],
    ))

    # Blockquotes
    styles.add(ParagraphStyle(
        name='Blockquote',
        parent=styles['Body'],
        leftIndent=px_to_pt(5),
        rightIndent=px_to_pt(7),
        spaceBefore=0,
        spaceAfter=0,
        borderWidth=px_to_pt(5),
        borderPadding=px_to_pt(10),
        borderColor=colors['border'],
        textColor=colors['text'],
    ))

    # Code blocks
    styles.add(ParagraphStyle(
        name='Code',
        parent=styles['Body'],
        fontName='Courier',
        fontSize=px_to_pt(14),
        leading=em_to_pt(1.357),
        textColor=colors['text'],
    ))

    styles.add(ParagraphStyle(
        name='Pre',
        parent=styles['Code'],
        backColor=colors['pre_background'],
        borderPadding=px_to_pt(16),
    ))

    # Links
    styles.add(ParagraphStyle(
        name='Link',
        parent=styles['Body'],
        textColor=colors['link'],
        underline=1,
    ))

    # Lists
    styles.add(ParagraphStyle(
        name='ListItem',
        parent=styles['Body'],
        leftIndent=px_to_pt(24),
        spaceBefore=px_to_pt(4),
        spaceAfter=px_to_pt(4),
    ))

    # Tables
    styles.add(ParagraphStyle(
        name='TableHeader',
        parent=styles['Body'],
        backColor=colors['pre_background'],
        borderColor=colors['table_border'],
        borderWidth=1,
        borderPadding=px_to_pt(6),
        alignment=TA_LEFT,
    ))

    styles.add(ParagraphStyle(
        name='TableCell',
        parent=styles['Body'],
        borderColor=colors['table_border'],
        borderWidth=1,
        borderPadding=px_to_pt(6),
        alignment=TA_LEFT,
    ))

    # Images
    styles.add(ParagraphStyle(
        name='Image',
        parent=styles['Body'],
        alignment=TA_CENTER,
        spaceBefore=px_to_pt(14),
        spaceAfter=px_to_pt(14),
    ))

    return styles