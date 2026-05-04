import re
import textnode as tn
import htmlnode as hn
from pprint import pprint

# htmlnode:

def text_node_to_html_node(text_node):
    prop = None
    if text_node.text_type == tn.TextType.TEXT:
        return hn.LeafNode(None, text_node.text, None, prop)
    elif text_node.text_type == tn.TextType.BOLD:
        return hn.LeafNode('b', text_node.text, None, prop)
    elif text_node.text_type == tn.TextType.ITALIC:
        return hn.LeafNode('i', text_node.text, None, prop)
    elif text_node.text_type == tn.TextType.CODE:
        return hn.LeafNode('code', text_node.text, None, prop)
    if text_node.text_type == tn.TextType.LINK:
        prop = {"href":text_node.url}
    if text_node.text_type == tn.TextType.IMAGE:
        prop = {"src":text_node.url, "alt":text_node.text}
        text_node.text = ""
    return hn.LeafNode(text_node.text_type.value, text_node.text, None, prop)

# textnode:

def extract_markdown_images(text):
    return re.findall(r"!\[(.+?)\]\((.+?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"[^!]\[(.+?)\]\((.+?)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != tn.TextType.TEXT:
            new_nodes.append(node)
            continue
        parts = re.split(r"(!\[.+?\]\(.+?\))", node.text)
        for part in parts:
            if re.search(r"^!", part):
                props = extract_markdown_images(part)
                link = tn.TextNode(props[0][0], tn.TextType.IMAGE, props[0][1])
                new_nodes.append(link)
            elif part == "":
                continue
            else:
                if part != parts[-1] and not part.endswith(" "):
                    part = part + " "
                new_nodes.append(tn.TextNode(part, tn.TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != tn.TextType.TEXT:
            new_nodes.append(node)
            continue
        parts = re.split(r"([^!]\[.+?\]\(.+?\))", node.text)
        for part in parts:
            if re.search(r"[^!]\[", part):
                props = extract_markdown_links(part)
                link = tn.TextNode(props[0][0], tn.TextType.LINK, props[0][1])
                new_nodes.append(link)
            elif part == "":
                continue
            else:
                if part != parts[-1] and not part.endswith(" "):
                    part = part + " "
                new_nodes.append(tn.TextNode(part, tn.TextType.TEXT))
    return new_nodes

def split_nodes_delimeter(old_nodes, delimeter = None):
    new_nodes = []
    for node in old_nodes:
        if (delimeter == None):
            new_nodes.append(node)
        elif node.text_type != tn.TextType.TEXT:
            new_nodes.append(node)
        else:
            parts = node.text.split(delimeter)
            if len(parts)%2 == 0:
                raise Exception("invalid markdown syntax")
            for i in range(0, len(parts)):
                if i%2 == 0:
                    new_nodes.append(tn.TextNode(parts[i], node.text_type))
                else:
                    type = node.text_type
                    if delimeter == "_":
                        type = tn.TextType.ITALIC
                    elif delimeter == "**":
                        type = tn.TextType.BOLD
                    elif delimeter == "`":
                        type = tn.TextType.CODE
                    new_nodes.append(tn.TextNode(parts[i], type))
    return new_nodes

# markdown:

def markdown_to_blocks(markdown):
    blocks = []
    parts = re.split("\n\n+", markdown)
    for part in parts:
        part = part.strip()
        if part == "":
            continue
        blocks.append(part)
    return blocks

def block_to_block_type(block):
    if re.search(r"^#{1,6} \S", block):
        return tn.BlockType.HEADER
    if re.search(r"```", block):
        return tn.BlockType.CODE
    if re.search(r"^> ?", block, flags = re.M):
        return tn.BlockType.QUOTE
    if re.search(r"^- ", block, flags = re.M):
        return tn.BlockType.ULIST
    if re.search(r"^\d+\. ", block, flags = re.M):
        return tn.BlockType.OLIST
    return tn.BlockType.PARAGRAPH

def process_uolist(text, rgx):
    children = []
    lines = text.split("\n")
    for line in lines:
        line = re.sub(rgx, "", line)
        child_nodes = text_to_nodes(line)
        bnode = hn.ParentNode(tag = "li", children = child_nodes)
        children.append(bnode)
    return children

def process_lines(text, rgx):
    children = []
    lines = text.split("\n")
    for line in lines:
        line = re.sub(rgx, "", line)
        child_nodes = text_to_nodes(line)
        bnode = hn.ParentNode(tag = "div", children = child_nodes)
        children.append(bnode)
    return children

def text_to_nodes(text):
    children = []
    text_node = tn.TextNode(text, tn.TextType.TEXT)
    nodes = split_nodes_image([text_node])
    nodes = split_nodes_link(nodes)
    for delimeter in ("_", "**", "`"):
        nodes = split_nodes_delimeter(nodes, delimeter)
    for node in nodes:
        html_node = text_node_to_html_node(node)
        children.append(html_node)
    return children
    
def text_to_children(btype, text):
    children = []
    if btype == tn.BlockType.HEADER:
        text = text.lstrip("#")
        children = text_to_nodes(text)
    elif btype == tn.BlockType.PARAGRAPH:
        children = text_to_nodes(text)
    elif btype == tn.BlockType.ULIST:
        children = process_uolist(text, r"^- ")
    elif btype == tn.BlockType.OLIST:
        children = process_uolist(text, r"^\d+\. ")
    elif btype == tn.BlockType.QUOTE:
        text = process_lines(text, r"^> ?")
    elif btype == tn.BlockType.CODE:
        value = ""
        lines = text.split("\n")
        for line in lines:
            if line == "```":
                continue
            value = value + line + "\n"
        children.append(hn.LeafNode(tag = None, value = value))
        return children
    return children
    
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        btype = block_to_block_type(block)
        bnode = hn.ParentNode(tag = btype.value, children=[])
        match btype.value:
            case "h":
                level = block.count("#")
                bnode.tag = f"h{level}"
            case "quote":
                bnode.tag = 'div'
        bnode.children = text_to_children(btype, block)
        children.append(bnode)
    parent = hn.ParentNode(tag = "div", children = children)
    return parent

# section: help testing functions

indent = 0

# print tree
def print_html_node(node):
    global indent
    if (indent > 0):
        print("  " * indent, node)
    else:
        print(node)
    indent = indent + 1
    for child in node.children:
        if child.children != None:
            print_html_node(child)
            indent = indent - 1
        else:
            print("  " * indent, child)

# get formated tree
def fprint_html_node(node):
    str = f"{node!r}"
    for child in node.children:
        if child.children != None:
            str += fprint_html_node(child)
        else:
            str += f"{node!r}"
    return str

# test: section

