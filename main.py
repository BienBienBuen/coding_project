import requests
import re
import datetime
from pyyoutube import Api
import os

# Daily scraping channel: Golden Hoops
channel = "https://www.youtube.com/channel/UCoDfZzwJNFJ2lVgF41tUX0A"
channel_id = "UCoDfZzwJNFJ2lVgF41tUX0A"
#channel = "https://www.youtube.com/channel/UCEjOSbbaOfgnfRODEEMYlCw"
#channel_id = "UCEjOSbbaOfgnfRODEEMYlCw"
#channel = "https://www.youtube.com/channel/UC3L9XPe0_FGfRG-CMGtBvFg"
#channel_id = "UC3L9XPe0_FGfRG-CMGtBvFg"
#html = requests.get(channel + "/videos").text

api_key = "AIzaSyAK-BlzaRCnoDG6L0RbHp0spMT1htOEsV8" #这是我youtube的key
api = Api(api_key=api_key)
folder = 'videos'
path_1 = '/Users/bx/Documents/GitHub/coding_project/'
path_2 = '/Users/Tiger/Desktop/GitHub/coding_project/'
#test time_stamps
# time_stamps = [(0, 2), (2, 3), [4,5], [11, 12]] 
time_limit = 300

def sports_highlight(path):
    from videos import download_video, get_video_info, divide_video, detect_background_change, search_video
    from audios import get_sub, add_sub
    from upload import upload_douyin
    # download newest vid into video folder
    video_id = search_video.get_newest_video(channel_id, api)
    #sub = translate.get_subtitle(video_id, path_1)
    print(download_video.download_youtube_video(ytid = video_id, path = path, format = 'mp4'))
    
    #translate video title
    from audios import translate
    title_eng = get_video_info.get_useful_info(video_id, api)['title']
    title_chi = translate.translate(title_eng)
    print(title_chi)
    
    # need the name of the video fronm download_video func
    number_count = len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))])
    vid_name = 'vid' + str(number_count-1) + '.mp4'
    """
    scene_list = detect_background_change.split_video_into_scenes(os.path.join(path, vid_name), threshold=75)
    time_stamps = detect_background_change.standardize_scene_list(scene_list)
    """
    #get subtitle from video
    get_sub.get_sub(video_id=video_id, video_name=vid_name, path = path+"audios_storage/")
    #add subtitles
    add_sub.generate_subtitles(video_path=path+"videos_storage", dest=path,sub_path=path+"audios_storage"+str(number_count-1)+".txt")
    #unload_douyin.upload_douyin()
    """
    divide_video.generate_final_clips(vid_name, time_stamps, time_limit, path)
    """
sports_highlight(path_2)


def motivational_speech(path):
    from audios import add_sub, get_sub, translate, txt_to_list
    from videos import download_video, search_video, get_video_info
    
    # download newest vid into video folder
    video_id = search_video.get_newest_video(channel_id, api)
    #sub = translate.get_subtitle(video_id, path_1)
    download_video.download_video(ytid = video_id, path = path, format = 'mp4')
    
    #translate video title
    title_eng = get_video_info.get_useful_info(video_id, api)['title']
    title_chi = translate.translate(title_eng)
    print(title_chi)

    ### need to work on naming
    get_sub(video_id, title_chi, path+'audios_storage')
    sub_txt_path = path + 'audios_storage' + title_chi + '.txt'
    sub_list = txt_to_list(sub_txt_path, [])
    






