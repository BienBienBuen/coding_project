from unicodedata import name
from pyyoutube import Api
import yt_dlp 
import os
#from main import get_newest_video

def download_video(ytid, folder):
    '''
    Given a youtube video id and target folder, this function will download video to that folder
    '''

    ytdl_format_options = {
        'outtmpl': os.path.join(folder, '%(title)s-%(id)s.%(ext)s')
    }

    with yt_dlp.YoutubeDL(ytdl_format_options) as ydl:
        ydl.download('https://www.youtube.com/watch?v=%s' % ytid )
        return True

