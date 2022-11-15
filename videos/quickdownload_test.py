import yt_dlp
import os
 
ytdl_format_options = {
        'outtmpl': os.path.join('/Users/Tiger/Desktop/GitHub/coding_project/videos/', '%(title)s.%(ext)s'),
        'format': 'mp4',
    }

with yt_dlp.YoutubeDL(ytdl_format_options) as ydl:
        
        ydl.download('https://www.youtube.com/watch?v=fLeJJPxua3E')