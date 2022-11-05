import requests
import json


import requests

API_URL = "https://api-inference.huggingface.co/models/pyannote/speaker-segmentation"
headers = {"Authorization": "Bearer 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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.request("POST", API_URL, headers=headers, data=data)
    print(response.text)
    # return json.loads(response.content.decode("utf-8"))

#output = query("/Users/Tiger/Desktop/GitHub/coding_project/1.wav")
#print(output)


import requests

API_URL = "https://api-inference.huggingface.co/models/pyannote/speaker-diarization"
headers = {"Authorization": "Bearer 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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))

output = query("/Users/Tiger/Desktop/GitHub/coding_project/1.wav")
print(output)