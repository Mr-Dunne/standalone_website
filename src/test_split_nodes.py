import unittest
from textnode import TextNode
from textnode import TextType
from split_nodes import *

class TestMarkdown(unittest.TestCase):
    # Your existing setup from previous steps
    def setUp(self):
        self.maxDiff = None
        # This allows you to see the full diff if a test fails

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes,
        )

    def test_image_at_start(self):
        node = TextNode("![image](https://i.imgur.com/zjjcJKZ.png) at the start", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" at the start", TextType.TEXT),
            ],
            new_nodes,
        )
    
    def test_image_at_end(self):
        node = TextNode("Image at the end ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Image at the end ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_multiple_nodes_image(self):
        node1 = TextNode("Text with an ![image](https://example.com/a.png)", TextType.TEXT)
        node2 = TextNode("More text with a ![second image](https://example.com/b.png)", TextType.TEXT)
        new_nodes = split_nodes_image([node1, node2])
        self.assertListEqual(
            [
                TextNode("Text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://example.com/a.png"),
                TextNode("More text with a ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://example.com/b.png"),
            ],
            new_nodes,
        )

    def test_no_links(self):
        node = TextNode("This text has no links.", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This text has no links.", TextType.TEXT),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()