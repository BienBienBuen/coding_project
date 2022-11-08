from moviepy.editor import *
import extract_subtitles
import re
time_stamps = [(0.4978125, 7.365937499999999), 
(8.395312500000003, 23.8359375), 
(24.9328125, 63.27281250000001)]
    
def add_subtitle(video_path, audio_id, audio_name):
    video = VideoFileClip(video_path) 
    video = video.volumex(0.8) 

    #调用 extract subtitle 放进txt，然后读每一行
    extract_subtitles(audio_id, audio_name)
    nums = ['0','1','2','3','4','5','6','7','8','9']
    with open('testfile02.txt', 'r') as fin:
        line = ' '
        nums = ['0','1','2','3','4','5','6','7','8','9']
        while len(line) != 0:
            if line[0] in nums:
                start = (re.search(r'\d*\W\d{2}\W.{6}', line).group()) 
                end = (re.search(r' \d*\W\d{2}\W.{6}', line).group())
                subtitle = fin.readline()[:-1]
                subtitle = TextClip(subtitle, fontsize = 75, color = 'white') 
                subtitle = subtitle.set_start(start).set_end(end).set_pos('center').set_duration(10) 
                video = CompositeVideoClip([video, subtitle]) 
                
            line = fin.readline()
    video.ipython_display(width = 280) 
    """
    destination = os.path.join(dir_path, f'{name}_{sub_clip_count}.mp4')
    final_video_clip.write_videofile(destination, fps=30, threads=4, codec="libx264")
    final_video_clip.close()
    """
add_subtitle()

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
#test
#print(get_video_length('00:03:48.370'))