import markdown
import re
from pathlib import Path

# Define the paths for the input markdown file and the output HTML file
markdown_file_path = Path('./readme.md')
html_file_path = Path('./index.html')

# Read the markdown file
with open(markdown_file_path, 'r', encoding='utf-8') as md_file:
    markdown_text = md_file.read()

# Use regex to precisely add <br/><br/><br/><hr> before ## (level 2 headings)
# The regex looks for a newline followed by exactly two # characters and a space, ensuring it matches only level 2 headings
processed_markdown_text = re.sub(r'(?<!#)\n(## )', r'\n<br/><br/><br/><hr>\n\1', markdown_text)

# Convert markdown to HTML
html_content = markdown.markdown(processed_markdown_text)

# Define an HTML template with styles for max-width for both the body and img tags
html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        body {{
            max-width: 800px;
            margin: auto;
            padding: 20px;
        }}
        img {{
            max-width: 100%;
            height: auto;
        }}
    </style>
</head>
<body>
{html_content}
</body>
</html>
"""

# Write the HTML to a new file
with open(html_file_path, 'w', encoding='utf-8') as html_file:
    html_file.write(html_template)

print(f"Converted {markdown_file_path} to {html_file_path} with specific modifications for level 2 headings and images")
