import re
import textnode as tn

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

