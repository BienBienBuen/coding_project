import requests
import re
import datetime
import search_video
from pyyoutube import Api

# Daily scraping channel: Golden Hoops
channel = "https://www.youtube.com/channel/UCoDfZzwJNFJ2lVgF41tUX0A"
channel_id = "UCoDfZzwJNFJ2lVgF41tUX0A"
#html = requests.get(channel + "/videos").text

api_key = "AIzaSyAK-BlzaRCnoDG6L0RbHp0spMT1htOEsV8" #这是我youtube的key
api = Api(api_key=api_key)


import download_video
import get_video_info

def main(user):
    # download newest vid into video folder

    video_id = search_video.get_newest_video(channel_id, api)
    print(video_id)
    #download_video.download_video(video_id, f'/Users/{user}/Desktop/GitHub/videos')
    
    video_length = get_video_info.get_video_length(video_id, api)
    print(video_length)
    # video_by_chart = api.get_videos_by_chart(chart="mostPopular", region_code="US", count=2)
main('Tiger')

