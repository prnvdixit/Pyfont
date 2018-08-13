filename = "test.html"
text = open(filename, "r").read()
with open("another-test.html", "w") as edit:
    edit.write(text.replace("dir_name", "ubuntu").replace("font_name", "Ubuntu-Regular.ttf"))
