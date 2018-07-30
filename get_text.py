from PIL import Image
import cv2
import imutils

import pytesseract

import argparse

import os
import sys
import subprocess


def downscale_image(args):
    
    DPI = 300
    height, width, _ = image.shape
    
    temp_path = os.getcwd() + '/temp.jpeg'
    cmd = ["convert", "-units", "PixelsPerInch", args["image"], "-density", str(DPI), temp_path]
    subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).wait()
    
    downscaled_image = cv2.imread(temp_path)
    os.remove(temp_path)
 
    return downscaled_image


def crop_to_text(image):
    return

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
    help="path to image to get text from")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

cv2.imshow("Input image", image)

# Resize if required for best detection (from docs)
downscaled_image = downscale_image(args)
cv2.imshow("Resized image", downscaled_image)

#cropped_image = crop_to_text(image)
#deskewed_cropped_image = fix_skewness(cropped_image)

# Convert to Grayscale
gray = cv2.cvtColor(downscaled_image, cv2.COLOR_BGR2GRAY)


#gray = cv2.threshold(gray, 0, 255,
#    cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]


gray = cv2.medianBlur(gray, 3)

#cv2.imshow("Blurred Image", gray)

#filename = "x.png"
#cv2.imwrite(filename, gray)

#text = pytesseract.image_to_string(Image.open(filename))
#os.remove(filename)
#print(text)

#cv2.imshow("Image", image)
#cv2.imshow("Output", gray)

if cv2.waitKey(0) & 0xFF == 'q':
    sys.exit()
