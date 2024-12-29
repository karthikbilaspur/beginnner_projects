import cv2

def enhance_image_contrast(image):
    """Enhances image contrast"""
    return cv2.convertScaleAbs(image, alpha=2, beta=0)

def enhance_image_brightness(image, value=50):
    """Enhances image brightness"""
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hsv[:, :, 2] += value
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)