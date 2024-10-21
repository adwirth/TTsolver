import pyautogui
import pytesseract
import easyocr
from PIL import ImageGrab, ImageOps, ImageFilter
import sympy as sp
import numpy as np
import random
import time
import os

# Configure Tesseract path if not in PATH (if needed)
pytesseract.pytesseract.tesseract_cmd = r"c:\Program Files\Tesseract-OCR\tesseract.exe"

reader = easyocr.Reader(['en'])

# Define region of the screen to capture (x, y, width, height)
def capture_screen(region):
    screenshot = ImageGrab.grab(bbox=region)
    return screenshot

# Apply preprocessing (grayscale, inverse, and blur) before OCR
def preprocess_image(image):
    # Convert the image to grayscale
    grayscale_img = image.convert('L')  # 'L' mode is for grayscale
    
    # Invert the image
    inverted_img = ImageOps.invert(grayscale_img)
    
    # Apply Gaussian blur
    blurred_img = inverted_img.filter(ImageFilter.GaussianBlur(radius=2))
    
    return blurred_img

# Perform OCR on the captured image
def perform_ocr(image):
    return pytesseract.image_to_string(image)

# Perform OCR using EasyOCR on the captured image
def perform_ocr2(image):
    # Preprocess the image
    preprocessed_image = preprocess_image(image)
    # Convert the image to a format that EasyOCR accepts (numpy array)
    image = image.convert("RGB")  # EasyOCR works with RGB images
    result = reader.readtext(np.array(preprocessed_image), detail=0)
    if result:
        return " ".join(result)  # Join results into a string
    return ""


# Evaluate the simple math expression
def evaluate_expression(expression):
    try:
        # Replace + and - with /
        modified_expression = modify_expression(expression)
        print(f"Modified Expression: {modified_expression}")

        # Use sympy for safety and robustness
        result = sp.sympify(modified_expression)

        # Convert the result to a float and round to nearest integer
        result = result.evalf()  # Convert symbolic result to floating-point number
        rounded_result = round(result)  # Round the result to the nearest integer
        
        return rounded_result
    except Exception as e:
        print(f"Error evaluating expression: {e}")
        return None

# Simulate keyboard input using pyautogui
def input_result(result):
    # Add a random delay between 0.4 and 0.8 seconds before inputting
    delay = random.uniform(0.1, 0.4)
    print(f"Delaying input by {delay:.2f} seconds...")
    time.sleep(delay)
    pyautogui.typewrite(str(result))
    pyautogui.press('enter')
    time.sleep(0.1)

def modify_expression(expression):
    return expression.replace('+', '/').replace('-', '/').replace('=', '').replace('x', '*')

# Main function
def main():
    # Define the region to capture (left, top, width, height)
    region = (224, 617, 467, 712)  # Modify this according to the area you want to capture
    
    while True:
        # Capture screen
        image = capture_screen(region)
        
        # Perform OCR to extract text (math expression)
        # math_expression = perform_ocr(image)
        # print(f"Detected Expression: {math_expression.strip()}")
        math_expression = perform_ocr2(image)
        print(f"Detected Expression: {math_expression.strip()}")


        
        # Calculate the result of the expression
        result = None
        result = evaluate_expression(math_expression)
        
        if result is not None:
            print(f"Calculated Result: {result}")
            
            # Input the result into the current active window
            input_result(result)
        
        # Wait for a few seconds before next iteration (avoid overloading)
        # time.sleep(1)

if __name__ == "__main__":
    main()
