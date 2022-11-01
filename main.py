import requests
import re
import datetime
import search_video
from pyyoutube import Api

# Daily scraping channel: Golden Hoops
# channel = "https://www.youtube.com/channel/UCoDfZzwJNFJ2lVgF41tUX0A"
# channel_id = "UCoDfZzwJNFJ2lVgF41tUX0A"
channel = "https://www.youtube.com/channel/UCEjOSbbaOfgnfRODEEMYlCw"
channel_id = "UCEjOSbbaOfgnfRODEEMYlCw"
#html = requests.get(channel + "/videos").text

api_key = "AIzaSyAK-BlzaRCnoDG6L0RbHp0spMT1htOEsV8" #这是我youtube的key
api = Api(api_key=api_key)

#test time_stamps
time_stamps = [(0, 2), (2, 3), [4,5], [11, 12]] 
time_limit = 2
import download_video
import get_video_info
import divide_video1

def main(user):
    # download newest vid into video folder

    video_id = search_video.get_newest_video(channel_id, api)
    print(video_id)
    download_video.download_video(ytid = video_id, folder = 'videos', Api = api)
    # video_by_chart = api.get_videos_by_chart(chart="mostPopular", region_code="US", count=2)
    
    # need the name of the video fronm download_video func
    #divide_video1.generate_final_clips(, time_stamps, time_limit)
main('Tiger')


