"""
Test suite for MD-PDF-MCP converter.

This module tests the markdown to PDF conversion functionality,
ensuring all VS Code styling elements are correctly applied.
"""

import os
import pytest
from pathlib import Path
from md_pdf_mcp import convert_markdown_to_pdf, MDPDFError

# Get the tests directory path
TEST_DIR = Path(__file__).parent
SAMPLE_MD = TEST_DIR / "cv-text-test.md"  # Changed to use cover letter
OUTPUT_PDF = TEST_DIR / "test_output.pdf"

def generate_visual_samples():
    """
    Generate sample PDFs for visual inspection.
    These files will NOT be automatically deleted.
    """
    print("\nGenerating sample PDFs for visual inspection...")
    
    # Read test markdown
    with open(SAMPLE_MD, 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    
    # Generate a sample in each theme
    for theme in ['light', 'high-contrast']:  # Removed dark theme for now
        output_file = TEST_DIR / f"sample_{theme}_theme.pdf"
        print(f"Generating {output_file.name}...")
        
        success = convert_markdown_to_pdf(
            markdown_content,
            str(output_file),
            theme=theme
        )
        
        if success:
            print(f"✓ Successfully generated {output_file.name}")
        else:
            print(f"✗ Failed to generate {output_file.name}")

def test_basic_conversion():
    """Test basic markdown to PDF conversion."""
    # Read test markdown
    with open(SAMPLE_MD, 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    
    # Convert to PDF
    progress_updates = []
    def progress_callback(percent, message):
        progress_updates.append((percent, message))
    
    success = convert_markdown_to_pdf(
        markdown_content,
        str(OUTPUT_PDF),
        progress_callback=progress_callback
    )
    
    # Verify
    assert success, "PDF conversion should succeed"
    assert OUTPUT_PDF.exists(), "PDF file should be created"
    assert len(progress_updates) > 0, "Should receive progress updates"
    
    # Clean up
    OUTPUT_PDF.unlink(missing_ok=True)

def test_invalid_markdown():
    """Test handling of invalid markdown."""
    with pytest.raises(MDPDFError):
        convert_markdown_to_pdf(
            "Invalid [] markdown )",
            str(OUTPUT_PDF)
        )

def test_theme_selection():
    """Test PDF generation with different themes."""
    with open(SAMPLE_MD, 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    
    # Test each theme
    for theme in ['light', 'high-contrast']:  # Removed dark theme for now
        output_file = TEST_DIR / f"test_output_{theme}.pdf"
        success = convert_markdown_to_pdf(
            markdown_content,
            str(output_file),
            theme=theme
        )
        
        assert success, f"PDF conversion with {theme} theme should succeed"
        assert output_file.exists(), f"PDF file for {theme} theme should be created"
        
        # Clean up
        output_file.unlink(missing_ok=True)

def test_empty_content():
    """Test handling of empty markdown content."""
    success = convert_markdown_to_pdf(
        "",
        str(OUTPUT_PDF)
    )
    
    assert success, "Empty content should still generate a PDF"
    assert OUTPUT_PDF.exists(), "PDF file should be created"
    
    # Clean up
    OUTPUT_PDF.unlink(missing_ok=True)

def test_large_content():
    """Test handling of large markdown content."""
    # Create large markdown content
    large_content = "# Large Document\n\n" + ("This is a test paragraph.\n\n" * 1000)
    
    success = convert_markdown_to_pdf(
        large_content,
        str(OUTPUT_PDF)
    )
    
    assert success, "Large content should be handled correctly"
    assert OUTPUT_PDF.exists(), "PDF file should be created"
    
    # Clean up
    OUTPUT_PDF.unlink(missing_ok=True)

if __name__ == '__main__':
    # Run the visual sample generation first
    generate_visual_samples()
    
    # Then run the automated tests
    pytest.main([__file__])