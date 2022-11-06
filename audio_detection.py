import requests
import json
token = "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"

API_URL = "https://api-inference.huggingface.co/models/pyannote/speaker-diarization"
headers = {"Authorization": f"Bearer {token}"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))


path_2 = '/Users/Tiger/Desktop/GitHub/coding_project/audios/audio.wav'

from pyannote.audio import Pipeline
pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization@2.1",
                                    use_auth_token=token)
# apply the pipeline to an audio file
diarization = pipeline('/Users/Tiger/Desktop/GitHub/coding_project/audios/audio.wav')

# dump the diarization output to disk using RTTM format
with open("audio.rttm", "w") as rttm:
    print(1)
    diarization.write_rttm(rttm)