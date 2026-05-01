import re
import textnode as tn
import htmlnode as hn

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

def text_node_to_html_node(text_node):
    prop = None
    if text_node.text_type == tn.TextType.TEXT:
        return hn.LeafNode(None, text_node.text, None, prop)
    if text_node.text_type == tn.TextType.LINK:
        prop = {"href":text_node.url}
    if text_node.text_type == tn.TextType.IMAGE:
        prop = {"src":text_node.url, "alt":text_node.text}
        text_node.text = ""
    return hn.LeafNode(text_node.text_type.value, text_node.text, None, prop)

def split_nodes_delimeter(o_node, delimeter = None, text_type = None):
    new_nodes = []
    if (delimeter == None):
        new_nodes.append(o_node)
    elif text_type != tn.TextType.TEXT:
        new_nodes.append(o_node)
    else:
        parts = o_node.text.split(delimeter)
        if len(parts)%2 == 0:
            raise Exception("invalid markdown syntax")
        for i in range(0, len(parts)):
            if i%2 == 0:
                new_nodes.append(tn.TextNode(parts[i], text_type))
            else:
                type = text_type
                if delimeter == "_":
                    type = tn.TextType.ITALIC
                elif delimeter == "**":
                    type = tn.TextType.BOLD
                elif delimeter == "`":
                    type = tn.TextType.CODE
                new_nodes.append(tn.TextNode(parts[i], type))
    return new_nodes
