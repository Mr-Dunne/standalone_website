import unittest
from blocktype import block_to_block_type, BlockType

class TestBlockToBlockType(unittest.TestCase):
    def test_paragraph(self):
        block = "This is a simple paragraph."
        self.assertEqual(block_to_block_type(block), BlockType.paragraph)

    def test_heading_h1(self):
        block = "# This is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.heading)

    def test_heading_h6(self):
        block = "###### This is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.heading)

    def test_code_block(self):
        block = "```\nprint('Hello, world!')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.code)

    def test_quote_block(self):
        block = "> This is a quote\n> with multiple lines."
        self.assertEqual(block_to_block_type(block), BlockType.quote)
    
    def test_unordered_list(self):
        block = "- item 1\n- item 2\n- item 3"
        self.assertEqual(block_to_block_type(block), BlockType.unordered_list)

    def test_ordered_list(self):
        block = "1. First item\n2. Second item\n3. Third item"
        self.assertEqual(block_to_block_type(block), BlockType.ordered_list)

    def test_mismatched_ordered_list(self):
        block = "1. First item\n3. Second item"
        self.assertEqual(block_to_block_type(block), BlockType.paragraph)
    
    def test_invalid_quote_block(self):
        block = "> This is a quote\nThis is not a quote."
        self.assertEqual(block_to_block_type(block), BlockType.paragraph)

    def test_invalid_unordered_list(self):
        block = "- This is a list\n* This is not"
        self.assertEqual(block_to_block_type(block), BlockType.paragraph)

    def test_code_block_without_end(self):
        block = "```\nprint('code')"
        self.assertEqual(block_to_block_type(block), BlockType.paragraph)

    def test_heading_invalid(self):
        block = "####### This is not a heading"
        self.assertEqual(block_to_block_type(block), BlockType.paragraph)

    def test_heading_no_space(self):
        block = "###No space"
        self.assertEqual(block_to_block_type(block), BlockType.paragraph)

if __name__ == "__main__":
    unittest.main()