import cv2
import numpy as np

def gamma_correction(image_path, gamma):
    image = cv2.imread(image_path)
    inv_gamma = 1.0 / gamma
    table = np.array([(i / 255.0) ** inv_gamma * 255 for i in range(256)]).astype("uint8")
    corrected = cv2.LUT(image, table)
    return corrected
