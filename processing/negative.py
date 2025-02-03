import cv2

def negative_image(image_path):
    image = cv2.imread(image_path)
    negative = cv2.bitwise_not(image)
    return negative
