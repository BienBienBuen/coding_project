from pyannote.audio import Pipeline
from pyyoutube import Api
import os
import moviepy.editor as mpy

audio_path = '/Users/bx/Documents/GitHub/coding_project/audios/'

def get_audio(video_path, audio_path):
    audio = mpy.AudioFileClip(video_path)
    audio.write_audiofile(audio_path)

def divide_audio(audio_path):    
    pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization",
               use_auth_token="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")

    # 4. apply pretrained pipeline
    diarization = pipeline(audio_path)

    # 5. print the result
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        print(f"start={turn.start:.1f}s stop={turn.end:.1f}s speaker_{speaker}")
    
    dest = audio_path + 'audio.rttm'
    with open(dest, "w") as rttm:
        diarization.write_rttm(rttm)