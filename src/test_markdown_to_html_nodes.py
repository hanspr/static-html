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
        expected = "tag:div, value:None, props:Nonetag:h1, value:None, props:Nonetag:h1, value:None, props:Nonetag:h2, value:None, props:Nonetag:h2, value:None, props:Nonetag:h3, value:None, props:Nonetag:h3, value:None, props:Nonetag:p, value:None, props:Nonetag:p, value:None, props:Nonetag:p, value:None, props:Nonetag:p, value:None, props:Nonetag:p, value:None, props:Nonetag:p, value:None, props:Nonetag:p, value:None, props:Nonetag:p, value:None, props:Nonetag:p, value:None, props:Nonetag:p, value:None, props:Nonetag:p, value:None, props:Nonetag:pre, value:None, props:Nonetag:pre, value:None, props:Nonetag:div, value:None, props:Nonetag:ul, value:None, props:Nonetag:li, value:None, props:Nonetag:li, value:None, props:Nonetag:li, value:None, props:Nonetag:li, value:None, props:Nonetag:li, value:None, props:Nonetag:li, value:None, props:Nonetag:ol, value:None, props:Nonetag:li, value:None, props:Nonetag:li, value:None, props:Nonetag:li, value:None, props:Nonetag:li, value:None, props:Nonetag:li, value:None, props:Nonetag:li, value:None, props:None"
        nodes = fn.markdown_to_html_node(md)
        result = fn.fprint_html_node(nodes)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
