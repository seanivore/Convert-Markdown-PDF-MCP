"""
MD-PDF-MCP: VS Code-styled Markdown to PDF converter

This module provides the core functionality for converting markdown documents to PDFs
using VS Code's exact styling through ReportLab's PLATYPUS framework.
"""

import os
import tempfile
import urllib.request
import urllib.error
from pathlib import Path
from typing import Optional, Dict
from urllib.parse import urlparse

import markdown
from xml.etree import ElementTree
from PIL import Image as PILImage
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from .vscode_styles import get_vscode_stylesheet
from markdown.extensions import fenced_code, codehilite, attr_list, tables, toc, extra

class MDPDFError(Exception):
    """Base exception for MD-PDF-MCP"""
    pass

class InvalidMarkdownError(MDPDFError):
    """Raised when markdown cannot be parsed"""
    pass

class PDFGenerationError(MDPDFError):
    """Raised when PDF generation fails"""
    pass

class ImageError(MDPDFError):
    """Raised when image processing fails"""
    pass

def is_url(path: str) -> bool:
    """Check if a path is a URL."""
    try:
        result = urlparse(path)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def download_image(url: str, temp_dir: str) -> str:
    """Download an image to a temporary file.
    
    Args:
        url: The image URL
        temp_dir: Directory to save the image
        
    Returns:
        Path to downloaded image
    """
    try:
        # Create a safe filename from the URL
        filename = os.path.join(temp_dir, os.path.basename(url))
        
        # Download the image
        urllib.request.urlretrieve(url, filename)
        return filename
        
    except (urllib.error.URLError, OSError) as e:
        raise ImageError(f"Failed to download image {url}: {str(e)}")

def get_image_size(image_path: str, max_width: float) -> tuple[float, float]:
    """Calculate image dimensions constrained to max width.
    
    Args:
        image_path: Path to the image
        max_width: Maximum width in points
        
    Returns:
        Tuple of (width, height) in points
    """
    try:
        with PILImage.open(image_path) as img:
            # Get original dimensions
            orig_width, orig_height = img.size
            
            # If image is smaller than max width, use original size
            if orig_width <= max_width:
                return orig_width, orig_height
                
            # Scale height proportionally
            scale_factor = max_width / orig_width
            new_height = orig_height * scale_factor
            
            return max_width, new_height
            
    except Exception as e:
        raise ImageError(f"Failed to process image {image_path}: {str(e)}")

def process_inline_text(element) -> str:
    """Process inline text formatting (bold, italic, etc.)"""
    if element.text is None:
        return ''
        
    text = element.text
    
    # Process all child elements in order
    for child in element:
        # Handle line breaks
        if child.tag == 'br':
            text += "<br/>"
            continue
            
        # Handle text before any nested elements
        if child.text:
            if child.tag == 'strong':
                text += f"<b>{child.text}</b>"
            elif child.tag == 'em':
                text += f"<i>{child.text}</i>"
            else:
                text += child.text
                
        # Handle nested elements
        for nested in child:
            if nested.text:
                if nested.tag == 'strong':
                    text += f"<b>{nested.text}</b>"
                elif nested.tag == 'em':
                    text += f"<i>{nested.text}</i>"
                elif nested.tag == 'br':
                    text += "<br/>"
                else:
                    text += nested.text
            if nested.tail:
                text += nested.tail
                
        # Handle text after nested elements
        if child.tail:
            text += child.tail
            
    # Clean up line breaks
    text = text.replace("<br/><br/>", "<br/>")
    text = text.replace("<br/>", " ")  # Convert line breaks to spaces
            
    return text.strip()  # Remove extra whitespace

def validate_markdown(text: str) -> None:
    """
    Validate markdown syntax.
    Raises InvalidMarkdownError if the markdown is invalid.
    """
    # Check for unmatched brackets
    stack = []
    for i, char in enumerate(text):
        if char in '[(':
            stack.append((char, i))
        elif char in '])':
            if not stack:
                raise InvalidMarkdownError(f"Unmatched closing bracket at position {i}")
            last_char, _ = stack.pop()
            if (char == ']' and last_char != '[') or (char == ')' and last_char != '('):
                raise InvalidMarkdownError(f"Mismatched brackets at position {i}")
    if stack:
        pos = stack[-1][1]
        raise InvalidMarkdownError(f"Unclosed bracket at position {pos}")

def convert_markdown_to_pdf(
    markdown_text: str,
    output_path: str,
    theme: str = 'light',
    progress_callback: Optional[callable] = None
) -> bool:
    """
    Convert markdown to PDF using VS Code styling.
    
    Args:
        markdown_text: The markdown content to convert
        output_path: Where to save the PDF
        theme: VS Code theme to use ('light', 'dark', or 'high-contrast')
        progress_callback: Optional function to report progress
        
    Returns:
        bool: True if conversion successful
    
    Raises:
        PDFGenerationError: If conversion fails
    """
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            if progress_callback:
                progress_callback(0, "Starting conversion...")
            
            # Handle empty content
            if not markdown_text.strip():
                # Create an empty PDF with just the styles
                doc = SimpleDocTemplate(
                    output_path,
                    pagesize=A4,
                    rightMargin=72,
                    leftMargin=72,
                    topMargin=72,
                    bottomMargin=72
                )
                doc.build([])
                return True
            
            # Split content by double newlines to handle paragraphs better
            paragraphs = markdown_text.split('\n\n')
            processed_text = '\n\n'.join(p.replace('\n', ' ') for p in paragraphs)
            
            # Validate markdown syntax
            validate_markdown(processed_text)
            
            try:
                # Parse markdown to HTML with extensions
                html = markdown.markdown(
                    processed_text,
                    extensions=[
                        'fenced_code',
                        'codehilite',
                        'attr_list',
                        'tables',
                        'toc',
                        'extra',
                    ],
                    output_format='xhtml'
                )
            except Exception as e:
                raise InvalidMarkdownError(f"Failed to parse markdown: {str(e)}")
            
            # Empty HTML is fine - it means valid but empty markdown
            if progress_callback:
                progress_callback(25, "Markdown parsed...")
                
            # Create PDF document with styles
            doc = SimpleDocTemplate(
                output_path,
                pagesize=A4,
                rightMargin=72,
                leftMargin=72,
                topMargin=72,
                bottomMargin=72
            )
            
            page_width = A4[0] - 144  # Width minus margins
            styles = get_vscode_stylesheet(theme)
            
            if progress_callback:
                progress_callback(50, "Styles applied...")
                
            # Convert HTML to flowables
            elements = []
            try:
                root = ElementTree.fromstring(f"<root>{html}</root>")
            except ElementTree.ParseError as e:
                raise InvalidMarkdownError(f"Generated HTML is invalid: {str(e)}")
            
            for element in root.iter():
                if element.tag == 'root':
                    continue
                    
                if element.tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
                    style = f'Heading{element.tag[1]}'
                    text = process_inline_text(element)
                    elements.append(Paragraph(text, styles[style]))
                    
                elif element.tag == 'p':
                    text = process_inline_text(element)
                    elements.append(Paragraph(text, styles['Body']))
                    
                elif element.tag == 'pre':
                    # Handle code blocks properly
                    code = element.find('code')
                    if code is not None:
                        # Get language class if specified
                        classes = code.get('class', '').split()
                        lang = next((c.replace('language-', '') for c in classes if c.startswith('language-')), '')
                        
                        # Get the code text
                        text = code.text.strip('`') if code.text else ''
                        
                        # Split into lines and process each line
                        lines = text.split('\n')
                        processed_lines = []
                        
                        for line in lines:
                            line = line.rstrip()  # Remove trailing whitespace
                            if line.lstrip().startswith('#'):  # Python comment
                                processed_lines.append(Paragraph(line, styles['CodeComment']))
                            else:
                                processed_lines.append(Paragraph(line, styles['Pre']))
                        
                        elements.extend(processed_lines)
                    else:
                        text = element.text.strip('`') if element.text else ''
                        elements.append(Paragraph(text, styles['Pre']))
                    
                elif element.tag == 'blockquote':
                    # Only process the first paragraph in the blockquote to avoid duplication
                    p_elements = element.findall('p')
                    if p_elements:
                        text = process_inline_text(p_elements[0])
                    else:
                        text = process_inline_text(element)
                    elements.append(Paragraph(text, styles['Blockquote']))
                    
                elif element.tag == 'hr':
                    elements.append(Spacer(1, inch/4))
                    
                elif element.tag == 'img':
                    src = element.get('src')
                    if not src:
                        continue
                        
                    # Handle remote images
                    if is_url(src):
                        try:
                            src = download_image(src, temp_dir)
                        except ImageError as e:
                            print(f"Warning: Failed to download image {src}: {e}")
                            continue
                    
                    # Calculate image size
                    try:
                        width, height = get_image_size(src, page_width)
                        image = Image(src, width=width, height=height)
                        elements.append(image)
                    except ImageError as e:
                        print(f"Warning: Failed to process image {src}: {e}")
                        continue
            
            if progress_callback:
                progress_callback(75, "Content processed...")
                
            # Generate PDF
            doc.build(elements)
            
            if progress_callback:
                progress_callback(100, "PDF generated successfully!")
                
            return True
            
    except Exception as e:
        raise PDFGenerationError(f"Failed to generate PDF: {str(e)}")
