from unicodedata import name
from pyyoutube import Api
import yt_dlp 
import os
from unidecode import unidecode

#from main import get_newest_video

def download_video(ytid, path, format):
    #check number of files in directory
    number_count = len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))])
    ytdl_format_options = {
        'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
        'format': format
        
    }
    with yt_dlp.YoutubeDL(ytdl_format_options) as ydl:
        url = 'https://www.youtube.com/watch?v=%s' % ytid
        ydl.download(url)
        info_dict = ydl.extract_info(url, download=False)
        video_title = info_dict.get('title', None)
        # title_standardized = unidecode(video_title)
        #info = get_video_info.get_useful_info(ytid, Api)
        #title 有的时候符号下载下来不一样
        # title_standardized1 = video_title.replace('|','｜')
        # title_standardized2 = title_standardized1.replace('?','？')
        # video_name = title_standardized + format
        # numbered_name = 'vid' + str(number_count) + format
        # old_name = os.path.join(path, video_name)
        # new_name = os.path.join(path, numbered_name)  
        
        # try:
        #     os.rename(old_name, new_name)
        # except FileExistsError:
        #     pass

        return True

# test

"""
print(ord("｜"))
print(ord(unidecode("｜")))
print(ord("|"))
z3m7R6Ld6v8
wrMvtIrvdrA
"""
download_video("YLXHARATi-8",'/Users/bx/Documents/GitHub/coding_project/',"mp4")