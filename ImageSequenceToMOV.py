import ffmpeg
import os

# Define the input and output paths
input_folder = '/InputFolder'  # Folder containing the image sequence
output_file = '/Output.mov'   # Output MOV file

# Ensure the input folder exists
if not os.path.exists(input_folder):
    raise ValueError(f"Input folder '{input_folder}' does not exist.")

# Get a list of images in the input folder
image_files = sorted([img for img in os.listdir(input_folder) if img.endswith(".jpg")])

if not image_files:
    raise ValueError(f"No images found in the folder '{input_folder}'.")

# Assuming the images are named in the pattern Image Sequence_001_0000.jpg, Image Sequence_001_0001.jpg, etc.
input_pattern = os.path.join(input_folder, 'Image Sequence_001_%04d.jpg')

# Create the ffmpeg input object
input_stream = ffmpeg.input(input_pattern, framerate=24)  # Set framerate to 24 or your desired frame rate

# Define the output stream and settings
output_stream = ffmpeg.output(input_stream, output_file, codec='prores')

# Run the ffmpeg command
ffmpeg.run(output_stream)

print(f"Conversion complete. The output file is saved as '{output_file}'.")
