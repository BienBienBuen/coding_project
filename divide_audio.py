from pyannote.audio import Pipeline
from pyyoutube import Api
import os
import moviepy.editor as mpy
from itertools import islice
path_1 = '/Users/bx/Documents/GitHub/coding_project/audios/audio.wav'
path_2 = '/Users/Tiger/Desktop/GitHub/coding_project/audios/audio.wav'
dest = '/Users/bx/Documents/GitHub/coding_project/audios/'

def get_audio(video_path, dest):
    audio = mpy.AudioFileClip(video_path)
    audio.write_audiofile(dest)

def divide_audio(audio_path):    
    pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization",
               use_auth_token="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")

    # 4. apply pretrained pipeline
    diarization = pipeline(audio_path)

    timestamp = []
    timestamp_with_speaker = []
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        print(f"start={turn.start:.1f}s stop={turn.end:.1f}s speaker_{speaker}")
        timestamp.append(tuple([turn.start, turn.end]))
        timestamp_with_speaker.append([speaker[-1], turn.start, turn.end])
    
    timestamp_with_speaker.sort(key=lambda x: x[0]) #sort by which speaker it is
    sorted_stamp = [[]]
    for i in range(len(timestamp_with_speaker)-1):
        k = 0
        if timestamp_with_speaker[i][0] == timestamp_with_speaker[i+1][0]:
            sorted_stamp[k].append(tuple([timestamp_with_speaker[i][1], 
                                      timestamp_with_speaker[i][2]]))
        else:
            sublist = []
            sorted_stamp.append(sublist)
            k += 1
        if i+1 == len(timestamp_with_speaker):
            sorted_stamp[k].append(tuple([timestamp_with_speaker[i+1][1], 
                                          timestamp_with_speaker[i+1][2]]))
    print(sorted_stamp)
    #saving the result
    final = dest + 'audio.rttm'
    with open(final, "w") as rttm:
        print(2)
        diarization.write_rttm(rttm)

    return timestamp, sorted_stamp

divide_audio(path_1, dest)


def generate_final_audio(video_path, audio_path, dest):
    time_stamps, sorted_stamps = divide_audio(audio_path, dest)
    audio_clip = []
    audio = mpy.AudioFileClip(video_path)
    for i in range(len(time_stamps)):
        start, end = time_stamps[i][0], time_stamps[i][1]
        audio_subclip = audio.subclip(start, end)
        audio_clip.append(audio_subclip)
    final_audio_clip = mpy.concatenate_audioclips(audio_clip)
    
