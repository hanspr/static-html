import textnode

class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            return ""
        str = ""
        for k in self.props.keys():
            str = str + f" {k}=\"{self.props[k]}\""
        return str
    
    def __repr__(self):
        print(f"tag:{self.tag}, value:{self.value}, children:{self.children}, props:{self.props}")


class LeafNode(HTMLNode):
    def __init__(self, tag = None, value = None, children = None, props = None):
        super().__init__(tag, value, children, props)
        if value == None:
            raise ValueError("value is required")
        if children != None:
            raise ValueError("children not permitted on a leaf node")
        self.tag = tag
        self.value = value
        self.props = props
        
    def to_html(self):
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        print(f"tag:{self.tag}, value:{self.value}, props:{self.props}")
    
class ParentNode(HTMLNode):
    def __init__(self, tag = None, value = None, children = None, props = None):
        super().__init__(tag, value, children, props)
        if children == None:
            raise ValueError("parent node requires children")
        if tag == None:
            raise ValueError("tag is requeried")
        self.tag = tag
        self.children = children
        self.props = props
        
    def to_html(self):
        nodes = ""
        for child in self.children:
            nodes = nodes + child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{nodes}</{self.tag}>"
    
    def __repr__(self):
        print(f"tag:{self.tag}, value:{self.value}, props:{self.props}")
    
def text_node_to_html_node(text_node):
    prop = None
    if text_node.text_type == textnode.TextType.TEXT:
        return LeafNode(None, text_node.text, None, prop)
    if text_node.text_type == textnode.TextType.LINK:
        prop = {"href":text_node.url}
    if text_node.text_type == textnode.TextType.IMAGE:
        prop = {"src":text_node.url, "alt":text_node.text}
        text_node.text = ""
    return LeafNode(text_node.text_type.value, text_node.text, None, prop)
