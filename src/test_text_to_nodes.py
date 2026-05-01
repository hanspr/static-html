import unittest
import functions
import textnode as tn
import functions as fn

class TestTextToNodes(unittest.TestCase):
    def test_split_image_and_links(self):
        text_node = tn.TextNode(
            "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)",
            tn.TextType.TEXT,
        )
        nodes = fn.split_nodes_image([text_node])
        nodes = fn.split_nodes_link(nodes)
        for delimeter in ("_", "**", "`"):
            nodes = fn.split_nodes_delimeter(nodes, delimeter)
        self.assertListEqual(
            [
                tn.TextNode("This is ", tn.TextType.TEXT),
                tn.TextNode("text", tn.TextType.BOLD),
                tn.TextNode(" with an ", tn.TextType.TEXT),
                tn.TextNode("italic", tn.TextType.ITALIC),
                tn.TextNode(" word and a ", tn.TextType.TEXT),
                tn.TextNode("code block", tn.TextType.CODE),
                tn.TextNode(" and an ", tn.TextType.TEXT),
                tn.TextNode("obi wan image", tn.TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                tn.TextNode(" and a ", tn.TextType.TEXT),
                tn.TextNode("link", tn.TextType.LINK, "https://boot.dev"),
            ],
            nodes,
        )        

if __name__ == "__main__":
    unittest.main()
