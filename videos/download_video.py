from unicodedata import name
from pyyoutube import Api
import yt_dlp 
import os
from unidecode import unidecode
from TikTokAPI import TikTokAPI
from csv import DictReader
#from main import get_newest_video

def download_youtube_video(ytid, path, format):
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
if __name__ == "__main__":
    download_youtube_video('FKSKIfapQns', './videos_storage/', 'mp4')
# pip install PyTikTokAPI

def tiktok_api(cookie_path):
    dict = {}
    with open(cookie_path, 'r') as fin:
        key, value = fin.readline().split()
        dict[key] = value
    api = TikTokAPI(cookie=dict)
    return api
    
def download_tiktok_video(api, number, output_path):
    retval = api.getTrending(count=number)
    video_list = []
    for n in range(number):
        video_id = retval['items'][n]['id']
        description = retval['items'][n]['desc']
        video_list.append((video_id, description))
    print(video_list)
    """
    for n in number:
        api.downloadVideoById(video_id=video_list[n][0], save_path= output_path + str(video_list[n][0]) + '.mp4', )
    """

#api = TikTokAPI()
#download_tiktok_video(api, 5, './coding_project/videos_storage/')

def download_tiktok_video_by_ID(api, video_id):
    s = api.getVideoById(video_id='7109188785673473323')

    thumb_url = s['itemInfo']['itemStruct']['video']['cover']
    id = s['itemInfo']['itemStruct']['video']['id']

    api.downloadVideoById(video_id=id, save_path= './coding_project/videos_storage/14.mp4' )
    import urllib.request
    urllib.request.urlretrieve(thumb_url, f'./coding_project/videos_storage/{id}.jpg')

import moviepy.editor as mp
from PIL import Image
def add_images(input_path, image_path):
    video = mp.VideoFileClip(input_path)
    print(video.duration)
    n = Image.open(image_path)
    
    logo1 = (mp.ImageClip(image_path)
            .set_duration(video.duration)
            .resize(height=50) # if you need to resize...
            .margin(right=8, top=8, opacity=0) # (optional) logo-border padding
            .set_pos(("left","top")))
    logo2 = (Image.open(image_path)
            .set_duration(video.duration)
            .resize(height=50) # if you need to resize...
            .margin(right=8, top=8, opacity=0) # (optional) logo-border padding
            .set_pos(("right","top")))

    final = mp.CompositeVideoClip([video, logo1, logo2])
    final.write_videofile("edited.mp4")

#add_images('./coding_project/videos_storage/14.mp4', './coding_project/videos_storage/heart.jpg')
path = './coding_project/videos_storage/'
vid_name = 'dance'
link = 'https://www.youtube.com/watch?v=5ggNjBIs3h0'

from pytube import YouTube
yt = YouTube(link)
vid = yt.streams.filter(progressive=True, file_extension='mp4', custom_filter_functions=[lambda s: (s.resolution == '1080p') or (s.resolution == '720p')]).first()
vid.download(path+ vid_name)