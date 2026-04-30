import unittest
import functions
import textnode as tn

class TestTextNode(unittest.TestCase):
    def test_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        matches = functions.extract_markdown_images(text)
        self.assertEqual(f"{matches}", r"[('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]")
    
    def test_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        matches = functions.extract_markdown_links(text)
        self.assertEqual(f"{matches}", r"[('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')]")
    
    def test_image_links(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) , This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        matches_i = functions.extract_markdown_images(text)
        matches_l = functions.extract_markdown_links(text)
        self.assertEqual(f"{matches_i}", r"[('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]")
        self.assertEqual(f"{matches_l}", r"[('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')]")
    
    def test_split_images(self):
        node = tn.TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            tn.TextType.TEXT,
        )
        new_nodes = functions.split_nodes_image([node])
        self.assertListEqual(
            [
                tn.TextNode("This is text with an ", tn.TextType.TEXT),
                tn.TextNode("image", tn.TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                tn.TextNode(" and another ", tn.TextType.TEXT),
                tn.TextNode("second image", tn.TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )        

    def test_split_links(self):
        node = tn.TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            tn.TextType.TEXT,
        )
        new_nodes = functions.split_nodes_link([node])
        self.assertListEqual(
            [
                tn.TextNode("This is text with a link ", tn.TextType.TEXT),
                tn.TextNode("to boot dev", tn.TextType.LINK, "https://www.boot.dev"),
                tn.TextNode(" and ", tn.TextType.TEXT),
                tn.TextNode("to youtube", tn.TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            ],
            new_nodes,
        )        

    def test_split_image_and_links(self):
        node = tn.TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png) This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            tn.TextType.TEXT,
        )
        new_nodes = functions.split_nodes_image([node])
        final_nodes = functions.split_nodes_link(new_nodes)
        self.assertListEqual(
            [
                tn.TextNode("This is text with an ", tn.TextType.TEXT),
                tn.TextNode("image", tn.TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                tn.TextNode(" and another ", tn.TextType.TEXT),
                tn.TextNode("second image", tn.TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
                tn.TextNode(" This is text with a link ", tn.TextType.TEXT),
                tn.TextNode("to boot dev", tn.TextType.LINK, "https://www.boot.dev"),
                tn.TextNode(" and ", tn.TextType.TEXT),
                tn.TextNode("to youtube", tn.TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            ],
            final_nodes,
        )        

if __name__ == "__main__":
    unittest.main()
