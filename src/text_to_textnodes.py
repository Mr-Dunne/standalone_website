from textnode import TextNode, TextType
from split_nodes import *
from split_nodes_delimiter import split_nodes_delimiter
from text_node_to_html_node import text_node_to_html_node


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    
    # 1. Split for images and links first
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    # 2. Then, split for markdown delimiters
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    
    return nodes


def text_to_children(text):
    cleaned_text = text.replace("\n", " ")
    text_nodes = text_to_textnodes(cleaned_text)
    html_nodes = [text_node_to_html_node(node) for node in text_nodes]
    return html_nodes