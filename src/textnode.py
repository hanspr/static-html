from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "b"
    ITALIC = "i"
    CODE = "code"
    LINK = "a"
    IMAGE = "img"

class TextNode():
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self):
        return f"TextNode({self.text},{self.text_type.name},{self.url})"

def split_nodes_delimeter(o_node, delimeter = None, text_type = None):
    new_nodes = []
    if (delimeter == None):
        new_nodes.append(o_node)
    elif text_type != TextType.TEXT:
        new_nodes.append(o_node)
    else:
        parts = o_node.text.split(delimeter)
        if len(parts)%2 == 0:
            raise Exception("invalid markdown syntax")
        for i in range(0, len(parts)):
            if i%2 == 0:
                new_nodes.append(TextNode(parts[i], text_type))
            else:
                type = text_type
                if delimeter == "_":
                    type = TextType.ITALIC
                elif delimeter == "**":
                    type = TextType.BOLD
                elif delimeter == "`":
                    type = TextType.CODE
                new_nodes.append(TextNode(parts[i], type))
    return new_nodes
