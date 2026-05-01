import unittest
import htmlnode as hn
import textnode as tn
import functions as fn

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = tn.TextNode("This is a text node", tn.TextType.BOLD)
        node2 = tn.TextNode("This is a text node", tn.TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_ne(self):
        node = tn.TextNode("This is a text node", tn.TextType.BOLD)
        node2 = tn.TextNode("Another text", tn.TextType.BOLD)
        self.assertNotEqual(node, node2)
        
    def test_url_notnone(self):
        node = tn.TextNode("This is a text node", tn.TextType.LINK, "http://x.com")
        self.assertNotEqual(node.url, None)

    def test_text(self):
        node = tn.TextNode("utf8=áéíóúÑ-ñ", tn.TextType.LINK, "http://x.com")
        self.assertEqual(node.text, "utf8=áéíóúÑ-ñ")
        
    def test_text2html_node(self):
        node = tn.TextNode("This is a text node", tn.TextType.TEXT)
        html_node = fn.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_bold2html_node(self):
        node = tn.TextNode("This is bold", tn.TextType.BOLD)
        html_node = fn.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")
    
    def test_italic2html_node(self):
        node = tn.TextNode("This is italic", tn.TextType.ITALIC)
        html_node = fn.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is italic")
        
    def test_code2html_node(self):
        node = tn.TextNode("This is code", tn.TextType.CODE)
        html_node = fn.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is code")
        
    def test_link2html_node(self):
        node = tn.TextNode("This is a link", tn.TextType.LINK, "http://google.com")
        html_node = fn.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link")
        self.assertEqual(html_node.props["href"], "http://google.com")
        
    def test_img2html_node(self):
        node = tn.TextNode("my image alt", tn.TextType.IMAGE, "http://domina.com/images/image.png")
        html_node = fn.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props["alt"], "my image alt")
        self.assertEqual(html_node.props["src"], "http://domina.com/images/image.png")
        
if __name__ == "__main__":
    unittest.main()
