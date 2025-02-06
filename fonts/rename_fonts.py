import os
from fontTools import ttLib
from pathlib import Path

font_dir = Path("fonts/Need Names Hidden")
output_dir = Path("fonts/Renamed")
output_dir.mkdir(exist_ok=True)

def get_font_name(font_path):
    try:
        font = ttLib.TTFont(font_path)
        names = font["name"].names
        family = next((n.string.decode(n.getEncoding()) if isinstance(n.string, bytes) else n.string 
                      for n in names if n.nameID == 1), "Unknown")
        style = next((n.string.decode(n.getEncoding()) if isinstance(n.string, bytes) else n.string 
                     for n in names if n.nameID == 2), "Regular")
        return f"{family}-{style}.otf"
    except Exception as e:
        print(f"Error processing {font_path}: {e}")
        return None

for font_file in font_dir.glob(".*otf"):
    if font_file.name.startswith("."):
        new_name = get_font_name(font_file)
        if new_name:
            print(f"Renaming {font_file.name} to {new_name}")
            new_path = output_dir / new_name
            try:
                import shutil
                shutil.copy2(font_file, new_path)
                print(f"✓ Successfully copied to {new_path}")
            except Exception as e:
                print(f"Error copying {font_file}: {e}") 