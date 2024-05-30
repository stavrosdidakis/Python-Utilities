import os
from PIL import Image

def crop_and_resize_images(input_folder, output_folder, target_size=(1024, 1024)):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over each file in the input folder
    for filename in os.listdir(input_folder):
        # Create the full input path
        input_path = os.path.join(input_folder, filename)
        
        # Check if it's a file and an image
        if os.path.isfile(input_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            with Image.open(input_path) as img:
                # Calculate the cropping box to make the image square
                width, height = img.size
                if width > height:
                    left = (width - height) / 2
                    top = 0
                    right = (width + height) / 2
                    bottom = height
                else:
                    left = 0
                    top = (height - width) / 2
                    right = width
                    bottom = (height + width) / 2

                # Crop the image to a square
                square_img = img.crop((left, top, right, bottom))

                # Resize the square image to the target size
                resized_img = square_img.resize(target_size, Image.LANCZOS)

                # Create the full output path
                output_path = os.path.join(output_folder, filename)

                # Save the cropped and resized image
                resized_img.save(output_path)

                print(f"Cropped and resized {filename} to {output_folder}")

# Example usage
input_folder = '/input'
output_folder = '/output'
crop_and_resize_images(input_folder, output_folder)