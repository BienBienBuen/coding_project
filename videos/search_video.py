#All available info from channel
def get_channel_info(c_id, api):
    Channel_by_id = api.get_channel_info(channel_id= c_id)
    Channel_info = Channel_by_id.items[0].to_dict()
    return Channel_info

#从一个specific channel里return a list of video ID
def get_upload(c_id, number, api):
    info = get_channel_info(c_id, api)
    playlist_id = info["contentDetails"]["relatedPlaylists"]["uploads"]
    upload_list = api.get_playlist_items(playlist_id = playlist_id)
    videoID = []

    for i in range (number):
        videoID.append(upload_list.items[i].to_dict()["contentDetails"]["videoId"])
    return videoID

def get_newest_video(c_id, api):
    vid_id = get_upload(c_id, 1, api)
    return vid_id[0]

# check videos uploaded in the past week
def check_update_by_time(video_date):
    #standardize datetime to this format: "2022-09-05T03:37:56Z"
    from datetime import datetime, timedelta
    now_date = datetime.now()
    now_date -= timedelta(weeks=1)
    now_date = str(now_date)
    now_date = now_date[0:10]+'T'+ now_date[11:19] +'Z'

    video_year, video_month, video_day, video_hour, video_minute, video_second = int(video_date[0:4]), int(video_date[5:7]), int(video_date[8:10]),int(video_date[11:13]), int(video_date[14:16]), int(video_date[17:19])
    now_year, now_month, now_day, now_hour, now_minute, now_second = int(now_date[0:4]), int(now_date[5:7]), int(now_date[8:10]),int(now_date[11:13]), int(now_date[14:16]), int(now_date[17:19])

    #compare time
    if video_year > now_year: return True
    elif video_year < now_year: return False

    elif video_month > now_month: return True
    elif video_month < now_month: return False

    elif video_day > now_day: return True
    elif video_day < now_day: return False

    elif video_hour > now_hour: return True
    elif video_hour < now_hour: return False

    elif video_minute > now_minute: return True
    elif video_minute < now_minute: return False

    elif video_second > video_second: return True
    elif video_second < now_second: return False

def check_shorts_update(channel_name, new):
    with open('url_list.txt', 'r') as fin:
        info = fin.readlines()
        fin.close()
    for i in range(len(info)):
        if info[i][0:len(channel_name)] == channel_name:
            if info[i][len(channel_name)+2:].strip() == new:
                return False
            else:
                info[i] = channel_name + ': ' + new + '\n'
                print(info)
                with open('url_list.txt', 'w') as fin:
                    for line in info:
                        fin.write(line)
                return True

def convert_csv_to_excel(channel_type):
    import pandas as pd
    csv = pd.read_csv(f'{channel_type}.csv')
    excelWriter = pd.ExcelWriter(f'/Users/Tiger/Desktop/videos_storage/{channel_type}.xlsx')
    csv.to_excel(excelWriter)
    excelWriter.save()

""""""
from pyyoutube import Api
api_key = "AIzaSyAK-BlzaRCnoDG6L0RbHp0spMT1htOEsV8" #这是我youtube的key
api = Api(api_key=api_key)
""""""
#print(check_update_by_time('2022-11-26T20:52:35Z'))

