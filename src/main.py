#!/home/hans/.local/share/mise/installs/python/latest/bin/python

from textnode import *

def main():
    text_node = TextNode('anchore text', TextType.LINK, 'https://microflow.com.mx')
    print(text_node)

if __name__ == "__main__":
    main()
