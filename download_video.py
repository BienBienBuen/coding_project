from unicodedata import name
from pyyoutube import Api
import yt_dlp 
import os
import get_video_info

#from main import get_newest_video
def download_video(ytid, folder, Api):
    download_count = 1
    '''
    Given a youtube video id and target folder, this function will download video to that folder
    '''

    ytdl_format_options = {
        'outtmpl': os.path.join(folder, '%(title)s-%(id)s.%(ext)s')
    }

    with yt_dlp.YoutubeDL(ytdl_format_options) as ydl:
        ydl.download('https://www.youtube.com/watch?v=%s' % ytid )
        """
        info = get_video_info.get_useful_info(ytid, Api)
        #title 有的时候符号下载下来不一样
        title_standardized = info['title'].replace('|','｜')
        #yt-dlp下载视频名字的format是webm,要改成mp4
        video_name = title_standardized + '-' + ytid + '.webm'
        numbered_name = 'vid' + str(download_count) + '.mp4'
        #path_name = '/Users/bx/Documents/GitHub/coding_project/videos/'
        path_name = '/Users/Tiger/Desktop/GitHub/coding_project/videos/'
        old_name = os.path.join(path_name, video_name)
        new_name = os.path.join(path_name, numbered_name)  

        try:
            os.rename(old_name, new_name)
        except FileExistsError:

            while FileExistsError:
                download_count += 1
                new_numbered_name = 'vid' + str(download_count) + '.mp4'
                os.rename(old_name, os.path.join(path_name, new_numbered_name))

            count = download_count
        """
        return True