import re
from pyyoutube import Api
import os
import csv
import urllib.request
import re
from videos import get_video_info, download_video, search_video
import openpyxl

api_key = "AIzaSyAK-BlzaRCnoDG6L0RbHp0spMT1htOEsV8" #这是我youtube的key
api = Api(api_key=api_key)

basketball_channels = ['GoldenHoops', 'TristanJass', 'JoshWalker5', 'Hoopaholics', 'OTEATL', 'ClutchPoints', 'OmarESPN', 
'GDsHighlights', 'fingeroll_', 'braxtonpicou', 'TJCyt1', 'kingjetzz', 'SnapBackSports', 'Houseofhighlights', 'Thesosorondo',
'DDSquadstunts', 'BallerClipz', 'ypkraye']
basketball_channels = ['TJCyt1']


anime_channels = ['AniMemes08', 'UzumakiMadara', 'animixed106', 'animeshorts2910', 'animeshorts3852', 'viisual_ice8016', 
'SarotsiX', 'hokage_minato_shorts', 'Pride_Sage', 'CrunchyrollCollection']

def main(channel_type):
    from videos import search_video
    shorts_count = 0

    with open(f'{channel_type}.csv', 'w') as f:
        f.truncate()
        writer = csv.writer(f)
        writer.writerow(['channel_name', 'title', 'thumbnail_url', 'tags', 'done?'])
        f.close()

    excel_path = f'/Users/Tiger/Desktop/videos_storage/{channel_type}.xlsx'
    book = openpyxl.load_workbook(excel_path)
    sheet = book['Sheet1']
    for row in sheet: remove(sheet,row)
    book.save(excel_path)

    if channel_type == 'basketball': channels = basketball_channels
    elif channel_type == 'anime': channels = anime_channels
    else: pass

    for channel in channels:
        shorts_count = get_youtube_shorts(channel, api, shorts_count, channel_type)

    search_video.convert_csv_to_excel(channel_type)

def get_youtube_shorts(channel_name, api, shorts_count, channel_type):
    page_url = 'https://www.youtube.com/@' + channel_name + '/shorts'
    webUrl = urllib.request.urlopen(page_url)
   
    new = re.findall(r'[/][s][h][o][r][t][s][/].+?["]', str(webUrl.read()))
    shorts_ids = []
    for item in new:
        if item != '/shorts/shorts"':
            shorts_ids.append(item[:-1])
    #print(shorts_ids)
    # get the latest video

    #check with record in url_list.txt, if latest, then download
    with open(f'{channel_type}.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        
        for shorts_id in shorts_ids[:15]:
            #print(shorts_id)
            useful_info = get_video_info.get_useful_info(shorts_id[8:], api)
            publishedAt = useful_info['publishedAt']
            
            if search_video.check_update_by_time(publishedAt):
                
                try:
                    path = '/Users/Tiger/Desktop/videos_storage/'
                    folder_name = f'{channel_type}/{str(shorts_count)}/'
                    link = 'https://www.youtube.com' + shorts_id
                    print(link)
                    
                    download_video.download_yt_vid(path, folder_name, link)
                    print('downloaded!')
                    
                    title = useful_info['title']
                    thumbnail_url = useful_info['thumbnail_max']
                    
                    #contentDetails = useful_info['contentDetails']
                    tags = useful_info['tags']
                    
                    writer.writerow([channel_name, title, thumbnail_url, tags, 'nope'])
                    try:
                        download_video.download_image(thumbnail_url, path + folder_name, 'thumbnail.png')
                    except: pass
                    #print(shorts_count, 'hello!')
                   
                    shorts_count += 1

                except:
                    print('shit quality! did not download!')
    f.close()
    
    
    return shorts_count


def remove(sheet, row):
	# iterate the row object
	for cell in row:
		# check the value of each cell in
		# the row, if any of the value is not
		# None return without removing the row
		if cell.value != None:
			return
	# get the row number from the first cell
	# and remove the row
	sheet.delete_rows(row[0].row, 1)

main('anime')
def sports_highlight(path):

    from videos import download_video, get_video_info, divide_video, detect_background_change, search_video
    from audios import get_sub, add_sub
    from login import upload_douyin
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
#sports_highlight(path_2)
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
    






