import os
import sys
import fontforge
from pathlib import Path

def convert_otf_to_ttf(input_dir, output_dir):
    """Convert OTF fonts to TTF format."""
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    for font_file in input_path.glob("*.otf"):
        try:
            # Open the font
            font = fontforge.open(str(font_file))
            
            # Create output filename
            output_file = output_path / font_file.name.replace('.otf', '.ttf')
            
            print(f"Converting {font_file.name} to {output_file.name}")
            
            # Generate TTF
            font.generate(str(output_file))
            font.close()
            
            print(f"✓ Successfully converted to {output_file}")
            
        except Exception as e:
            print(f"Error converting {font_file}: {e}")

if __name__ == "__main__":
    convert_otf_to_ttf("fonts/Renamed", "fonts/TTF") 