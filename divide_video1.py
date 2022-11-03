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

def generate_final_clips(video_name, time_stamps, time_limit, path):
    sub_clip_count = 0
    dir_path, name = create_new_dir(video_name, path)
    random.shuffle(time_stamps)
    path = os.path.join(path, video_name)
    video = mpy.VideoFileClip(path)
    audio = mpy.AudioFileClip(path)
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
        destination = os.path.join(dir_path, f'{name}_{sub_clip_count}.mp4')
        final_video_clip.write_videofile(destination, fps=30, threads=4, codec="libx264")
        final_video_clip.close()







