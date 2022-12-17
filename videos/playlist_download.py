import os
import subprocess
from pytube import YouTube
import random
import requests
import re
import string


def foldertitle(url):
    try:
        res = requests.get(url)
    except:
        print('no internet')
        return False
    plain_text = res.text

    if 'list=' in url:
        eq = url.rfind('=') + 1
        cPL = url[eq:]
    else:
        print('Incorrect attempt.')
        return False
    return cPL

def link_snatcher(url):
    our_links = []
    try:
        res = requests.get(url)
    except:
        print('no internet')
        return False

    plain_text = res.text

    if 'list=' in url:
        eq = url.rfind('=') + 1
        cPL = url[eq:]
    else:
        print('Incorrect Playlist.')
        return False

    tmp_mat = re.compile(r'watch\?v=\S+?list=' + cPL)
    mat = re.findall(tmp_mat, plain_text)

    for m in mat:
        new_m = m.replace('&amp;', '&')
        work_m = 'https://youtube.com/' + new_m
        # print(work_m)
        if work_m not in our_links:
            our_links.append(work_m)
    return our_links

def main(url):
    BASE_DIR = os.getcwd()
    our_links = link_snatcher(url)
    os.chdir('/Users/Tiger/Desktop/videos_storage/')

    new_folder_name = foldertitle(url)
    print(new_folder_name[:7])

    try:
        os.mkdir(new_folder_name[:7])
    except:
        print('folder already exists')

    os.chdir(new_folder_name[:7])
    SAVEPATH = os.getcwd()
    print(f'\n files will be saved to {SAVEPATH}')

    x=[]
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            pathh = os.path.join(root, name)

            if os.path.getsize(pathh) < 1:
                os.remove(pathh)
            else:
                x.append(str(name))

    print('\nconnecting . . .\n')
    print()

    for link in our_links:
        try:
            yt = YouTube(link)
           
            main_title = yt.title
            main_title = main_title + '.mp4'
            main_title = main_title.replace('|', '')
            
        except:
            print('connection problem..unable to fetch video info')
            break
       
        if main_title not in x:
            if True:
                
                    vid = yt.streams.filter(progressive=True, file_extension='mp4', custom_filter_functions=[lambda s: (s.resolution == '1080p') or (s.resolution == '720p')]).first()
                        
                    print('Downloading. . . ' + vid.default_filename + ' and its file size -> ' + str(round(vid.filesize / (1024 * 1024), 2)) + ' MB.')
                
                    vid.download(SAVEPATH)
                    print('Video Downloaded')
                
            else:
                print('something is wrong.. please rerun the script')
        else:
            print(f'\n skipping "{main_title}" video \n')

    print(' downloading finished')
    print(f'\n all your videos are saved at --> {SAVEPATH}')
    return new_folder_name[:7]

print(main('https://www.youtube.com/watch?v=kcll-H4vCss&list=PL-8a09SW3wDTLiQDt2BPBP8EyN3Eug8bw'))