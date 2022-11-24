from moviepy.editor import *
import re
time_stamps = [(0.4978125, 7.365937499999999), 
(8.395312500000003, 23.8359375), 
(24.9328125, 63.27281250000001)]
import yt_dlp 
import requests
import re
import json
import translate
# link: https://stackoverflow.com/questions/53659427/python-retrieve-automatic-captions-with-youtube-dl-and-transform-to-transcript
#numerical to standard (hh/mm/ss)
def convert_time1(num, string):

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
        return convert_time1(num%60, string)
    else:
        string += str(helper(str(int(num//3600))))
        num = num%3600
        return convert_time1(num, string)
    
def helper(num):
    if len(num) == 1:
        return '0'+num
    else:
        return num

#standard (hh/mm/ss) to numerical
def convert_time2(duration):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    time, index, count, num = 0, 0, 0, ''
    while index < len(duration):
        if duration[index] == ':':
            if count == 0:
                time += int(num) * 3600
                num = ''
                count += 1
            else:
                time += int(num) * 60
                num = ''
        elif duration[index] in numbers:
            num += duration[index]  
        
        if duration[index] == '.':
            time += int(num) 
        index += 1
    
    return time

def get_captions(video_id, video_name):
    url = 'youtube.com/watch?v=' + video_id
    ydl = yt_dlp.YoutubeDL({'writesubtitles': True, 'allsubtitles': True, 'writeautomaticsub': True})
    res = ydl.extract_info(url, download=False)
    #name = res.get('title', None)
    
    if res['requested_subtitles'] and res['requested_subtitles']['en']:
        print('Grabbing vtt file from ' + res['requested_subtitles']['en']['url'])
        response = requests.get(res['requested_subtitles']['en']['url'], stream=True)
        f1 = open(f"{video_name}.txt", "w")
        """
        new = re.sub(r'\d{2}\W\d{2}\W\d{2}\W\d{3}\s\W{3}\s\d{2}\W\d{2}\W\d{2}\W\d{3}\ align:start position:0%',repl = '',string = response.text)
        new = re.sub(r'.*</c>',repl = '',string = new)
        """
        f1.write(response.text)
        f1.close()
        if len(res['subtitles']) > 0:
            print('manual captions')
        else:
            print('automatic_captions')
    else:
        print('Youtube Video does not have any english captions')
   
from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.config import change_settings
# change_settings({"IMAGEMAGICK_BINARY": "/usr/local/Cellar/imagemagick/6.9.6-2/bin/convert"})
def read_sub(sub_path):
    with open(sub_path) as f:
        lines = []
        temp_list = []
        for line in f:
            temp_list.append(line.rstrip("\n"))
            if line == "\n":
                lines.append(temp_list)
                temp_list = []
        subs = []
        for i in range(len(lines)):
            time = lines[i][0].split("--> ")
            time_tuple = tuple([convert_time2(t) for t in time])

            subtitle_list = [lines[i][j] for j in range(len(lines[i])-1) if j > 0]
            subtitle = "".join(subtitle_list)
            final_tuple = (time_tuple, subtitle) 
            subs.append(final_tuple)

        #merge subs
        subs.pop(0)
        sub_f = []
        sub_t = ""
        counter = 0
        for i in range (len(subs)):
            if subs[i][1][-1] != ".":
                sub_t = sub_t + " " + subs[i][1]
                counter += 1
            else:
                time = (subs[i-counter][0][0], subs[i][0][1])
                sub_t = sub_t + " " + subs[i][1]
                #change translate.translate(subtitle) to subtitle for original sub
                #sub_f.append(tuple([time, sub_t]))
                sub_f.append(tuple([time, translate.translate(sub_t)]))
                sub_t = ""
                counter = 0
        """
        test
        for i in range(len(sub_f)):
            print(sub_f[i])
        """
    return sub_f

read_sub("/Users/bx/Documents/GitHub/coding_project/vid1.txt")
    
def generate_subtitles(video_path, dest, sub_path):

    generator = lambda txt: TextClip(txt, font="Songti-SC-Black", fontsize=40, color='white')
    """
    subs = [((0, 4), 'subs1'),
            ((4, 9), 'subs2'),
            ((9, 12), 'subs3'),
            ((12, 16), 'subs4')]
    """
    #sub 的 format 可以是直接一个list，timestamp和subtitle都在list里
    subs = read_sub(sub_path)
    subtitles = SubtitlesClip(subs, generator)
    video = VideoFileClip(video_path)
    result = CompositeVideoClip([video, subtitles.set_pos(('center','bottom'))])
    result.write_videofile(dest + "output.mp4", fps=video.fps, temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")

path = "/Users/bx/Documents/GitHub/coding_project/videos/vid1.mp4"
dest = "/Users/bx/Documents/GitHub/coding_project/videos/"
sub_path = "/Users/bx/Documents/GitHub/coding_project/vid1.txt"
#generate_subtitles(path, dest, sub_path)



"""
def add_subtitle(video_path, subtitle, start_time, end_time):
    video = VideoFileClip(video_path) 
    video = video.volumex(0.8) 
    video = video.subclip(0,10)
    subtitle = TextClip(subtitle, fontsize = 75, color = 'yellow') 
    subtitle = subtitle.set_start(start_time).set_end(end_time).set_pos('center').set_duration(10) 
    video = CompositeVideoClip([video, subtitle]) 
                
    video.ipython_display(width = 280) 

    destination = os.path.join(dir_path, f'{name}_{sub_clip_count}.mp4')
    final_video_clip.write_videofile(destination, fps=30, threads=4, codec="libx264")
    final_video_clip.close()
    """
# add_subtitle('/Users/Tiger/Desktop/GitHub/coding_project/videos_storage/1.mp4', 'i love u', 0, 5)



time_stamp = ()
test = [['00:00:01.780', ' 00:00:04.630', ' How much time do you really waste?'], 
['00:00:04.630', ' 00:00:06.410', ' For real?'], 
['00:00:06.410', ' 00:00:08.910', ' How much time do you have left?']]
def match_sub(time_stamp, list, diff_allowed):
    start, end = time_stamp[0], time_stamp[1]
    start_min, start_max = convert_time1(start - diff_allowed, ''), convert_time1(start + diff_allowed, '')
    end_min, end_max = convert_time1(end - diff_allowed, ''), convert_time1(end + diff_allowed, '')

    for start_index in range(len(list)):
        if start_min <= list[start_index][0] <= start_max:
            end_index = start_index
            while end_index < len(list):
                if end_min <= list[end_index][1] <= end_max: break
                end_index += 1
    return (start_index, end_index)


#test
#print(get_video_length('00:03:48.370'))

