import requests
import re
import datetime
import search_video
from pyyoutube import Api
import os

# Daily scraping channel: Golden Hoops
#channel = "https://www.youtube.com/channel/UCoDfZzwJNFJ2lVgF41tUX0A"
#channel_id = "UCoDfZzwJNFJ2lVgF41tUX0A"
channel = "https://www.youtube.com/channel/UCEjOSbbaOfgnfRODEEMYlCw"
channel_id = "UCEjOSbbaOfgnfRODEEMYlCw"
#channel = "https://www.youtube.com/channel/UC3L9XPe0_FGfRG-CMGtBvFg"
#channel_id = "UC3L9XPe0_FGfRG-CMGtBvFg"
#html = requests.get(channel + "/videos").text

api_key = "AIzaSyAK-BlzaRCnoDG6L0RbHp0spMT1htOEsV8" #这是我youtube的key
api = Api(api_key=api_key)
folder = 'videos'
path_1 = '/Users/bx/Documents/GitHub/coding_project/videos/'
path_2 = '/Users/Tiger/Desktop/GitHub/coding_project/videos/'
#test time_stamps
# time_stamps = [(0, 2), (2, 3), [4,5], [11, 12]] 
time_limit = 30
import download_video
import get_video_info
import divide_video1
import detect_background_change
import get_video_info
import translate

def main():
    # download newest vid into video folder
    video_id = search_video.get_newest_video(channel_id, api)
    sub = translate.get_subtitle(video_id, path_1)
    # download_video.download_video(ytid = video_id, folder = path_1, Api = api)
    

    #translate video title
    title_eng = get_video_info.get_useful_info(video_id, api)
    title_chi = get_video_info.translate(title_eng)
    print(title_chi)

    # need the name of the video fronm download_video func
    number_count = len([name for name in os.listdir(path_1) if os.path.isfile(os.path.join(path_1, name))])
    vid_name = 'vid' + str(number_count-1) + '.mp4'
    # print(vid_name)
    scene_list = detect_background_change.split_video_into_scenes(os.path.join(path_1, vid_name), threshold=75)
    time_stamps = detect_background_change.standardize_scene_list(scene_list)

    # divide_video1.generate_final_clips(vid_name, time_stamps, time_limit)
    
    translate.generate_subtitles()

main()


# 直接将motivational speech的稿子翻译成中文然后放原来的sound track
# english sound track + 中文文案