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
        # Create temporary directory for downloaded images
        with tempfile.TemporaryDirectory() as temp_dir:
            if progress_callback:
                progress_callback(0, "Starting conversion...")
            
            # 1. Parse markdown to HTML
            html = markdown.markdown(markdown_text)
            
            if progress_callback:
                progress_callback(25, "Markdown parsed...")
                
            # 2. Create PDF document with styles
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
                
            # 3. Convert HTML to flowables
            elements = []
            root = ElementTree.fromstring(f"<root>{html}</root>")
            
            for element in root.iter():
                if element.tag == 'root':
                    continue
                    
                if element.tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
                    style = f'Heading{element.tag[1]}'
                    elements.append(Paragraph(element.text or '', styles[style]))
                    
                elif element.tag == 'p':
                    elements.append(Paragraph(element.text or '', styles['Body']))
                    
                elif element.tag == 'pre':
                    elements.append(Paragraph(element.text or '', styles['Pre']))
                    
                elif element.tag == 'blockquote':
                    elements.append(Paragraph(element.text or '', styles['Blockquote']))
                    
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
                
            # 4. Generate PDF
            doc.build(elements)
            
            if progress_callback:
                progress_callback(100, "PDF generated successfully!")
                
            return True
            
    except Exception as e:
        raise PDFGenerationError(f"Failed to generate PDF: {str(e)}")
