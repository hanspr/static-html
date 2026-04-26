import unittest

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
        
if __name__ == "__main__":
    unittest.main()
