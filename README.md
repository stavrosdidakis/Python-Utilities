
# Python Utilities

A collection of Python scripts for automating common creative and productivity tasks related to image processing, file conversion, video editing, and more.

---

## Scripts Overview

### 📐 BatchImageCrop
Crops images to a square centered region and resizes them to a specified size (default 1024x1024). Supports `.png`, `.jpg`, `.jpeg`, `.bmp`, `.gif`.

### 📝 BatchWordToPDF
Recursively converts `.doc` and `.docx` files in a folder into `.pdf` format using `unoconv`. Maintains the original folder structure.

### ⏱️ Counter
A simple countdown timer to assist with presentations. Each presenter gets a 1-minute timer.

### 🎬 CreateSlideshow
Generates a slideshow video from a folder of images. Images are automatically cropped to fit exactly **1920x1080** resolution, centered for best visual presentation. Uses `moviepy` for video generation.

**Usage:**
\`\`\`bash
python create_slideshow.py <folder_path> [output_path] [duration]
\`\`\`
- **folder_path**: Path to the folder containing images.
- **output_path**: Name of the output video file (default: \`output_video.mp4\`).
- **duration**: Duration (in seconds) for each image (default: \`2\`).

Example:
\`\`\`bash
python create_slideshow.py ./images slideshow.mp4 3
\`\`\`

### 🎬 GetYTSubs
Extracts and cleans subtitle text from a YouTube subtitle JSON file (\`fx.txt\`) and writes it to \`extracted_text.txt\`.
1. Open YouTube video link and enable subtitles/CC.
2. Open Developer Tools (Chrome: View → Inspect).
3. Open Network tab, filter with \`timedtext\`, and copy the request URL.
4. Download the subtitle JSON file from that URL.
5. Run the script with the subtitle file in the same directory.

### 🎞 Mp4ToGif
Converts an MP4 video into a GIF using \`moviepy\`. Adjustable framerate (default 10 fps).

### 🖼️ ImageSequenceToMOV
Takes a sequence of images (named like \`Image Sequence_001_0000.jpg\`, etc.) and compiles them into a \`.mov\` video using FFmpeg with ProRes encoding.

### 🧹 RemoveDuplicateWords
Reads a list of words from a file and removes any duplicates while preserving the original order. Outputs to a new file.

### 🧩 SplitLongImage
Splits a vertically long image into a series of equally sized (1024x1024) image tiles.

---

## Setup

Install dependencies:
\`\`\`bash
pip install pillow moviepy ffmpeg-python
sudo apt install unoconv  # for BatchWordToPDF
\`\`\`
