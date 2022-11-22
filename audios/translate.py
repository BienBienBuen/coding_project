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
folder1 = '/Users/Tiger/Desktop/GitHub/coding_project/subtitles/'
# folder = ''
def get_subtitle(ytid, folder):
    ytdl_format_options = {
            'outtmpl': folder
    }
    with yt_dlp.YoutubeDL(ytdl_format_options) as ydl:

        url = 'https://www.youtube.com/watch?v=%s' % ytid
        info_dict = ydl.extract_info(url, download=False)
        subtitles = info_dict.get('subtitles')

        for sub_info in subtitles.items():
            sub_format = sub_info[0]
            dest = folder + 'sub' + str(sub_format)+'.csv'
            with open(dest, 'w', encoding='utf-8', newline='') as subfile:
                if sub_format == 'en-GB': #'zh-hans' or 'zh-CN' or 'zh_CN' or 
                    sub_url = sub_info[1][0]['url']
                    response = requests.get(sub_url)
                    parse = json.loads(response.content)
                    print(parse)
                    info = parse['events']
                    #write
                    
                    writer = csv.writer(subfile)
                    for i in range (len(info)):
                        for key, value in info[i].items():
                            writer.writerow([key, value])
                    
                else:
                    os.remove(dest)
                    
        # 这个东西本来可以call后直接下载subtitles， 但是他这个已经用不了了，github上好多index name都改了      
        # ydl._write_subtitles(info_dict, dest)


#get_subtitle('fXb02MQ78yQ', folder1)
# inputs some text/subtitle, and translate it into chinese
# returns chinese subtitle and their timestamp
from googletrans import Translator
SPECIAL_CASES = {
    'ee': 'et',
}
LANGUAGES = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'he': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'or': 'odia',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'ug': 'uyghur',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu',
}
def translate(original_text):
    translator = Translator()
    translation = translator.translate(original_text, src = 'en', dest= 'zh-cn')
    return translation.text
    
def audio_to_txt():
    pass

# inputs chinese subtitles, 
# #overlay them into videos
