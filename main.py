import requests
import re
import datetime
import search_video
from pyyoutube import Api
import os

# Daily scraping channel: Golden Hoops
# channel = "https://www.youtube.com/channel/UCoDfZzwJNFJ2lVgF41tUX0A"
# channel_id = "UCoDfZzwJNFJ2lVgF41tUX0A"
#channel = "https://www.youtube.com/channel/UCEjOSbbaOfgnfRODEEMYlCw"
#channel_id = "UCEjOSbbaOfgnfRODEEMYlCw"
channel = "https://www.youtube.com/channel/UC3L9XPe0_FGfRG-CMGtBvFg"
channel_id = "UC3L9XPe0_FGfRG-CMGtBvFg"
#html = requests.get(channel + "/videos").text

api_key = "AIzaSyAK-BlzaRCnoDG6L0RbHp0spMT1htOEsV8" #这是我youtube的key
api = Api(api_key=api_key)
folder = 'videos'
path_1 = '/Users/bx/Documents/GitHub/coding_project/videos/'
path_2 = '/Users/Tiger/Desktop/GitHub/coding_project/videos/'
#test time_stamps
# time_stamps = [(0, 2), (2, 3), [4,5], [11, 12]] 
time_limit = 700
import download_video
import get_video_info
import divide_video1
import detect_background_change

def main(user):
    # download newest vid into video folder

    video_id = search_video.get_newest_video(channel_id, api)
    print(video_id)
    download_video.download_video(ytid = video_id, folder = 'videos', Api = api)
    # video_by_chart = api.get_videos_by_chart(chart="mostPopular", region_code="US", count=2)
    
    # need the name of the video fronm download_video func
    number_count = len([name for name in os.listdir(folder) if os.path.isfile(os.path.join(folder, name))])
    vid_name = 'vid' + str(number_count-1) + '.mp4'

    scene_list = detect_background_change.split_video_into_scenes(os.path.join(path_1, vid_name), threshold=90)
    time_stamps = detect_background_change.standardize_scene_list(scene_list)

    print(time_stamps)
    divide_video1.generate_final_clips(vid_name, time_stamps, time_limit)

main('Tiger')


