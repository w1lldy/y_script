# YouTube Video Downloader Script

This Python script downloads videos from YouTube along with English subtitles. The video and subtitles are merged into an MP4 file, using `yt-dlp` and `FFmpeg` for processing. The downloaded video can then be transferred to another machine via SSH.

## Prerequisites

### Requirements:
- **Unrestricted access to YouTube:** Ensure that your network setup allows for unhindered access to YouTube.
- **yt-dlp and FFmpeg:** Install `yt-dlp` and `FFmpeg` before using this script. You can install them via `pip` and your package manager:

  ```bash
  pip install yt-dlp
  sudo apt install ffmpeg  # For Linux-based systems
  ```
- Python 3.x installed on your machine.

Usage
Run the script via the terminal/console. When prompted, input the URL of the YouTube video you want to download:
 ```bash
python3 YOUscript.py
```
The script will:

Download the video in the best available quality.
Fetch and embed English subtitles into the video file.
Save the video as an .mp4 file.
Note: The script currently only works through a console interface.

###SSH Transfer
The feature to transfer the downloaded video to a remote machine via SSH is included but commented out. You can enable it by uncommenting the relevant lines in the script.

###Future Development Plans
In future releases, the script will include:

A graphical interface to enhance user experience.
An option to select the video quality before downloading.
More customization options, such as selecting different subtitle languages and output formats.
Stay tuned for updates!

###License
This project is open-source under the MIT License. (PS. I don't know what the license is, but everyone uses it :))
Let me know if you need any changes!
