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

Channel_by_id = api.get_channel_info(channel_id= channel_id)
print(Channel_by_id.items[0].to_dict()) 

