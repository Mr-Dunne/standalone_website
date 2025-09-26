from textnode import TextNode
from textnode import TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
    
        parts = node.text.split(delimiter)

        if len(parts) % 2 == 0:
            print(f"DEBUG: Problematic text: '{node.text}'") 
            raise ValueError(f"Invalid markdown: A closing delimiter '{delimiter}' is missing.")
        
        for num, segment in enumerate(parts):
            if num % 2 == 0:
                if segment:
                    new_nodes.append(TextNode(segment, TextType.TEXT))
            else:
                new_nodes.append(TextNode(segment, text_type))
    
    return new_nodes

node = TextNode("This is text with a `code block` word", TextType.TEXT)
new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

print(new_nodes)