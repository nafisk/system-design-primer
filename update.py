import markdown
from pathlib import Path

# Define the paths for the input markdown file and the output HTML file
markdown_file_path = Path('./README.md')
html_file_path = Path('./index.html')

# Read the markdown file
with open(markdown_file_path, 'r', encoding='utf-8') as md_file:
    markdown_text = md_file.read()

# Convert markdown to HTML with the 'tables' extension enabled
html_content = markdown.markdown(markdown_text, extensions=['tables'])

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
        /* Additional styles for table formatting */
        table {{
            border-collapse: collapse;
            width: 100%;
        }}
        th, td {{
            border: 1px solid #dddddd;
            text-align: left;
            padding: 8px;
        }}
        tr:nth-child(even) {{
            background-color: #f2f2f2;
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

print(f"Converted {markdown_file_path} to {html_file_path} with table conversion and specific modifications for level 2 headings and images")
