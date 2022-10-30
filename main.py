# web scraping a specific channel (e.g. Golden Hoops)
#inspiration: https://stackoverflow.com/questions/68101221/how-to-get-notification-when-youtube-channel-uploads-video-in-python

### need regular expression to search for updates

import requests
import re

channel = "https://www.youtube.com/channel/UCoDfZzwJNFJ2lVgF41tUX0A"
channel_id = "UCoDfZzwJNFJ2lVgF41tUX0A"
html = requests.get(channel + "/videos").text

# scrape specific info ( ' ' 里面的是regular expression，我还没去看),这里可以用来实现自动检测upload，然后下载视频
# https://docs.python.org/3/library/re.html
# info = re.search('(?<={"label":").*?(?="})', html).group()
# date = re.search('\d+ \w+ ago.*seconds ', info).group()



# Using pyyoutube library to get data from Goolden Hoops channel
#inspiration: https://pypi.org/project/python-youtube/

from pyyoutube import Api

api_key = "AIzaSyAK-BlzaRCnoDG6L0RbHp0spMT1htOEsV8" #这是我youtube的key
api = Api(api_key=api_key) 

#从一个specific channel里return a list of videos
def get_playist_from_channel(c_id):
    list_by_channel = api.get_playlists(channel_id=c_id)
    playlist = list_by_channel
    return playlist

def get_video_info(c_id):
    Channel_by_id = api.get_channel_info(channel_id= c_id)
    Channel_info = Channel_by_id.items[0].to_dict()
    return Channel_info

print(get_video_info(channel_id)) 
print(get_playist_from_channel(channel_id))
video_by_chart = api.get_videos_by_chart(chart="mostPopular", region_code="US", count=2)

