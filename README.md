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
```python
python main.py

## Input

![12](https://github.com/ven187/Python-Image-to-Latex/assets/172064899/792e267d-59cb-4239-8396-4bac1be8c3a3)


## Output

![XggHHM](https://github.com/ven187/Python-Image-to-Latex/assets/172064899/08780521-c482-4ff9-82e0-b870753f377e)

