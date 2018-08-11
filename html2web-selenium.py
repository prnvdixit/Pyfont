import glob
from PIL import Image
from selenium import webdriver
import os 

# get a list of all the files to open
glob_folder = os.path.join("/home/prnvdixit/Codes/Pyfont", '*.html')

os.environ['MOZ_HEADLESS'] = '1'
 
#driver = webdriver.Firefox(executable_path='/home/prnvdixit/Desktop/geckodriver')
#driver.get('http://10.14.36.185:8080/')
#driver.save_screenshot("/home/prnvdixit/Desktop/screenshot.png")

html_file_list = glob.glob(glob_folder)
index = 1

for html_file in html_file_list:

    # get the name into the right format
    temp_name = "file://" + html_file

    # open in webpage
    driver = webdriver.Firefox(executable_path='/home/prnvdixit/Desktop/geckodriver')
    driver.get(temp_name)
    save_name = '00' + str(index) + '.png'       
    driver.save_screenshot("UbuntuMono-HTML.png")
    driver.quit()
    index += 1
