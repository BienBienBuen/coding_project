from unicodedata import name
from pyyoutube import Api
import yt_dlp 
import os
import get_video_info

#from main import get_newest_video

def download_video(ytid, folder, Api):
    
    #check number of files in directory
    number_count = len([name for name in os.listdir(folder) if os.path.isfile(os.path.join(folder, name))])
    '''
    Given a youtube video id and target folder, this function will download video to that folder
    '''

    ytdl_format_options = {
        'outtmpl': os.path.join(folder, '%(title)s.%(ext)s'),
        'format': 'mp4',
    }

    with yt_dlp.YoutubeDL(ytdl_format_options) as ydl:
        url = 'https://www.youtube.com/watch?v=%s' % ytid
        ydl.download(url)
        
        info_dict = ydl.extract_info(url, download=False)
        video_title = info_dict.get('title', None)
        #info = get_video_info.get_useful_info(ytid, Api)
        #title 有的时候符号下载下来不一样
        title_standardized = video_title.replace('|','｜')
        #title_standardized = video_title.replace('?','？')
        video_name = title_standardized + '.mp4'
        numbered_name = 'vid' + str(number_count) + '.mp4'
        #path_name = '/Users/bx/Documents/GitHub/coding_project/videos/'
        path_name = '/Users/Tiger/Desktop/GitHub/coding_project/videos/'
        old_name = os.path.join(path_name, video_name)
        new_name = os.path.join(path_name, numbered_name)  
        
        try:
            os.rename(old_name, new_name)
        except FileExistsError:
            pass
        
        return True
   
       #/Users/bx/Documents/GitHub/coding_project/videos/Can You Buy An NBA Championship? -B77KZH_1h-A.mp4
    #                                               Can You Buy An NBA Championship？-B77KZH_1h-A

    #/Users/Tiger/Desktop/GitHub/coding_project/videos/Brooklyn Nets vs Chicago Bulls Full Game Highlights | Nov 1, 2022 | FreeDawkins.mp4
                                                   #   Brooklyn Nets vs Chicago Bulls Full Game Highlights ｜ Nov 1, 2022 ｜ FreeDawkins.mp4