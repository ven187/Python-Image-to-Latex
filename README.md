# Image to LaTeX Converter

This Python script converts basic-level image files containing mathematical formulas into LaTeX formatted output. The script utilizes the Tesseract OCR engine for text recognition and generates LaTeX formulas from the detected text.

## Requirements
- Python 3.x
- PIL (Python Imaging Library)
- matplotlib
- OpenCV (cv2)
- pytesseract
- pix2tex

## Usage
1. Ensure all dependencies are installed.
2. Set the Tesseract executable path (`tesseract_cmd`) according to your system.
3. Run the script and select the region of interest (ROI) containing the mathematical formula.
4. The script will perform OCR on the selected region and display the detected text along with the bounding box.
5. Detected text will be converted into a LaTeX formula and saved as an image in the 'output' folder.

## Example

### Input

![Input Image](https://github.com/ven187/Python-Image-to-Latex/raw/main/12.png)

### Output

![Generated LaTeX Formula](https://github.com/ven187/Python-Image-to-Latex/raw/main/output/XggHHM.png)
