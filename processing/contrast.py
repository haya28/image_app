import cv2
import numpy as np

def adjust_contrast(image_path, alpha):
    image = cv2.imread(image_path)
    adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=0)
    return adjusted
