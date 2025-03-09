# YouTube Video and Caption Downloader

This Python script allows me to download YouTube videos and their corresponding captions (subtitles) using video IDs. It is particularly useful for collecting video data for research, analysis, or archival purposes.

---

## Features
- **Download YouTube Videos**: Downloads videos in the highest available resolution.
- **Download Captions**: Fetches and saves captions (subtitles) for the videos.
- **Batch Processing**: Reads a list of video IDs from a text file and processes them in bulk.
- **Error Handling**: Handles exceptions during video and caption downloads gracefully.

---

## Requirements
To run this script, you need the following Python libraries:
- `pytube`: For downloading YouTube videos.
- `youtube_transcript_api`: For fetching video captions.

You can install the required libraries using pip:
```bash
pip install pytube youtube-transcript-api