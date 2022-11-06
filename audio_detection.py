import requests
import json
token = "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"


API_URL = "https://api-inference.huggingface.co/models/pyannote/speaker-diarization"
headers = {"Authorization": f"Bearer {token}"}
path_1 = '/Users/bx/Documents/GitHub/coding_project/audio.wav'
path_2 = '/Users/Tiger/Desktop/GitHub/coding_project/audios/audio.wav'

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))

from pyannote.audio import Pipeline
pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization@2.1",
                                    use_auth_token=token)
# apply the pipeline to an audio file
diarization = pipeline("audio.wav")

# dump the diarization output to disk using RTTM format
with open("audio.rttm", "w") as rttm:
    print(1)
    diarization.write_rttm(rttm)