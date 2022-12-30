import re
from pyyoutube import Api
import os
import csv
import urllib.request
import re
from videos import get_video_info, download_video, search_video, detect_background_change, divide_video
import openpyxl

api_key = "AIzaSyAK-BlzaRCnoDG6L0RbHp0spMT1htOEsV8" 
api = Api(api_key=api_key)

NBA_channels = ['GoldenHoops',
'GDsHighlights', 'fingeroll_', 'TJCyt1', 'kingjetzz', 'SnapBackSports', 'Houseofhighlights', 'SwishCultures', 'NBAOnFire-', 'Jnglert']

basketball_youtuber_channels = ['JoshWalker5', 'braxtonpicou', 'dexton4'
 'Thesosorondo', 'RealJDub', 'ChrisStaplesDunker', 'seggie', 'R2bball', 'JumpmanJimmy', 'Maxisnicee', 'simonssaysjax']
basketball_youtuber_channels = ['afv']
basketball_podcasts = []

basketball_highlight_channels = ['PureSweat', 'OTEATL', 'killerjunior23', 'TristanJass', 'DunkademicsOfficial', 'R2bball', 'jlawbball7293', 'ChrisJohnsonHoops',
 'Overtime', 'Maxisnicee', 'EliteMixtapes', 'ShowtimeFilms', 'lakers' ]

anime_channels = ['AniMemes08', 'UzumakiMadara', 'animixed106', 'animeshorts2910', 'animeshorts3852', 'viisual_ice8016', 
'SarotsiX', 'hokage_minato_shorts', 'CrunchyrollCollection', 'upsidedownart09', 'Animeme_TV', 'ouranimax8661']

anime_channels = ['animixed106', 'animeshorts2910', 'animeshorts3852', 'hokage_minato_shorts', 'upsidedownart09', 
'ouranimax8661', '_Namikaze_Naruto', 'leang_vengse_anime_edit', 'hmmYeahIDK']

def main(channel_type, number_of_vids, type, scene_cut):
    from videos import search_video
    with open(f'{channel_type}.csv', 'w') as f:
        f.truncate()
        writer = csv.writer(f)
        writer.writerow(['channel_name', 'title', 'thumbnail_url', 'tags', 'done?', 'uploaded?'])
        f.close()

    excel_path = f'/Users/Tiger/Desktop/videos_storage/{channel_type}.xlsx'
    book = openpyxl.load_workbook(excel_path)
    sheet = book['Sheet1']
    for row in sheet: remove(sheet,row)
    book.save(excel_path)
   
    if channel_type == 'NBA_channels': channels = NBA_channels      
    elif channel_type == 'basketball_youtuber_channels': channels = basketball_youtuber_channels

    elif channel_type == 'basketball_highlight_channels': channels = basketball_highlight_channels
    elif channel_type == 'anime': channels = anime_channels
    else: pass

    shorts_collection = []
    for channel in channels:
        get_youtube_shorts(channel, api, shorts_collection, type)
        print('getting videos...')
    #print(shorts_collection)
    shorts_collection = (sorted(shorts_collection, key = lambda x : int(x[1]), reverse=True))[:number_of_vids]
    print(shorts_collection)
    download_shorts(shorts_collection, channel_type, api, type, scene_cut)

    search_video.convert_csv_to_excel(channel_type)

def get_youtube_shorts(channel_name, api, shorts_collection, type):
    page_url = 'https://www.youtube.com/@' + channel_name + f'/{type}'
    webUrl = urllib.request.urlopen(page_url)
    
    if type == 'shorts':
        new = re.findall(r'[/][s][h][o][r][t][s][/].+?["]', str(webUrl.read()))
        shorts_ids = []
        for item in new:
            if item != '/shorts/shorts"':
                shorts_ids.append(item[:-1])
        
        for shorts_id in shorts_ids:
            useful_info = get_video_info.get_useful_info(shorts_id[8:], api)
            publishedAt = useful_info['publishedAt']
            statistics = useful_info['statistics']
            #if search_video.check_update_by_time(publishedAt):
            if True:
                shorts_collection.append((shorts_id[8:], statistics, channel_name)) 

    else:
        new = re.findall(r'["][v][i][d][e][o][I][d][s]["][:][[]["](.+?)["]', str(webUrl.read()))
        videos_ids = []
        for item in new:
            if item not in videos_ids:
                videos_ids.append(item)
   
        for video_id in videos_ids:
            useful_info = get_video_info.get_useful_info(video_id, api)
            publishedAt = useful_info['publishedAt']
            statistics = useful_info['statistics']
            #if search_video.check_update_by_time(publishedAt):
            if True:
                shorts_collection.append((video_id, statistics, channel_name))


def download_shorts(shorts_collection, channel_type, api, type, scene_cut):
    with open(f'{channel_type}.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        path = '/Users/Tiger/Desktop/videos_storage/'

        for i in range(len(shorts_collection)):
            shorts_id, channel_name = shorts_collection[i][0], shorts_collection[i][2]
            useful_info = get_video_info.get_useful_info(shorts_id, api)
            
            folder_name = f'{channel_type}/{str(i)}/'
            if type == 'shorts':
                link = 'https://www.youtube.com/shorts/' + shorts_id
            else:
                link = 'https://www.youtube.com/watch?v=' + shorts_id
            print(link)

            if scene_cut:
                download_video.download_yt_vid(path+folder_name, link, str(i))
                print('downloaded!')
                print(path+folder_name+title+'.mp4')
                
                print('dividing vids...')
                divide_video.simple_divide(path+folder_name+str(i), 0, 25)
            else:    
                title = useful_info['title']
                thumbnail_url = useful_info['thumbnail_max']
                tags = useful_info['tags']
                download_video.download_yt_vid(path+folder_name, link, title)
                
                writer.writerow([channel_name, title, thumbnail_url, tags, ' ', ''])

                try:
                    download_video.download_image(thumbnail_url, path + folder_name, 'thumbnail.png')
                    
                except: pass
    f.close()

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

main('basketball_youtuber_channels', 2, 'videos', True)



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







