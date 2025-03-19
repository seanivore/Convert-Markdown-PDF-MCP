# Basic Python Styles - No dependencies needed!
# Just copy and run to see how styles look

# Colors in hex (like CSS)
COLORS = {
    # Main colors
    'primary': '#2B579A',      # A nice blue
    'secondary': '#4A9D4A',    # Forest green
    'accent': '#FFB900',       # Warm yellow
    
    # Text colors
    'text_dark': '#333333',    # Almost black
    'text_light': '#FFFFFF',   # White
    'text_gray': '#666666',    # Medium gray
    
    # Background colors
    'bg_light': '#FFFFFF',     # White
    'bg_dark': '#1E1E1E',      # Dark gray (like VSCode)
    'bg_code': '#F5F5F5',      # Light gray for code
}

# Font sizes (in points)
SIZES = {
    'tiny': 8,
    'small': 10,
    'normal': 12,
    'large': 14,
    'xlarge': 18,
    'huge': 24
}

# Spacing (in points)
SPACING = {
    'tight': 4,
    'normal': 8,
    'loose': 12,
    'wide': 16,
    'paragraph': 20
}

# Example styles for different elements
STYLES = {
    'heading1': {
        'font_size': SIZES['huge'],
        'color': COLORS['primary'],
        'spacing_before': SPACING['wide'],
        'spacing_after': SPACING['normal']
    },
    'heading2': {
        'font_size': SIZES['xlarge'],
        'color': COLORS['primary'],
        'spacing_before': SPACING['normal'],
        'spacing_after': SPACING['tight']
    },
    'normal_text': {
        'font_size': SIZES['normal'],
        'color': COLORS['text_dark'],
        'spacing_after': SPACING['normal']
    },
    'code_block': {
        'font_size': SIZES['small'],
        'color': COLORS['text_dark'],
        'background': COLORS['bg_code'],
        'spacing': SPACING['tight']
    },
    'quote': {
        'font_size': SIZES['normal'],
        'color': COLORS['text_gray'],
        'spacing': SPACING['normal'],
        'indent': SPACING['wide']
    }
}

# Let's see how they look!
print("🎨 Python Style Guide Preview:")
print("=============================")

# Show color palette
print("\n📊 Color Palette:")
for name, hex_value in COLORS.items():
    print(f"{name:15} {hex_value}")

# Show text sizes
print("\n📏 Text Sizes:")
for name, size in SIZES.items():
    print(f"{name:10} {size}pt")

# Show example styles
print("\n🎯 Example Styles:")
for element, style in STYLES.items():
    print(f"\n{element}:")
    for property, value in style.items():
        print(f"  {property:15} {value}")

print("\n✨ Ready to make your documents beautiful! ✨") 