import os
import shutil
import functions as fn

#from textnode import *
#import textnode

def clean_dir(dir):
    shutil.rmtree(dir, ignore_errors = True)
    os.mkdir(dir)
    return

def copy_dir(dir_from = "", dir_to = ""):
    if dir_from == "" or dir_to == "" or os.path.exists(dir_from) == False or os.path.exists(dir_to) == False or os.path.isdir(dir_from) == False or os.path.isdir(dir_to) == False:
        print(f"Nothing to do, invalid paths {dir_from} -> {dir_to}")
        return
    paths = os.listdir(dir_from)
    for path in paths:
        fpath = os.path.join(dir_from, path)
        tpath = os.path.join(dir_to, path)
        if os.path.isfile(fpath):
            if fpath.find(".md") != -1:
                tpath = tpath.replace(".md", ".html")
                fn.generate_page(fpath, "./template.html", tpath)
            else:
                shutil.copy(fpath, tpath)
        elif os.path.isdir(fpath):
            if os.path.exists(tpath) == False:
                os.mkdir(tpath)
            copy_dir(fpath, tpath)

def main():
    clean_dir("./public")
    copy_dir("./static", "./public")

if __name__ == "__main__":
    main()
