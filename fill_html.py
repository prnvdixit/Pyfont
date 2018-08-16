import os
import argparse


ap = argparse.ArgumentParser()
ap.add_argument("directory", required=True,
    help="path to font files")
args = vars(ap.parse_args())

filename = "test.html"

font_dir = args.directory;

text = open(filename, "r").read()
with open("another-test.html", "w") as edit:
    print([os.path.abspath(name) for name in os.listdir(font_dir) if os.path.isdir(name)])
    edit.write(text.replace("dir_name", "ubuntu").replace("font_name", "Ubuntu-Regular.ttf"))
