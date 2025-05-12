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

### 🎬 GetYTSubs
Extracts and cleans subtitle text from a YouTube subtitle JSON file (`fx.txt`) and writes it to `extracted_text.txt`.
1.	Open YouTube video link. Turn On Subtitles/Closed Captions
2.	Open Developer Tools (Chrome: View Inspect)
3.	Open Network tab, and paste `timedtext` inside `Filter`. Copy the `Request URL` content and paste it into the URL of a new browser window.
4.	Pass the downloaded file into the `getSubs.py` code (run using python, make sure that the directory of the file and the script are the same)
5.	You will receive a new `extracted_text.txt` file (in the same directory)

### 🖼️ ImageSequenceToMOV
Takes a sequence of images (named like `Image Sequence_001_0000.jpg`, etc.) and compiles them into a `.mov` video using FFmpeg with ProRes encoding.

### 🎞 Mp4ToGif
Converts an MP4 video into a GIF using `moviepy`. Adjustable framerate (default 10 fps).

### 🧹 RemoveDuplicateWords
Reads a list of words from a file and removes any duplicates while preserving the original order. Outputs to a new file.

### 🧩 SplitLongImage
Splits a vertically long image into a series of equally sized (1024x1024) image tiles.

---

## Setup

- Install dependencies:
  ```bash
  pip install pillow moviepy ffmpeg-python
  sudo apt install unoconv  # for BatchWordToPDF
