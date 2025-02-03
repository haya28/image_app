import cv2
import numpy as np

def morphology_operation(image_path, operation="dilate", kernel_size=3):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    
    if operation == "dilate":
        processed = cv2.dilate(image, kernel, iterations=1)
    elif operation == "erode":
        processed = cv2.erode(image, kernel, iterations=1)
    else:
        raise ValueError("Invalid operation. Choose 'dilate' or 'erode'.")
    
    return processed
