import unittest
import htmlnode

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_ne(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("Another text", TextType.BOLD)
        self.assertNotEqual(node, node2)
        
    def test_url_notnone(self):
        node = TextNode("This is a text node", TextType.LINK, "http://x.com")
        self.assertNotEqual(node.url, None)

    def test_text(self):
        node = TextNode("utf8=áéíóúÑ-ñ", TextType.LINK, "http://x.com")
        self.assertEqual(node.text, "utf8=áéíóúÑ-ñ")
        
    def test_text2html_node(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = htmlnode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_bold2html_node(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = htmlnode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")
    
    def test_italic2html_node(self):
        node = TextNode("This is italic", TextType.ITALIC)
        html_node = htmlnode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is italic")
        
    def test_code2html_node(self):
        node = TextNode("This is code", TextType.CODE)
        html_node = htmlnode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is code")
        
    def test_link2html_node(self):
        node = TextNode("This is a link", TextType.LINK, "http://google.com")
        html_node = htmlnode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link")
        self.assertEqual(html_node.props["href"], "http://google.com")
        
    def test_img2html_node(self):
        node = TextNode("my image alt", TextType.IMAGE, "http://domina.com/images/image.png")
        html_node = htmlnode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props["alt"], "my image alt")
        self.assertEqual(html_node.props["src"], "http://domina.com/images/image.png")
        
if __name__ == "__main__":
    unittest.main()
