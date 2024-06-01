from PIL import Image

# Open the long image
input_image_path = 'path/image.png'  # Replace with your image path
long_image = Image.open(input_image_path)

# Dimensions of the long image
long_image_width, long_image_height = long_image.size

# Desired dimensions of each screenshot
screenshot_width = 1024
screenshot_height = 1024

# Calculate the number of screenshots
num_screenshots = long_image_height // screenshot_height
if long_image_height % screenshot_height != 0:
    num_screenshots += 1

# Create the screenshots
for i in range(num_screenshots):
    left = 0
    upper = i * screenshot_height
    right = screenshot_width
    lower = (i + 1) * screenshot_height
    
    if lower > long_image_height:
        lower = long_image_height
    
    # Crop the image to the current screenshot dimensions
    screenshot = long_image.crop((left, upper, right, lower))
    
    # Save the screenshot
    screenshot.save(f'screenshot_{i + 1}.png')

print(f'{num_screenshots} screenshots created.')
