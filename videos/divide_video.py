import os
# os.environ["IMAGEIO_FFMPEG_EXE"] = "/usr/bin/ffmpeg"
#os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/Cellar/ffmpeg@4/4.4.3/bin/ffmpeg"
import moviepy.editor as mpy
import random

# time_stamps are found by algo which segments video 
def create_new_dir(video_name, path):
    new = ''
    for letter in video_name:
        if letter == '.': break
        else: new += letter
    new_name = new + '_remake_collection'
    path = os.path.join(path, new_name) 
    os.mkdir(path)
    return path, new

def generate_final_clips(vid_name, time_stamps, time_limit, vid_path):
    sub_clip_count = 0
    
    try:
        vid_collection_path = os.path.join(f'./coding_project/videos_storage/'+ vid_name + '_collection')
        os.mkdir(vid_collection_path)
    except: pass
    random.shuffle(time_stamps)
    
    video = mpy.VideoFileClip(vid_path)
    audio = mpy.AudioFileClip(vid_path)
    index = 0
    #find groups of subclips that fit time limit
    while index < len(time_stamps):
        start_index = index
        accumulated_time = 0
        while index < len(time_stamps) and (accumulated_time + (time_stamps[index][1] - time_stamps[index][0]) <= time_limit):
            accumulated_time += time_stamps[index][1] - time_stamps[index][0]
            index += 1
            
        # group subclips 
        video_clip, audio_clip = [], []
        if start_index == index:
            for i in range(start_index, index+1):
                start, end = time_stamps[i][0], time_stamps[i][1]
                video_subclip = video.subclip(start, end)
                audio_subclip = audio.subclip(start, end)
                video_clip.append(video_subclip)
                audio_clip.append(audio_subclip)
        else:
            for i in range(start_index, index):
                start, end = time_stamps[i][0], time_stamps[i][1]
                video_subclip = video.subclip(start, end)
                audio_subclip = audio.subclip(start, end)
                video_clip.append(video_subclip)
                audio_clip.append(audio_subclip)
        sub_clip_count += 1
        final_video_clip = mpy.concatenate_videoclips(video_clip)
        final_audio_clip = mpy.concatenate_audioclips(audio_clip)
        final_video_clip.audio = final_audio_clip
        destination = os.path.join(vid_collection_path, f'{vid_name}_{sub_clip_count}.mp4')
        final_video_clip.write_videofile(destination, fps=30, threads=4, codec="mpeg4")
        final_video_clip.close()
#time_stamps = [(0.0, 0.6), (0.6, 1.97), (1.97, 4.67), (4.67, 19.55), (19.55, 34.63), (34.63, 49.72), (49.72, 64.8), (64.8, 79.88), (79.88, 94.99), (94.99, 110.08), (110.08, 125.16), (125.16, 139.77), (139.77, 154.85), (154.85, 169.94), (169.94, 185.02), (185.02, 200.1), (200.1, 215.18), (215.18, 230.26), (230.26, 245.38), (245.38, 260.46), (260.46, 275.54), (275.54, 283.65), (283.65, 298.73), (298.73, 313.81), (313.81, 316.05), (316.05, 328.93), (328.93, 344.01), (344.01, 359.09), (359.09, 374.17), (374.17, 389.26), (389.26, 407.24), (407.24, 410.48)]
#generate_final_clips('dance', time_stamps, 35, './coding_project/videos_storage/dance.mp4')

def simple_divide(dir_name, vid_name, start_time, time_per_clip, vid_path):
    video = mpy.VideoFileClip(vid_path)
    audio = mpy.AudioFileClip(vid_path)
    vid_collection_path = os.path.join(f'./coding_project/videos_storage/anime/{dir_name}/' + vid_name + '_collection')
    os.mkdir(vid_collection_path)
    print(video.duration)
    count = 0
    for time in range(start_time, int(video.duration)-time_per_clip, time_per_clip):
        
        
        start, end = time, time+time_per_clip
        if time+time_per_clip > video.duration:
            break
        
        video_subclip = video.subclip(start, end)
        audio_subclip = audio.subclip(start, end)
        video_subclip.set_audio(audio_subclip)
        destination = os.path.join(vid_collection_path, f'{vid_name}_{count}.mp4')
        try:
            video_subclip.write_videofile(destination, fps=30, threads=4, codec="mpeg4")
            video_subclip.close()
            count += 1
        except: pass
        

import os
path = './coding_project/videos_storage/anime/PLECYMF/'
dir_list = os.listdir(path)

count = 0
dir_name = 'PLECYMF'
for i in range(len(dir_list)):
    count+= 1
    simple_divide(dir_name, f'vid{count}', 10, 20, f'./coding_project/videos_storage/anime/{dir_name}/{dir_list[i]}')
