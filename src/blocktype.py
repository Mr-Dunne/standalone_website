import re
from enum import Enum

class BlockType(Enum):
    paragraph = 'paragraph'
    heading = 'heading'
    code = 'code'
    quote = 'quote'
    unordered_list = 'unordered list'
    ordered_list = 'ordered list'

def block_to_block_type(block):
    lines = block.split('\n')

    # Check for a heading (H1-H6)
    if re.match(r"^#{1,6}\s", block):
        return BlockType.heading
    
    # Check for a code block (must start and end with ```)
    if block.startswith("```") and block.endswith("```"):
        return BlockType.code
    
    # Check for a quote block (every single line must start with >)
    is_quote = all(line.startswith('>') for line in lines)
    if is_quote:
        return BlockType.quote
    
    # Check for an unordered list (every single line must start with - or *)
    is_unordered_list = True
    for line in lines:
        if not (line.startswith('- ') or line.startswith('* ')):
            is_unordered_list = False
            break
    if is_unordered_list:
        return BlockType.unordered_list

    # Check for an ordered list (every single line must be a sequential number)
    is_ordered_list = True
    expected_number = 1
    for line in lines:
        match = re.match(r"^(\d+)\.\s", line)
        if not match or int(match.group(1)) != expected_number:
            is_ordered_list = False
            break
        expected_number += 1
    
    if is_ordered_list:
        return BlockType.ordered_list
    
    # If none of the above conditions are met, it's a paragraph
    return BlockType.paragraph