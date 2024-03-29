import cv2
from PIL import Image
import io

import os
import argparse
import numpy as np

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import file_names
import crop_to_text
import compare_img

def screenshot_html(args, ocr_text):

    filename = file_names.template_html

    font_dir = args["directory"];

    walk_output = os.walk(font_dir)

    chrome_options = Options()  
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--window-size=%s" % "800,600")
    chrome_options.binary_location = "/usr/bin/google-chrome"

    driver = webdriver.Chrome(executable_path='/home/prnvdixit/Desktop/chromedriver',
                                chrome_options=chrome_options
                                )

    error_values = {}

    text = open(filename, "r").read()

    index = 0

    for root, dirs, files in walk_output:
        path = root.split(os.sep)
        dir_name = os.path.basename(root)
        if(dir_name):
            fam_name = (dir_name)
            try:
                for file_name in files:
                    font_name = ('/'.join(path) + "/" + file_name)
                    with open(file_names.edited_html, "w") as edit:
                        edit.write(text.replace("fam_name", fam_name).replace("font_name", font_name).replace("ocr_text", ocr_text))

                    temp_name = "file://" + "/home/prnvdixit/Codes/Pyfont/" + file_names.edited_html

                    driver.get(temp_name)
                    screenshot_image = driver.get_screenshot_as_png()
                    #save_name = file_names.full_page_html_image

                    #driver.save_screenshot(save_name)
                    # Save cropped HTML page image
                    #screenshot_image = cv2.imread(save_name, cv2.IMREAD_GRAYSCALE)

                    screenshot_image = Image.open(io.BytesIO(screenshot_image))

                    r, g, b, a = cv2.split(np.asarray(screenshot_image))
                    contrast = cv2.merge([b, g, r])
                    # Reads the enhanced image and converts it to grayscale, creates new file
                    screenshot_image = cv2.cvtColor(contrast, cv2.COLOR_BGR2GRAY)
                    #screenshot_image = cv2.cvtColor(np.asarray(screenshot_image), cv2.COLOR_BGR2GRAY)
                    #cv2.imshow("Frame", screenshot_image)
                    #cv2.waitKey(1000)


                    image = crop_to_text.fit_to_text(screenshot_image)
                    cv2.imwrite(file_names.cropped_html_image, image)

                    # Call error values
                    error_val = compare_img.mse(cv2.imread(file_names.cropped_html_image),
                                                cv2.imread(file_names.denoised_threshed_input_image)
                                                )

                    error_values[font_name] = error_val
                    index += 1

                    #if cv2.waitKey(1000) & 0xFF == ord('q'):
                    #    cv2.destroyAllWindows()
            except Exception as e:
                print(e)
                print(index)
                print(fam_name)

    driver.quit()
    print(index)
    return error_values

if __name__ == "__main__":

    ap = argparse.ArgumentParser()
    ap.add_argument("directory", help="path to font files")
    args = vars(ap.parse_args())

    ocr_text = "Jennifer Niedersl Robbins"
    print(screenshot_html(args, ocr_text))
