
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
    
