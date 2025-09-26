from textnode import *
from static_to_public import copy_directory_contents
from generate_page import generate_pages_recursive
import sys



def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    
    copy_directory_contents(f"static", "public")

    generate_pages_recursive(f"content", "template.html", "public", basepath)

if __name__ == "__main__":
    main()