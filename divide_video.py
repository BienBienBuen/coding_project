import moviepy.editor as mpy
import os
#test video and time_stamps

time_stamps = [(0, 20)] 

# time_stamps are found by algo which segments video 



def generate_final_clips(video_name, time_stamps):
    path = os.path.join('/Users/Tiger/Desktop/GitHub/videos/', video_name)
    video = mpy.VideoFileClip(path)
    audio = mpy.AudioFileClip(path)
    # divide into parts according to given time stamps
    video_clips, audio_clips = [], []
    for i in range(len(time_stamps)):
        start, end = time_stamps[i][0], time_stamps[i][1]
        video_subclip = video.subclip(start, end)
        audio_subclip = audio.subclip(start, end)
        video_clips.append(video_subclip)
        audio_clips.append(audio_subclip)
    
    # save file 
    final_video_clips = mpy.concatenate_videoclips(video_clips)
    final_audio_clips = mpy.concatenate_audioclips(audio_clips)
    final_video_clips.audio = final_audio_clips

    ### need to think of ways to organize downloaded and produced videos. 
    ### e.g. naming (keeping a global variable to keep count....vid1, vid2, vid3...? 
    ### adding orginal titles....crazy_dimes_vid1, crazy_dimes_vid2, crazy_dimes_vid3?)

    final_video_clips.write_videofile('/Users/Tiger/Desktop/GitHub/videos/vidx.mp4') 

generate_final_clips('12', time_stamps)

def put_new_dir(video_name, final_video_clips):
    
    path = os.path.join('/Users/Tiger/Desktop/GitHub/videos/', video_name, 'remake')
    os.mkdir(path)

    for clip in final_video_clips:
        clip.write_videofile(path)
    return


# need to do: randomly group subclips, each group under certain time limits, concatenate each group
# and put them in final clips list