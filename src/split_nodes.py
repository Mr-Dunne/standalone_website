from extract_markdown_images import extract_markdown_images
from extract_markdown_links import extract_markdown_links
from textnode import TextNode
from textnode import TextType

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        matches = extract_markdown_images(node.text)
        if not matches:
            new_nodes.append(node)
            continue
        
        current_text = node.text
        for alt_text, url in matches:
            full_match = f"![{alt_text}]({url})"
            
            # Find the index of the full match
            match_index = current_text.find(full_match)
            if match_index == -1:
                # Should not happen if regex is correct, but a good safeguard
                continue
            
            # Split the text before the image
            text_before = current_text[:match_index]
            if text_before:
                new_nodes.append(TextNode(text_before, TextType.TEXT))
            
            # Add the image node
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            
            # Update the current_text to be the part after the image
            current_text = current_text[match_index + len(full_match):]
        
        # Add any remaining text after the last image
        if current_text:
            new_nodes.append(TextNode(current_text, TextType.TEXT))
    
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        matches = extract_markdown_links(node.text)
        if not matches:
            new_nodes.append(node)
            continue
        
        current_text = node.text
        for link_text, url in matches:
            full_match = f"[{link_text}]({url})"
            
            # Find the index of the full match
            match_index = current_text.find(full_match)
            if match_index == -1:
                # Should not happen
                continue
            
            # Split the text before the link
            text_before = current_text[:match_index]
            if text_before:
                new_nodes.append(TextNode(text_before, TextType.TEXT))
            
            # Add the link node
            new_nodes.append(TextNode(link_text, TextType.LINK, url))
            
            # Update the current_text to be the part after the link
            current_text = current_text[match_index + len(full_match):]
        
        # Add any remaining text after the last link
        if current_text:
            new_nodes.append(TextNode(current_text, TextType.TEXT))
    
    return new_nodes
    