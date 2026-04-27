from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag = None, value = None, props = None):
        super().__init__(tag, value, children = None, props = None)
        if value == None:
            raise ValueError
        self.tag = tag
        self.value = value
        self.props = props
        
    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        print(f"tag:{self.tag}, value:{self.value}, props:{self.props}")
    
