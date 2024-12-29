from src.image_loader import load_image_opencv
from src.image_filters import apply_grayscale_opencv, apply_blur_opencv
from src.image_enhancers import enhance_image_contrast, enhance_image_brightness
from src.utils import save_image, create_directory

def main():
    input_image_path = "input/image.jpg"
    output_directory_path = "output"
    output_image_path = os.path.join(output_directory_path, "enhanced_image.jpg")

    # Load image
    image = load_image_opencv(input_image_path)

    # Enhance image
    enhanced_image = enhance_image_contrast(image)
    enhanced_image = enhance_image_brightness(enhanced_image)

    # Apply filters
    grayscale_image = apply_grayscale_opencv(enhanced_image)
    blurred_image = apply_blur_opencv(grayscale_image)

    # Save image
    create_directory(output_directory_path)
    save_image(blurred_image, output_image_path)

if __name__ == "__main__":
    main()