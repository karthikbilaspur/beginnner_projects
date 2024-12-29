import cv2
from PIL import Image

def load_image_opencv(image_path):
    """Loads image using OpenCV"""
    return cv2.imread(image_path)

def load_image_pillow(image_path):
    """Loads image using Pillow"""
    return Image.open(image_path)