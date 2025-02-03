import cv2
import numpy as np

def inpaint_image(image_path, mask_path):
    image = cv2.imread(image_path)
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
    restored = cv2.inpaint(image, mask, 3, cv2.INPAINT_TELEA)
    return restored
