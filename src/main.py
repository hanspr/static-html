
#from textnode import *
import textnode

def main():
    text_node = textnode.TextNode('anchore text', textnode.TextType.LINK, 'https://microflow.com.mx')
    print(text_node)

if __name__ == "__main__":
    main()
