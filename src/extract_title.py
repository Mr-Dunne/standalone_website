

def extract_title(markdown):
    lines = markdown.split('\n')
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    
    raise ValueError("Markdown file must have a single H1 heading.")