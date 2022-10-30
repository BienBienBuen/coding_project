# web scraping a specific channel (e.g. Golden Hoops)
#inspiration: https://stackoverflow.com/questions/68101221/how-to-get-notification-when-youtube-channel-uploads-video-in-python

### need regular expression to search for updates

import requests
import re
import datetime
import get_video

if __name__ == '__main__':
    channel = "https://www.youtube.com/channel/UCoDfZzwJNFJ2lVgF41tUX0A"
    channel_id = "UCoDfZzwJNFJ2lVgF41tUX0A"
    html = requests.get(channel + "/videos").text
    
    """
    from pyyoutube import Api
    api_key = "AIzaSyAK-BlzaRCnoDG6L0RbHp0spMT1htOEsV8" #这是我youtube的key
    api = Api(api_key=api_key) 
    """

    #print(channel_info)

    #channel_info = get_video.get_channel_info(channel_id)

    #print(get_video.get_upload(channel_id, 5))

    # video_by_chart = api.get_videos_by_chart(chart="mostPopular", region_code="US", count=2)


