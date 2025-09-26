from markdown_to_blocks import markdown_to_blocks
from blocktype import block_to_block_type
from htmlnode import HTMLNode
from blocktype import BlockType
from text_to_textnodes import text_to_children
import re


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    parent_node = HTMLNode("div", children=[])

    for block in blocks:
        block_type = block_to_block_type(block)
        html_node = None
        
        if block_type == BlockType.paragraph:
            # text_to_children now handles the newline replacement
            children = text_to_children(block) 
            html_node = HTMLNode("p", children=children)
        
        # ... (rest of the block type checks are the same)
        # Note: Code blocks are handled separately and bypass text_to_children,
        # so their newlines are preserved as required.
        
        elif block_type == BlockType.heading:
            level = len(re.match(r"^#+", block).group(0))
            children = text_to_children(block.lstrip('#').lstrip())
            html_node = HTMLNode(f"h{level}", children=children)
            
        elif block_type == BlockType.code:
            content = block.strip('`').lstrip()
            code_node = HTMLNode("code", value=content)
            html_node = HTMLNode("pre", children=[code_node])
        
        elif block_type == BlockType.quote:
            lines = [line.lstrip('>').lstrip() for line in block.split('\n')]
            content = "\n".join(lines)
            children = text_to_children(content)
            html_node = HTMLNode("blockquote", children=children)
            
        elif block_type == BlockType.unordered_list:
            list_items = []
            for item in block.split('\n'):
                item_content = item.lstrip('- ')
                children = text_to_children(item_content)
                list_items.append(HTMLNode("li", children=children))
            html_node = HTMLNode("ul", children=list_items)
            
        elif block_type == BlockType.ordered_list:
            list_items = []
            for item in block.split('\n'):
                item_content = re.match(r"^\d+\.\s(.*)", item).group(1)
                children = text_to_children(item_content)
                list_items.append(HTMLNode("li", children=children))
            html_node = HTMLNode("ol", children=list_items)

        if html_node:
            parent_node.children.append(html_node)
    
    return parent_node