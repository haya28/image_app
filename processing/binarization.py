import cv2

def binarize_image(image_path, threshold=128):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    _, binary = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
    return binary
