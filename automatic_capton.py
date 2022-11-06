import yt_dlp 
import requests
import re
import json

# link: https://stackoverflow.com/questions/53659427/python-retrieve-automatic-captions-with-youtube-dl-and-transform-to-transcript

def captions_test02(url):
    ydl = yt_dlp.YoutubeDL({'writesubtitles': True, 'allsubtitles': True, 'writeautomaticsub': True})
    res = ydl.extract_info(url, download=False)
    
    
    if res['requested_subtitles'] and res['requested_subtitles']['en']:
        print('Grabbing vtt file from ' + res['requested_subtitles']['en']['url'])
        response = requests.get(res['requested_subtitles']['en']['url'], stream=True)
        f1 = open("testfile02.txt", "w")
        """
        new = re.sub(r'\d{2}\W\d{2}\W\d{2}\W\d{3}\s\W{3}\s\d{2}\W\d{2}\W\d{2}\W\d{3}\ align:start position:0%',repl = '',string = response.text)
        new = re.sub(r'.*</c>',repl = '',string = new)
        """
        f1.write(response.content)
        f1.close()
        if len(res['subtitles']) > 0:
            print('manual captions')
        else:
            print('automatic_captions')
    else:
        print('Youtube Video does not have any english captions')
   

if __name__ == '__main__':
    captions_test02("https://www.youtube.com/watch?v=K-kYglkAETg") 