import cv2
import argparse
import sys
import numpy as np

def min_bound_rect(image):

    small = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    grad = cv2.morphologyEx(small, cv2.MORPH_GRADIENT, kernel)

    _, bw = cv2.threshold(grad, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 1))
    connected = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, kernel)
    # using RETR_EXTERNAL instead of RETR_CCOMP
    _, contours, hierarchy = cv2.findContours(connected.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    mask = np.zeros(bw.shape, dtype=np.uint8)

    x, y, w, h = cv2.boundingRect(contours[0])
    mask[y:y+h, x:x+w] = 0
    cv2.drawContours(mask, contours, 0, (255, 255, 255), -1)
    r = float(cv2.countNonZero(mask[y:y+h, x:x+w])) / (w * h)
    
    if r > 0.45 and w > 8 and h > 8:
        return image[y:y+h, x:x+w]

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
    help="path to image to crop")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
#print(image.shape)
#cv2.imshow("Image", image)
#image = find_boundary(image)

image = min_bound_rect(image)

print(image.shape)
#cv2.imshow("Cropped", image)
cv2.imwrite("UbuntuMono-Cropped.png", image)

if cv2.waitKey(0) & 0xFF == 'q':
    sys.exit()
