# 2値化処理
import cv2
import numpy as np
from matplotlib import pyplot as plt

def binarize_image(image_path, threshold=128):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    _, th1 = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
    _, th2 = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY_INV)
    _, th3 = cv2.threshold(image, threshold, 255, cv2.THRESH_TRUNC)
    _, th4 = cv2.threshold(image, threshold, 255, cv2.THRESH_TOZERO)
    _, th5 = cv2.threshold(image, threshold, 255, cv2.THRESH_TOZERO_INV)
    
    titles = ['Original', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
    images = [image, th1, th2, th3, th4, th5]
    
    for i in range(6):
        plt.subplot(2, 3, i + 1)
        plt.imshow(images[i], 'gray', vmin=0, vmax=255)
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    
    plt.show()
    return th1  # デフォルトの2値化画像を返す
