from PIL import Image
import matplotlib.pyplot as plt
from pix2tex.cli import LatexOCR
from io import BytesIO
import string
import random
import cv2
import pytesseract
import os

# Set Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Check if the output folder exists, if not, create it
output_folder = 'output'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Function to generate a random title
def get_random_title():
    N = 5
    res = 'X' + ''.join(random.choices(string.ascii_letters, k=N))
    return res

# Function to render LaTeX formula
def render_latex(formula, filename='output.png', fontsize=12, dpi=500, format_='png'):
    file_path = os.path.join(output_folder, filename)
    fig = plt.figure(figsize=(0.01, 0.01))
    fig.text(0, 0, u'${}$'.format(formula), fontsize=fontsize)
    buffer_ = BytesIO()
    fig.savefig(buffer_, dpi=dpi, transparent=False, format=format_, bbox_inches='tight', pad_inches=0.6)
    plt.close(fig)
    
    # Write the buffer to a file
    with open(file_path, 'wb') as f:
        f.write(buffer_.getvalue())

# Function for LaTeX OCR
def latex_ocr(image_path):
    try:
        # Open the image
        img = Image.open(image_path)

        # Load the LatexOCR model
        model = LatexOCR()

        # Recognize the text
        text = model(img)

        return text

    except Exception as e:
        return str(e)

# Read the input image
core_image = cv2.imread("12.png")

# Select a region of interest (ROI)
r = cv2.selectROI("Select Field :", core_image , cv2.WINDOW_NORMAL)

# Crop the image based on the ROI
cropped_image = core_image[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]

# Save the cropped image temporarily
tmp_img = "temp_img.png"
cv2.imwrite(tmp_img , cropped_image)

# Read the temporarily saved image
img = cv2.imread(tmp_img)

# Resize the image
img = cv2.resize(img, (600, 360))
hImg, wImg, _ = img.shape

# Perform OCR on the image
boxes = pytesseract.image_to_boxes(img)
xy = pytesseract.image_to_string(img)
for b in boxes.splitlines():
  b = b.split(' ')
print(b)
x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])

# Draw bounding box and text
cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (50, 50, 255), 1)
cv2.putText(img, b[0], (x, hImg - y + 13), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (50, 205, 50), 1)

# Display the detected text
cv2.imshow('Detected text', img)

# Display the cropped image
cv2.imshow("Select IMG :", cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Process the temporary image for LaTeX OCR
image_path = tmp_img
real_time_name = get_random_title() + '.png'
result = latex_ocr(image_path)

# Print the detected text and the generated image name
print("############################################")
print("Detected Text => "  , result)
print("Generated Image => " , real_time_name)
print("############################################")

# Render the LaTeX formula and save the image
get_latex_formul = result
render_latex(get_latex_formul, filename=real_time_name)
