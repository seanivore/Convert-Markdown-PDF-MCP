"""Core PDF conversion functionality for markdown to PDF conversion."""

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
from reportlab.lib.styles import ParagraphStyle
from .vscode_styles import get_vscode_stylesheet, em_to_pt, THEME_COLORS
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
    """Download an image to a temporary file."""
    try:
        filename = os.path.join(temp_dir, os.path.basename(url))
        urllib.request.urlretrieve(url, filename)
        return filename
    except (urllib.error.URLError, OSError) as e:
        raise ImageError(f"Failed to download image {url}: {str(e)}")

def get_image_size(image_path: str, max_width: float) -> tuple[float, float]:
    """Calculate image dimensions constrained to max width."""
    try:
        with PILImage.open(image_path) as img:
            orig_width, orig_height = img.size
            if orig_width <= max_width:
                return orig_width, orig_height
            scale_factor = max_width / orig_width
            new_height = orig_height * scale_factor
            return max_width, new_height
    except Exception as e:
        raise ImageError(f"Failed to process image {image_path}: {str(e)}")

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
                
        for nested in child:
            if nested.text:
                if nested.tag == 'strong' or nested.tag == 'b':
                    text += f'<b>{nested.text}</b>'
                elif nested.tag == 'em' or nested.tag == 'i':
                    text += f'<i>{nested.text}</i>'
                else:
                    text += nested.text
            if nested.tail:
                text += nested.tail
                
        if child.tail:
            text += child.tail
            
    return text.strip()

def validate_markdown(text: str) -> None:
    """Validate markdown syntax."""
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
    """Convert markdown to PDF using VS Code styling."""
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            if progress_callback:
                progress_callback(0, "Starting conversion...")
            
            # Handle empty content
            if not markdown_text.strip():
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
            
            # Split content but preserve header and signature newlines
            lines = markdown_text.split('\n')
            processed_lines = []
            in_header = True
            in_signature = False
            
            for line in lines:
                if line.strip() == '':
                    processed_lines.append('')  # Keep empty lines
                    if len(processed_lines) > 4:  # After title, role, blank line, and date
                        in_header = False
                elif in_header:
                    processed_lines.append(line)  # Keep header lines as-is
                elif 'Hope to hear from you soon' in line:  # Start of signature
                    in_signature = True
                    processed_lines.append(line)
                elif in_signature:
                    processed_lines.append(line)  # Preserve signature line breaks
                else:
                    processed_lines.append(line.rstrip())  # Outside header/signature, replace single newlines
            
            processed_text = '\n'.join(processed_lines)
            
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
            
            # Track document sections
            in_header = False
            in_signature = False
            last_was_heading = False
            
            for element in root.iter():
                if element.tag == 'root':
                    continue
                
                if element.tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
                    text = process_inline_text(element)
                    style = f'Heading{element.tag[1]}'
                    elements.append(Paragraph(text, styles[style]))
                    
                    # Update section tracking
                    if element.tag == 'h1':
                        in_header = True
                    else:
                        in_header = False
                    
                    last_was_heading = True
                    
                elif element.tag == 'p':
                    text = process_inline_text(element)
                    
                    # Check for signature section
                    if 'Hope to hear from you soon' in text:
                        in_signature = True
                        
                    # Use special styles for different sections
                    if in_header:
                        if 'ITALICS' in text:  # Date line
                            text = text.replace('ITALICS', '').strip()
                            elements.append(Paragraph(text, styles['Heading3']))
                        else:  # Role line
                            elements.append(Paragraph(text, styles['Heading2']))
                            if last_was_heading:
                                elements.append(Spacer(1, em_to_pt(0.3)))
                    elif in_signature:
                        # Split signature into lines and add each as separate paragraph
                        sig_lines = text.split('\n')
                        for line in sig_lines:
                            if line.strip():
                                elements.append(Paragraph(line.strip(), styles['Signature']))
                    else:
                        elements.append(Paragraph(text, styles['Body']))
                    last_was_heading = False
                    
                elif element.tag == 'ul':
                    list_items = []
                    for li in element.findall('li'):
                        text = process_inline_text(li)
                        if text.strip():
                            list_items.append(Paragraph('• ' + text.strip(), styles['ListItem']))
                    # Add all list items
                    elements.extend(list_items)
                    # Add space after the whole list
                    if list_items:  # Only add space if list wasn't empty
                        elements.append(Spacer(1, em_to_pt(0.8)))
                    last_was_heading = False
                    
                elif element.tag == 'pre':
                    # Handle code blocks properly
                    code = element.find('code')
                    if code is not None:
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
                    last_was_heading = False
                    
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
                    last_was_heading = False
            
            if progress_callback:
                progress_callback(75, "Content processed...")
                
            # Generate PDF
            doc.build(elements)
            
            if progress_callback:
                progress_callback(100, "PDF generated successfully!")
                
            return True
            
    except Exception as e:
        raise PDFGenerationError(f"Failed to generate PDF: {str(e)}") 