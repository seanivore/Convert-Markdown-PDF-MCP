# Test Commands Guide

## Initial Setup
Only needed once when first setting up the project:
```bash
# Create virtual environment
python3 -m venv venv

# Activate environment and install package with dev dependencies
source venv/bin/activate && pip install -e ".[dev]"
```

## Running Tests

### Run All Tests
Using pytest (recommended, provides better reporting):
```bash
python -m pytest tests/test_pdf.py
```

Alternative simple method (basic output):
```bash
python tests/test_pdf.py
```

### Generate Visual Samples Only
When working on styling and only need to see PDF output:
```bash
python -c "from tests.test_pdf import generate_visual_samples; generate_visual_samples()"
```

## Output Files
The visual samples will be generated in the `tests/` directory:
- `tests/sample_light_theme.pdf`
- `tests/sample_high-contrast_theme.pdf`

## Notes
- Always ensure the virtual environment is activated before running commands
- The visual samples generator is the fastest way to check styling changes
- Use pytest for actual test development and debugging
- Generated PDFs are not automatically cleaned up - delete old versions manually if needed 