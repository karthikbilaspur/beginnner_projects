import cv2
from PIL import ImageFilter

def apply_grayscale_opencv(image):
    """Applies grayscale filter using OpenCV"""
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def apply_grayscale_pillow(image):
    """Applies grayscale filter using Pillow"""
    return image.convert('L')

def apply_blur_opencv(image, kernel_size=5):
    """Applies Gaussian blur filter using OpenCV"""
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

def apply_blur_pillow(image, radius=2):
    """Applies Gaussian blur filter using Pillow"""
    return image.filter(ImageFilter.GaussianBlur(radius=radius))