#!/bin/bash

# Create output directory
mkdir -p fonts/TTF

# Convert each OTF file to TTF
for font in fonts/Renamed/*.otf; do
    filename=$(basename "$font")
    output_name="${filename%.otf}.ttf"
    echo "Converting $filename to $output_name"
    fontforge -lang=ff -c "Open(\$1); Generate(\$2)" "$font" "fonts/TTF/$output_name"
done 