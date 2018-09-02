import cv2
import argparse

import get_text
import fill_html

import operator

#################################################################################################################################
#                                                _____       ______          _                                                  #
#                                               |  __ \     |  ____|        | |                                                 #
#                                               | |__) |   _| |__ ___  _ __ | |_                                                #
#                                               |  ___/ | | |  __/ _ \| '_ \| __|                                               #
#                                               | |   | |_| | | | (_) | | | | |_                                                #
#                                               |_|    \__, |_|  \___/|_| |_|\__|                                               #
#                                                        _/ |                                                                   #
#                                                       |___/            	                                                    #
#################################################################################################################################

if __name__ == "__main__":
    
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True,
        help="path to image to crop")
    ap.add_argument("directory", help="path to font files")    
    args = vars(ap.parse_args())

    image = cv2.imread(args["image"])
    ocr_text = get_text.return_text(image)
    #print(ocr_text)
    error_values = fill_html.screenshot_html(args, ocr_text)

    error_values_sort = sorted(error_values.items(), key=operator.itemgetter(1))

    print(error_values_sort[:10])
