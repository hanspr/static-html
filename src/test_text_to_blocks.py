import unittest
import functions as fn
import textnode as tn

class TestTextToNodes(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """


This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = fn.markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_block_types(self):
        md = """
# Header 1

## Header 2

### Header 3

This is paragraph

```
section of code
with several lines
of text
```

> Quoted text
> Second line of quoted text

- This is an unorderd list
- with items

1. This is an orderd list
1. with some items

"""
        blocks = fn.markdown_to_blocks(md)
        for i, block in enumerate(blocks):
            block_type = fn.block_to_block_type(block)
            if i < 3:
                self.assertEqual(block_type, tn.BlockType.HEADER)
            elif i == 3:
                self.assertEqual(block_type, tn.BlockType.PARAGRAPH)
            elif i == 4:
                self.assertEqual(block_type, tn.BlockType.CODE)
            elif i == 5:
                self.assertEqual(block_type, tn.BlockType.QUOTE)
            elif i == 6:
                self.assertEqual(block_type, tn.BlockType.ULIST)
            elif i == 7:
                self.assertEqual(block_type, tn.BlockType.OLIST)


if __name__ == "__main__":
    unittest.main()
