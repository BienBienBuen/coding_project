import yt_dlp 
import requests
import re
import json

# link: https://stackoverflow.com/questions/53659427/python-retrieve-automatic-captions-with-youtube-dl-and-transform-to-transcript
path_1 = '/Users/bx/Documents/GitHub/coding_project/audios_storage/'
path_2 = '/Users/Tiger/Desktop/GitHub/coding_project/audios_storage/'

def get_sub(video_id, video_name, path):
    url = 'youtube.com/watch?v=' + video_id
    ydl = yt_dlp.YoutubeDL({'writesubtitles': True, 'allsubtitles': True, 'writeautomaticsub': True})
    res = ydl.extract_info(url, download=False)
    #name = res.get('title', None)
    
    if res['requested_subtitles'] and res['requested_subtitles']['en']:
        print('Grabbing vtt file from ' + res['requested_subtitles']['en']['url'])
        response = requests.get(res['requested_subtitles']['en']['url'], stream=True)
        f1 = open(path + video_name+'.txt', "w")
        
        new = re.sub(r'\d{2}\W\d{2}\W\d{2}\W\d{3}\s\W{3}\s\d{2}\W\d{2}\W\d{2}\W\d{3}\ align:start position:0%',repl = '',string = response.text)
        new = re.sub(r'.*</c>',repl = '',string = new)
        
        f1.write(new)
        f1.close()
        if len(res['subtitles']) > 0:
            print('manual captions')
        else:
            print('automatic_captions')
    else:
        print('Youtube Video does not have any english captions')
   

if __name__ == '__main__':
    # get_sub("CDxHbfFDvxo", 'testfile2', path_2) 
    get_sub("qvX3DJj0rkA", 'vid7', path_1)