import numpy as np
import cv2

def mse(img1, img2):
    
    err = np.sum((img1.astype("float") - img2.astype("float")) ** 2)
    err /= float(img1.shape[0] * img1.shape[1])

    return err

img1 = cv2.imread("UbuntuMonoShot.png")
img2 = cv2.imread("UbuntuMono-Cropped.png")

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

img1 = cv2.resize(img1, (img2.shape[1], img2.shape[0]))

print(mse(img1, img2))


# 18470.133661740558
# 5876.877963125548
