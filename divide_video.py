import os
# os.environ["IMAGEIO_FFMPEG_EXE"] = "/usr/bin/ffmpeg"
os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/Cellar/ffmpeg@4/4.4.3/bin/ffmpeg"
import moviepy.editor as mpy
import random

#test video and time_stamps

time_stamps1 = [(0, 20)]
time_stamps = [(0, 20), (20, 30), (30, 45),(50, 59)] 
# time_stamps are found by algo which segments video 

time_limit = 60
def create_new_dir(video_name):
    new = ''
    for letter in video_name:
        if letter == '.': break
        else: new += letter
    new += '_remake_collection'
    #comment out the other path on your local repository
    # path = os.path.join('/Users/Tiger/Desktop/GitHub/videos/', new)
    path = os.path.join('/Users/bx/Documents/GitHub/coding_project/videos/', new) 
    os.mkdir(path)
    return path
"""
def put_new_dir(final_video_clips, path):
    
    for clip in final_video_clips:
        clip.write_videofile(path, fps=30, threads=1, codec="libx264")
        clip.close()
    return
"""
def generate_final_clips(video_name, time_stamps, time_limit):
    # dir_path = create_new_dir(video_name)
    random.shuffle(time_stamps)
    #comment out the other path on your local repository
    # path = os.path.join('/Users/Tiger/Desktop/GitHub/videos/', video_name)
    path = os.path.join('/Users/bx/Documents/GitHub/coding_project/videos/', video_name)
    video = mpy.VideoFileClip(path)
    audio = mpy.AudioFileClip(path)
    index = 0
    accumulated_time = 0
    video_clip, audio_clip = [], []
    #find groups of subclips that fit time limit
    print(11111)
    while index < len(time_stamps) and accumulated_time + (time_stamps[index][1] - time_stamps[index][0]) <= time_limit:
        if index < len(time_stamps) and accumulated_time + (time_stamps[index][1] - time_stamps[index][0]) <= time_limit:
            accumulated_time += (time_stamps[index][1] - time_stamps[index][0])
            print(index)
            # group subclips 
            start, end = time_stamps[index][0], time_stamps[index][1]
            video_subclip = video.subclip(start, end)
            audio_subclip = audio.subclip(start, end)
            video_clip.append(video_subclip)
            audio_clip.append(audio_subclip)
            index += 1

    final_video_clip = mpy.concatenate_videoclips(video_clip)
    final_audio_clip = mpy.concatenate_audioclips(audio_clip)
    final_video_clip.audio = final_audio_clip
    #这个是一个placeholder mp4 file, 用来承载final video
    destination = '/Users/bx/Documents/GitHub/coding_project/videos/vid1.mp4'
    final_video_clip.write_videofile(destination, fps=30, threads=1, codec="libx264")
    final_video_clip.close()
    #put_new_dir(final_video_clip, dir_path)
        
       

    ### need to think of ways to organize downloaded and produced videos. 
    ### e.g. naming (keeping a global variable to keep count....vid1, vid2, vid3...? 
    ### adding orginal titles....crazy_dimes_vid1, crazy_dimes_vid2, crazy_dimes_vid3?)



generate_final_clips('Dad Slander.mp4', time_stamps, 60)


