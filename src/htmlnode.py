

class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag              # (e.g. "p", "a", "h1", etc.)
        self.value = value          # (e.g. the text inside a paragraph)
        self.children = children    # List of child HTMLNodes
        self.props = props          # {"href": "https://www.google.com"}

    def to_html(self):
        if self.tag is None:
            return self.value
        
        props_str = ""
        if self.props:
            props_str = "".join([f' {k}="{v}"' for k, v in self.props.items()])
        
        if self.children is None:
            return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"
        
        children_html = "".join([child.to_html() for child in self.children])
        return f"<{self.tag}{props_str}>{children_html}</{self.tag}>"
    
    def props_to_html(self):
        html_string = ''
        for key, value in self.props.items():
            html_string += f' {key}={value}'
        return html_string
    
    def __repr__(self):
        return f'tag = {self.tag}\nvalue = {self.value}\nchildren = {self.children}\nprops = {self.props}'
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        self.tag = tag
        self.value = value
        self.children = None
        self.props = props
    
    def to_html(self):
        if self.tag == 'img':
            if not self.props:
                return f"<{self.tag}>"
            props_html = "".join([f' {k}="{v}"' for k, v in self.props.items()])
            return f"<{self.tag}{props_html}>"
        if not self.value:
            raise ValueError("LeafNode has no value")
        if not self.tag:
            return f'{self.value}'
        if self.props:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        if not self.tag:
            raise ValueError("No woman no tag")
        if not self.children:
            raise ValueError("No children by The Mountain Goats")
        final_string = ''
        for child in self.children:
            final_string += child.to_html()
        final_string = f'<{self.tag}>{final_string}</{self.tag}>'
        return final_string
