# Development Guide

## Environment Setup

1. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Unix/macOS
# or
venv\Scripts\activate     # On Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install package in development mode:
```bash
pip install -e .
```

## Running Tests

Run all tests:
```bash
pytest tests/
```

Generate test PDFs (won't be auto-deleted):
```bash
python tests/test_pdf.py
```

## Development Tips

1. The `tests/test_styling.md` file contains examples of all supported markdown elements
2. Visual test PDFs are generated in the tests directory as:
   - `sample_light_theme.pdf`
   - `sample_dark_theme.pdf`
   - `sample_high-contrast_theme.pdf`
3. Use `black` for code formatting:
```bash
black md_pdf_mcp/ tests/
```