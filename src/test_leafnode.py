import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    # Test html format strings
    def test_anchor(self):
        node = LeafNode(tag = "a", value = "click me!", props = {"href":"https://google.com", "target":"_blank"})
        self.assertEqual(node.to_html(), '<a href="https://google.com" target="_blank">click me!</a>')
    
    def test_bold(self):
        node = LeafNode(tag = "b", value = "letra en negritas")
        self.assertEqual(node.to_html(), '<b>letra en negritas</b>')
        
    def test_text(self):
        node = LeafNode(value = "letra sin formato")
        self.assertEqual(node.to_html(), 'letra sin formato')
        
    # Validate raises error on missing value
    def test_validate_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode(tag = "a", props = {"href":"https://google.com", "target":"_blank"})

    # Validate raises an error on children parameter
    def test_validate_children(self):
        with self.assertRaises(TypeError):
            node = LeafNode(tag = "a", children = None, props = {"href":"https://google.com", "target":"_blank"})
        
if __name__ == "__main__":
    unittest.main()
