#https://github.com/TensorSpeech/TensorFlowTTS
import googletrans 
import yt_dlp
import os 
import webbrowser
import requests
import json
import csv

# if video has subtitles from yt-dlp, we import them directly
# returns subtitle and their timestamp
folder = '/Users/bx/Documents/GitHub/coding_project/subtitles/'
# folder = ''
def get_subtitle(ytid, folder):
    ytdl_format_options = {
            'outtmpl': folder
    }
    with yt_dlp.YoutubeDL(ytdl_format_options) as ydl:

        url = 'https://www.youtube.com/watch?v=%s' % ytid
        info_dict = ydl.extract_info(url, download=False)
        subtitles = info_dict.get('subtitles')
        dest = folder + 'sub.csv'

        with open(dest, 'w', encoding='utf-8', newline='') as subfile:

            for sub_info in subtitles.items():
                sub_format = sub_info[0]

                if sub_format == 'en-GB': #'zh-hans' or 'zh-CN' or 'zh_CN' or 
                    sub_url = sub_info[1][0]['url']
                    response = requests.get(sub_url)
                    parse = json.loads(response.content)
                    info = parse['events']
                    #write
                    writer = csv.writer(subfile)
                    for i in range (len(info)):
                        for key, value in info[i].items():
                            writer.writerow([key, value])

                else:
                    print("no subtitles")    
        # 这个东西本来可以call后直接下载subtitles， 但是他这个已经用不了了，github上好多index name都改了      
        # ydl._write_subtitles(info_dict, dest)

get_subtitle('fXb02MQ78yQ', folder)

# inputs some text/subtitle, and translate it into chinese
# returns chinese subtitle and their timestamp
def translate():
    pass

#if we want to generate audio from a piece of inspirational text, we call this
# inputs a txt file, length of target video, outputs mp3
def generate_audio():
    pass

# inputs chinese subtitles, 
# #overlay them into videos
def generate_subtitles():

    pass