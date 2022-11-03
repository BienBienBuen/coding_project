from unicodedata import name
from pyyoutube import Api
import yt_dlp 
import os
import get_video_info

#from main import get_newest_video

def download_video(ytid, path, Api):
    
    #check number of files in directory
    number_count = len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))])
    '''
    Given a youtube video id and target folder, this function will download video to that folder
    '''

    ytdl_format_options = {
        'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
        'format': 'mp4',
    }

    with yt_dlp.YoutubeDL(ytdl_format_options) as ydl:
        url = 'https://www.youtube.com/watch?v=%s' % ytid
        ydl.download(url)
        info_dict = ydl.extract_info(url, download=False)
        video_title = info_dict.get('title', None)
        #info = get_video_info.get_useful_info(ytid, Api)
        #title 有的时候符号下载下来不一样
        title_standardized1 = video_title.replace('|','｜')
        title_standardized2 = title_standardized1.replace('?','？')
        video_name = title_standardized2 + '.mp4'
        numbered_name = 'vid' + str(number_count) + '.mp4'
        old_name = os.path.join(path, video_name)
        new_name = os.path.join(path, numbered_name)  
        
        try:
            os.rename(old_name, new_name)
        except FileExistsError:
            pass
        
        return True
   
       #/Users/bx/Documents/GitHub/coding_project/videos/Can You Buy An NBA Championship? -B77KZH_1h-A.mp4
    #                                               Can You Buy An NBA Championship？-B77KZH_1h-A

    #/Users/Tiger/Desktop/GitHub/coding_project/videos/Brooklyn Nets vs Chicago Bulls Full Game Highlights | Nov 1, 2022 | FreeDawkins.mp4
                                                   #   Brooklyn Nets vs Chicago Bulls Full Game Highlights ｜ Nov 1, 2022 ｜ FreeDawkins.mp4
