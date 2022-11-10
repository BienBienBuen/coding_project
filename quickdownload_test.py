import yt_dlp
import os
 
path_1 = '/Users/bx/Documents/GitHub/coding_project/videos/'
path_2 = '/Users/Tiger/Desktop/GitHub/coding_project/videos/'

ytdl_format_options = {
        'outtmpl': os.path.join(path_1, '%(title)s.%(ext)s'),
        'format': 'mp4',
    }

with yt_dlp.YoutubeDL(ytdl_format_options) as ydl:
        
        ydl.download('https://www.youtube.com/watch?v=fLeJJPxua3E')