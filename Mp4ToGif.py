from moviepy.editor import VideoFileClip

input_video_path = "input.mp4"  # Replace with your input file path
output_gif_path = "output.gif"  # Replace with your desired output file path

try:
    # Load the video
    video = VideoFileClip(input_video_path)
    
    # Convert to GIF
    video.write_gif(output_gif_path, fps=10)
    print(f"GIF successfully created: {output_gif_path}")
except Exception as e:
    print(f"An error occurred: {e}")
