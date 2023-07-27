# Import necessary libraries
from PIL import ImageGrab
import pytesseract
import cv2

# Set the coordinates of the area of the screen to be captured
bbox = (100, 100, 500, 500)

# Use a loop to repeatedly capture the specified part of the screen
while True:
    # Capture the specified part of the screen
    image = ImageGrab.grab(bbox)

    # Convert the captured image to grayscale
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use PyTesseract to recognize the text in the image
    text = pytesseract.image_to_string(image)

    # Print the recognized text
    print(text)
