from unicodedata import name
from pyyoutube import Api
import yt_dlp 
import os
import get_video_info

#from main import get_newest_video
count = 0
def download_video(ytid, folder, Api):
    download_count = count
    '''
    Given a youtube video id and target folder, this function will download video to that folder
    '''

    ytdl_format_options = {
        'outtmpl': os.path.join(folder, '%(title)s-%(id)s.%(ext)s')
    }

    with yt_dlp.YoutubeDL(ytdl_format_options) as ydl:
        ydl.download('https://www.youtube.com/watch?v=%s' % ytid )

        info = get_video_info.get_useful_info(ytid, Api)
        title_standardized = info['title'].replace('|','｜')
        video_name = title_standardized + '-' + ytid + '.webm'
        numbered_name = 'vid' + str(download_count) + '.mp4'
        path_name = '/Users/bx/Documents/GitHub/coding_project/videos/'
        old_name = os.path.join(path_name, video_name)
        new_name = os.path.join(path_name, numbered_name)  
        try:
            os.rename(old_name, new_name)
        except FileExistsError:
            download_count += 1
            os.rename(old_name, new_name)
        return True