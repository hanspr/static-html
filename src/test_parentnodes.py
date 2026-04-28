import unittest

from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    # Validate raises error on missing children
    def test_validate_value(self):
        with self.assertRaises(ValueError):
            node = ParentNode(tag = "a", props = {"href":"https://google.com", "target":"_blank"})

    # Validate raises an error on missing tag
    def test_validate_children(self):
        with self.assertRaises(ValueError):
            node = ParentNode(children = [], props = {"href":"https://google.com", "target":"_blank"})
    
    def test_to_html_one_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", children=[child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    
    def test_to_html_empty_children(self):
        parent_node = ParentNode("div", children=[])
        self.assertEqual(parent_node.to_html(), "<div></div>")
    
    def test_to_html_three_children(self):
        child_one = LeafNode("span", "child")
        child_two = LeafNode("b", "bold text")
        child_three = LeafNode(tag = None, value = "regular text")
        parent_node = ParentNode("div", children=[child_one, child_two, child_three])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span><b>bold text</b>regular text</div>")
    
    def test_to_html_multichild_properties(self):
        child_one = LeafNode("span", "child", props = {"class":"red"})
        child_two = LeafNode("b", "bold text", props = {"class":"flex text-sm"})
        child_three = LeafNode(tag = None, value = "regular text")
        parent_node = ParentNode("div", children=[child_one, child_two, child_three], props = {"style":"color:red;"})
        self.assertEqual(parent_node.to_html(), '<div style="color:red;"><span class="red">child</span><b class="flex text-sm">bold text</b>regular text</div>')
    
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", children=[grandchild_node])
        parent_node = ParentNode("div", children=[child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>")
        
if __name__ == "__main__":
    unittest.main()
