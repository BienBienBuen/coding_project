import yt_dlp 
import requests
import re
import json
from get_video_info import get_video_length

time_stamps = [[(0.4978125, 7.365937499999999), 
(8.395312500000003, 23.8359375), 
(24.9328125, 63.27281250000001)]]


url = "https://www.youtube.com/watch?v=CDxHbfFDvxo"
ydl = yt_dlp.YoutubeDL({'writesubtitles': True, 'allsubtitles': True, 'writeautomaticsub': True})
res = ydl.extract_info(url, download=False)


if res['requested_subtitles'] and res['requested_subtitles']['en']:
    print('Grabbing vtt file from ' + res['requested_subtitles']['en']['url'])
    response = requests.get(res['requested_subtitles']['en']['url'], stream=True)
    print(response.content)
    new = re.sub(r'\d{2}\W\d{2}\W\d{2}\W\d{3}\s\W{3}\s\d{2}\W\d{2}\W\d{2}\W\d{3}\ align:start position:0%',repl = '',string = response.text)
    new = re.sub(r'.*</c>',repl = '',string = new)
    

def convert_time(num, string):

    if num < 60:
        if string == '':
            string += '00:00' 
        string += ':' 
        decimals = num - int(num)
        string += helper(str(int(num)))
        string += '.' + str(round(decimals, 3))[2:]
        return string
        
    elif num < 3600:
        if string == '':
            string += '00'
        string += ':'
        print(int(num//60))
        string += helper(str(int(num//60)))
        print(num%60, string)
        return convert_time(num%60, string)
    else:
        string += str(helper(str(int(num//3600))))
        num = num%3600
        return convert_time(num, string)
    
def helper(num):
    if len(num) == 1:
        return '0'+num
    else:
        return num
#test
#print(convert_time(9.949, ''))