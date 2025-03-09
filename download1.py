import os
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi

# Function to download video
def download_video(video_id, video_output_path):
    if not os.path.exists(video_output_path):
        os.makedirs(video_output_path)

    url = f'https://www.youtube.com/watch?v={video_id}'
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(video_output_path)
        print(f'Successfully downloaded: {yt.title}')
    except Exception as e:
        print(f"An error occurred while downloading video {video_id}: {str(e)}")

# Function to download captions
def download_captions(video_id, captions_output_path):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        if not os.path.exists(captions_output_path):
            os.makedirs(captions_output_path)
        with open(os.path.join(captions_output_path, f'{video_id}.txt'), 'w', encoding='utf-8') as f:
            for entry in transcript:
                f.write(f"{entry['start']} --> {entry['start'] + entry['duration']}\n{entry['text']}\n\n")
        print(f"Downloaded captions for video: {video_id}")
    except Exception as e:
        print(f"An error occurred while downloading captions for video {video_id}: {str(e)}")

# Function to read video IDs from a text file
def read_video_ids(file_path):
    with open(file_path, 'r') as file:
        video_ids = [line.strip() for line in file.readlines()]
    return video_ids

# Main function to download videos and captions
def download_videos_and_captions(ids_file_path, videos_output_path, captions_output_path):
    video_ids = read_video_ids(ids_file_path)
    for video_id in video_ids:
        download_video(video_id, videos_output_path)
        download_captions(video_id, captions_output_path)

# Paths
ids_file_path = '.../youtube_asl_video_ids.txt'  # Path to the text file containing video IDs
videos_output_path = '...'  # Folder to save downloaded videos
captions_output_path = '...'  # Folder to save downloaded captions

# Execute the download process
download_videos_and_captions(ids_file_path, videos_output_path, captions_output_path)



