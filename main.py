import requests
import re
import datetime
import get_video
from pyyoutube import Api

# Daily scraping channel: Golden Hoops
channel = "https://www.youtube.com/channel/UCoDfZzwJNFJ2lVgF41tUX0A"
channel_id = "UCoDfZzwJNFJ2lVgF41tUX0A"
#html = requests.get(channel + "/videos").text

api_key = "AIzaSyAK-BlzaRCnoDG6L0RbHp0spMT1htOEsV8" #这是我youtube的key
api = Api(api_key=api_key)


import download_video
def main():
    # download newest vid into video folder
    video_id = get_video.get_newest_video(channel_id, api)
    download_video.download_video(video_id, '/Users/Tiger/Desktop/GitHub/videos')
    


    # video_by_chart = api.get_videos_by_chart(chart="mostPopular", region_code="US", count=2)
main()

