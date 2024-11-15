import yt_dlp


def download_youtube_video(url, output_path='./downloads'):
    ydl_opts = {
        # Prefer MP4
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'merge_output_format': 'mp4'  # Force MP4 as output format
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


# Example usage
download_youtube_video('https://www.youtube.com/watch?v=hPSsPCNxta4')
