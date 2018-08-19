import os
import argparse
#from selenium import webdriver
#from selenium.webdriver.chrome.options import Options


ap = argparse.ArgumentParser()
ap.add_argument("directory", help="path to font files")
args = vars(ap.parse_args())

filename = "test.html"

font_dir = args["directory"];

walk_output = os.walk(font_dir)

#chrome_options = Options()  
#chrome_options.add_argument("--headless")  
#chrome_options.add_argument("--window-size=%s" % "800,600")
#chrome_options.binary_location = "/usr/bin/google-chrome"

#driver = webdriver.Chrome(executable_path='/home/prnvdixit/Desktop/chromedriver',
                            chrome_options=chrome_options
                            )

#index = 0


text = open(filename, "r").read()
ocr_text = "Jennifer Niedersl Robbins"

for root, dirs, files in walk_output:
    path = root.split(os.sep)
    dir_name = os.path.basename(root)
    if(dir_name):
        fam_name = (dir_name)
        for file_name in files:
            font_name = ('/'.join(path) + "/" + file_name)
            with open("another-test.html", "w") as edit:
                edit.write(text.replace("fam_name", fam_name).replace("font_name", font_name).replace("ocr_text", ocr_text))

            #temp_name = "file://" + "/home/prnvdixit/Codes/Pyfont/another-test.html"

            #driver.get(temp_name)
            #save_name = '00' + str(index) + '.png'       
            #driver.save_screenshot(save_name)
            #index += 1
#driver.quit()
