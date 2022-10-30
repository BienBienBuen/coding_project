# web scraping a specific channel (e.g. Golden Hoops)
#inspiration: https://stackoverflow.com/questions/68101221/how-to-get-notification-when-youtube-channel-uploads-video-in-python

### need regular expression to search for updates

import requests
import re
import datetime

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


#All available info from channel
def get_channel_info(c_id):
    Channel_by_id = api.get_channel_info(channel_id= c_id)
    Channel_info = Channel_by_id.items[0].to_dict()
    return Channel_info

#从一个specific channel里return a list of video ID
def get_upload(c_id, number):
    info = get_channel_info(c_id)
    playlist_id = info["contentDetails"]["relatedPlaylists"]["uploads"]
    upload_list = api.get_playlist_items(playlist_id = playlist_id)
    videoID = []

    for i in range (number):
        videoID.append(upload_list.items[i].to_dict()["contentDetails"]["videoId"])
    return videoID

def get_newest_video(c_id):
    vid_id = get_upload(c_id, 1)
    return vid_id

channel_info = get_channel_info(channel_id)
print(channel_info)
print(get_upload(channel_id, 5))
# video_by_chart = api.get_videos_by_chart(chart="mostPopular", region_code="US", count=2)

