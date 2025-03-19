# First, try importing reportlab
try:
    from reportlab.lib import colors
    from reportlab.lib.styles import StyleSheet1, ParagraphStyle
    from reportlab.lib.enums import TA_LEFT
    print("Successfully imported ReportLab!")
except ImportError:
    print("ReportLab is not installed. This is just a style demo.")
    
# Basic style definitions that will work without ReportLab
COLORS = {
    'black': '#000000',
    'white': '#FFFFFF',
    'link_blue': '#0090f1',
    'code_bg': '#1E1E1E',
    'code_text': '#DCDCDC',
    'comment_green': '#57A64A'
}

# Font sizes in points (1pt = 1/72 inch)
SIZES = {
    'body': 11,
    'h1': 32,
    'h2': 24,
    'h3': 18.72,
    'h4': 16,
    'code': 13.5
}

# Demo the styles
print("\nVSCode-style Markdown Settings:")
print("--------------------------------")
print(f"Body text size: {SIZES['body']}pt")
print(f"Heading 1 size: {SIZES['h1']}pt")
print(f"Link color: {COLORS['link_blue']}")
print(f"Code background: {COLORS['code_bg']}")

# If you want to see what a specific style would look like:
style_name = input("\nEnter a style to preview (body, h1, h2, h3, h4, code): ")
if style_name in SIZES:
    print(f"\nStyle '{style_name}':")
    print(f"Font size: {SIZES[style_name]}pt")
    if style_name == 'code':
        print(f"Background color: {COLORS['code_bg']}")
        print(f"Text color: {COLORS['code_text']}")
    else:
        print(f"Text color: {COLORS['black']}")
else:
    print("Style not found!") 