from PIL import Image
import cv2
import imutils

import pytesseract

import numpy as np

import argparse

import os
import sys
import subprocess

import file_names
import crop_to_text

#def downscale_image(args):
#    
#    DPI = 300
#    height, width, _ = image.shape
#    
#    temp_path = os.getcwd() + '/temp.jpeg'
#    cmd = ["convert", "-units", "PixelsPerInch", args["image"], "-density", str(DPI), temp_path]
#    subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).wait()
#    
#    downscaled_image = cv2.imread(temp_path)
#    os.remove(temp_path)
#
#    return downscaled_image

def return_text(image):

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.fastNlMeansDenoising(image, None, 10, 3, 7)

    #cv2.imshow("Gray", image)

    image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 41, 10) 

    filename = file_names.denoised_threshed_input_image
    image = crop_to_text.fit_to_text(image)
    cv2.imwrite(filename, image)

    text = pytesseract.image_to_string(Image.open(filename))
    
    return text

if __name__ == "__main__":

    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True,
        help="path to image to get text from")
    args = vars(ap.parse_args())

    image = cv2.imread(args["image"])
    #cv2.imshow("Input image", image)

    #deskewed_cropped_image = fix_skewness(cropped_image)

    #image = downscale_image(args)

    print(return_text(image))
