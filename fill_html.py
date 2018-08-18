import os
import argparse


ap = argparse.ArgumentParser()
ap.add_argument("directory", help="path to font files")
args = vars(ap.parse_args())

filename = "test.html"

font_dir = args["directory"];

walk_output = os.walk(font_dir)

text = open(filename, "r").read()

for root, dirs, files in walk_output:
    path = root.split(os.sep)
    dir_name = os.path.basename(root)
    if(dir_name):
        fam_name = ('/'.join(path[:-1]) + "/" + dir_name)
        for file_name in files:
            font_name = ('/'.join(path) + "/" + file_name)
            with open("another-test.html", "w") as edit:
                edit.write(text.replace("fam_name", fam_name).replace("font_name", font_name))
