import unittest
import htmlnode

from textnode import TextNode, TextType, split_nodes_delimeter

class TestTextNode(unittest.TestCase):
    def test_split_node_error(self):
        node = TextNode("This is a _text node", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimeter(node, "_", node.text_type)
    
    def test_split_not_TEXT(self):
        node = TextNode("This is a _italic text_ node", TextType.CODE)
        new_nodes = split_nodes_delimeter(node, "_", node.text_type)
        self.assertEqual(node, new_nodes[0])
        
    def test_split_italic(self):
        node = TextNode("This is a _italic text_ node", TextType.TEXT)
        new_nodes = split_nodes_delimeter(node, "_", node.text_type)
        self.assertEqual(f"{new_nodes[0]!r}", 'TextNode(This is a ,TEXT,None)')
        self.assertEqual(f"{new_nodes[1]!r}", 'TextNode(italic text,ITALIC,None)')
        self.assertEqual(f"{new_nodes[2]!r}", 'TextNode( node,TEXT,None)')
            
    def test_split_bold(self):
        node = TextNode("This is a **bold text** node", TextType.TEXT)
        new_nodes = split_nodes_delimeter(node, "**", node.text_type)
        self.assertEqual(f"{new_nodes[0]!r}", 'TextNode(This is a ,TEXT,None)')
        self.assertEqual(f"{new_nodes[1]!r}", 'TextNode(bold text,BOLD,None)')
        self.assertEqual(f"{new_nodes[2]!r}", 'TextNode( node,TEXT,None)')
            
    def test_split_multi_bold(self):
        node = TextNode("This **is** a multi **bold text** node", TextType.TEXT)
        new_nodes = split_nodes_delimeter(node, "**", node.text_type)
        self.assertEqual(f"{new_nodes[0]!r}", 'TextNode(This ,TEXT,None)')
        self.assertEqual(f"{new_nodes[1]!r}", 'TextNode(is,BOLD,None)')
        self.assertEqual(f"{new_nodes[2]!r}", 'TextNode( a multi ,TEXT,None)')
        self.assertEqual(f"{new_nodes[3]!r}", 'TextNode(bold text,BOLD,None)')
        self.assertEqual(f"{new_nodes[4]!r}", 'TextNode( node,TEXT,None)')
            
if __name__ == "__main__":
    unittest.main()
