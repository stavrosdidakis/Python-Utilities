import os
import sys
from moviepy.editor import ImageClip, concatenate_videoclips, vfx

def crop_to_1920x1080(img_clip):
    """
    Resizes the image so that it covers at least 1920x1080,
    then crops the overflow from the center to get exactly 1920x1080.
    """
    target_w, target_h = 1920, 1080
    target_aspect = target_w / target_h

    # Current image dimensions
    w, h = img_clip.size
    current_aspect = w / h

    # 1. Resize so that the image is at least 1920 wide or 1080 high
    #    depending on which dimension is limiting.
    if current_aspect > target_aspect:
        # Image is relatively wider than 16:9 => match height first
        # so we definitely cover 1080 in height
        resized_clip = img_clip.resize(height=target_h)
        # Now we have at least 1080 in height, and possibly more than 1920 in width
    else:
        # Image is relatively taller or same => match width first
        # so we definitely cover 1920 in width
        resized_clip = img_clip.resize(width=target_w)
    
    # After resize, the image may exceed 1920x1080 in the other dimension
    # 2. Center-crop to exactly 1920x1080
    cropped_clip = resized_clip.fx(
        vfx.crop,
        width=target_w,
        height=target_h,
        x_center=resized_clip.w / 2,
        y_center=resized_clip.h / 2
    )
    
    return cropped_clip

def create_slideshow(
    folder_path, 
    output_path="output_video.mp4", 
    duration=2, 
    size=(1920, 1080)
):
    """
    Create a slideshow video from images in a folder, 
    cropping them to exactly 1920x1080 if needed.
    """
    # 1. Gather valid image files
    valid_extensions = (".png", ".jpg", ".jpeg", ".bmp", ".gif")
    image_files = [
        os.path.join(folder_path, f)
        for f in sorted(os.listdir(folder_path))
        if f.lower().endswith(valid_extensions)
    ]

    if not image_files:
        print("No valid images found in the folder:", folder_path)
        return

    # 2. Build clips
    clips = []
    for img_path in image_files:
        # Create an ImageClip
        clip = ImageClip(img_path, duration=duration)
        
        # Crop/resize to 1920x1080
        clip_1920x1080 = crop_to_1920x1080(clip)

        # Append to list
        clips.append(clip_1920x1080)

    # 3. Concatenate all ImageClips
    final_clip = concatenate_videoclips(clips, method="compose")

    # 4. Write the output video
    final_clip.write_videofile(output_path, fps=30)

if __name__ == "__main__":
    """
    Example usage:
        python create_slideshow.py /path/to/images output.mp4 2
    """
    if len(sys.argv) < 2:
        print("Usage: python create_slideshow.py <folder_path> [output_path] [duration]")
        sys.exit(1)

    folder = sys.argv[1]
    out_file = sys.argv[2] if len(sys.argv) > 2 else "output_video.mp4"
    dur = float(sys.argv[3]) if len(sys.argv) > 3 else 2

    create_slideshow(folder, out_file, dur, (1920, 1080))
