import cv2
import os

def save_image(image, image_path):
    """Saves image"""
    cv2.imwrite(image_path, image)

def create_directory(directory_path):
    """Creates directory if not exists"""
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)