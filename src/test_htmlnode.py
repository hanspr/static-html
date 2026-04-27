import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(tag = "a", value = "liga", props = {"href":"https://google.com", "target":"_blank"})
        self.assertEqual(node.children, None)
    
    def test_notimplemented(self):
        obj = HTMLNode(tag = "a", value = "liga", children = None, props = {"href":"https://google.com", "target":"_blank"})
        with self.assertRaises(NotImplementedError):
            obj.to_html()
        
    def test_props(self):
        node = HTMLNode(tag = "a", value = "liga", children = None, props = {"href":"https://google.com", "target":"_blank"})
        self.assertEqual(node.props_to_html(), " href=\"https://google.com\" target=\"_blank\"")
        
if __name__ == "__main__":
    unittest.main()
