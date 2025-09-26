from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r') as md_file:
        markdown_content = md_file.read()
    with open(template_path, 'r') as tmp_file:
        template_content = tmp_file.read()

    html_content = markdown_to_html_node(markdown_content).to_html()
    title = extract_title(markdown_content)

    final_html = template_content.replace("{{ Title }}", title)
    final_html = final_html.replace("{{ Content }}", html_content)

    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    with open(dest_path, 'w') as dest_file:
        dest_file.write(final_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    """
    Recursively generates HTML pages from markdown files in a directory.

    Args:
        dir_path_content: The root directory containing markdown files (e.g., 'content/').
        template_path: The path to the HTML template file.
        dest_dir_path: The destination directory for the generated HTML files (e.g., 'public/').
    """
    if not os.path.exists(dir_path_content):
        raise FileNotFoundError(f"Source directory does not exist: {dir_path_content}")
    
    print(f"Generating pages from {dir_path_content} to {dest_dir_path}")
    
    # Use os.walk to traverse the directory tree
    for dirpath, dirnames, filenames in os.walk(dir_path_content):
        # Calculate the relative path from the source to the current directory
        relative_path = os.path.relpath(dirpath, dir_path_content)
        current_dest_dir = os.path.join(dest_dir_path, relative_path)
        
        # Ensure the corresponding destination directory exists
        if not os.path.exists(current_dest_dir):
            os.makedirs(current_dest_dir)
            
        # Process each markdown file in the current directory
        for filename in filenames:
            if filename.endswith(".md"):
                from_path = os.path.join(dirpath, filename)
                
                # Create the destination path with a .html extension
                dest_filename = os.path.splitext(filename)[0] + ".html"
                dest_filepath = os.path.join(current_dest_dir, dest_filename)
                
                # Call your existing generate_page function
                generate_page(from_path, template_path, dest_filepath)