import cv2
import numpy as np
import os
from keras.models import load_model

# Load the model
model = load_model('BrainTumor.h5')

# Function to get class name
def get_className(classNo):
    if classNo == 0:
        return "No Brain Tumor"
    elif classNo == 1:
        return "Yes Brain Tumor"

# Read and preprocess the image using OpenCV
# Use a sample image from the test directory
image_path = os.path.join('yes', 'Y51.jpg')  # Update with your own test image path
if not os.path.exists(image_path):
    print(f"Error: Test image not found at {image_path}")
    print("Please update the image path to a valid MRI scan image.")
    exit(1)

image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
image = cv2.resize(image, (64, 64))  # Resize to match input shape of the model
image = image / 255.0  # Normalize the image

# Expand dimensions to match the input shape of the model
input_img = np.expand_dims(image, axis=0)

# Make prediction
result = model.predict(input_img)
predicted_class = np.argmax(result)

# Get the class name
class_name = get_className(predicted_class)

print(f'Prediction: {class_name}')
print(f'Predicted Class: {predicted_class}, Probability: {np.max(result):.4f}')
