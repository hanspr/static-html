import unittest
import functions as fn
import textnode as tn

class TestTextToNodes(unittest.TestCase):
    def test_markdown_to_html_nodes(self):
        md = """
# Header 1

## Header 2

### Header 3

This is paragraph. This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)

```
section of code
with several lines
of text
```

> Quoted text
> Second line of quoted text

- This is an unorderd list
- item 1
- item 2

1. This is an orderd list
1. with some item 1
1. with some item 2

"""
        expected = "<tag:div, value:None, props:None><tag:h1, value:None, props:None><tag:None, value: Header 1, props:None><tag:h2, value:None, props:None><tag:None, value: Header 2, props:None><tag:h3, value:None, props:None><tag:None, value: Header 3, props:None><tag:p, value:None, props:None><tag:None, value:This is paragraph. This is , props:None><tag:b, value:text, props:None><tag:None, value: with an , props:None><tag:i, value:italic, props:None><tag:None, value: word and a , props:None><tag:code, value:code block, props:None><tag:None, value: and an , props:None><tag:img, value:, props:{'src': 'https://i.imgur.com/fJRm4Vk.jpeg', 'alt': 'obi wan image'}><tag:None, value: and a , props:None><tag:a, value:link, props:{'href': 'https://boot.dev'}><tag:code, value:None, props:None><tag:None, value:section of code\\nwith several lines\\nof text\\n, props:None><tag:blockquote, value:None, props:None><tag:p, value:None, props:None><tag:None, value:Quoted text, props:None><tag:p, value:None, props:None><tag:None, value:Second line of quoted text, props:None><tag:ul, value:None, props:None><tag:li, value:None, props:None><tag:None, value:This is an unorderd list, props:None><tag:li, value:None, props:None><tag:None, value:item 1, props:None><tag:li, value:None, props:None><tag:None, value:item 2, props:None><tag:ol, value:None, props:None><tag:li, value:None, props:None><tag:None, value:This is an orderd list, props:None><tag:li, value:None, props:None><tag:None, value:with some item 1, props:None><tag:li, value:None, props:None><tag:None, value:with some item 2, props:None>"
        nodes = fn.markdown_to_html_node(md)
        result = fn.fprint_html_node(nodes, '')
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
