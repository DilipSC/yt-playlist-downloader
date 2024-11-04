from yt_dlp import YoutubeDL

def download_video(video_url, base_download_folder='downloads'):
    # Set up options for downloading each video into a separate folder
    ydl_opts = {
        'format': 'bestvideo[height<=1080]+bestaudio/best',  # 1080p video and best audio available
        'outtmpl': f'{base_download_folder}/%(title)s/%(title)s.%(ext)s',  # Each video in its own folder
        'ignoreerrors': True,  # Skip errors for unavailable videos
        'merge_output_format': 'mp4',  # Merge audio and video into an MP4 file
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4'  # Ensures the final output is in MP4 format
        }]
    }
    
    # Initialize the downloader with options
    with YoutubeDL(ydl_opts) as ydl:
        print(f"Downloading video: {video_url} into separate folder")
        ydl.download([video_url])

# Replace with the URL of your YouTube video
video_url = input("Enter YouTube video URL: ")
base_download_folder = 'my_youtube_downloads'  # Specify base folder name or path as desired
download_video(video_url, base_download_folder)
