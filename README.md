# PyFont

PyFont is a command-line application to detect fonts of text in images. It can be configured to include fonts existing in the system (eg. paid ones) as well.

## Dependencies

- Python3
- OpenCV
- Argparse
- Numpy
- Selenium Webdriver
- Pytesseract

## Working

Tesseract library is first used for OCR - Detecting text from the image supplied. The input image is cropped to text only (omitting out the unnecessary parts and borders). The text obtained from OCR is checked against different fonts (using the ttf-directory, supplied through commandline arguments) and is checked using image similarity algorithms for best matches.

## Known Issues

## Future work

- Add rotational invariance for input images
- Use Google API (give a cmd arguement for same) instead of downloading the .ttf files
- Add tests

## Contributors

## License
