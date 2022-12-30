from unicodedata import name
import yt_dlp 
import os
from TikTokApi import TikTokApi
import requests

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

#download_youtube_video('5ggNjBIs3h0', './coding_project/videos_storage/', 'mp4')
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

def download_yt_vid(path, link, filename):
    from pytube import YouTube
    yt = YouTube(link)
    vid = yt.streams.get_highest_resolution()
    vid.download(path, filename= filename + '.mp4')
    #vid = yt.streams.filter(only_audio= True).first()
    #vid.download(output_path = path, filename= filename + '_audio.mp4')

def download_image(image_url, output_path, name):
    img_data = requests.get(image_url).content
    with open(output_path + name, 'wb') as handler:
        handler.write(img_data)



path = '/Users/Tiger/Desktop/videos_storage/'
folder_name = ''
link = 'https://www.youtube.com/shorts/DoXDAfLse6Q'

download_yt_vid(path + folder_name, link, '2')

def download_insta_vids(username, number_of_vids):
    from pathlib import Path
    from instaloader import Instaloader, Profile 
    L = Instaloader()
    PROFILE = username #instagram username for profile you want to download data
    profile = Profile.from_username(L.context, PROFILE)
    posts_sorted_by_likes = sorted(profile.get_posts(), key=lambda post: post.date,reverse=True)
    videos = []
    for post in posts_sorted_by_likes:
        if post.is_video: videos.append(post)

    video_selected = videos[0:number_of_vids] #to download from only 2 posts
    #for post in video_selected:
     #   L.download_post(post, Path(f'/Users/Tiger/Desktop/videos_storage/{username}'))
    L.login(user='xiaokangzou9', passwd='s?C?2t9F$AXAjx$')
    L.download_stories(userids = [19410587], filename_target = Path(f'/Users/Tiger/Desktop/videos_storage/{username} stories'))

#download_insta_vids('zo', 3)