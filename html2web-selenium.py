import glob
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os 

# get a list of all the files to open
glob_folder = os.path.join("/home/prnvdixit/Codes/Pyfont", '*.html')

chrome_options = Options()  
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--window-size=%s" % "800,600")
chrome_options.binary_location = "/usr/bin/google-chrome"

driver = webdriver.Chrome(executable_path='/home/prnvdixit/Desktop/chromedriver',
                            chrome_options=chrome_options
                            )

#os.environ['MOZ_HEADLESS'] = '1'
#driver = webdriver.Firefox(executable_path='/home/prnvdixit/Desktop/geckodriver')
#driver.get('http://10.14.36.185:8080/')
#driver.save_screenshot("/home/prnvdixit/Desktop/screenshot.png")

html_file_list = glob.glob(glob_folder)
index = 1

for html_file in html_file_list:

    print(html_file)
    # get the name into the right format
    temp_name = "file://" + html_file

    # open in webpage
    driver.get(temp_name)
    save_name = '00' + str(index) + '.png'       
    driver.save_screenshot(save_name)
    index += 1

driver.quit()
