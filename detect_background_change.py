import cv2
import time
import os
# import js2py

path_1 = '/Users/bx/Documents/GitHub/coding_project/videos/Dad Slander.mp4'
path_2 = '/Users/Tiger/Desktop/GitHub/coding_project/videos/vid3.mp4'
cap = cv2.VideoCapture(path_1)
video_fps = cap.get(cv2.CAP_PROP_FPS),
total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

js1 = """
function escramble_758(){
var a,b,c
a='+1 '
b='84-'
a+='425-'
b+='7450'
c='9'
document.write(a+c+b)
}
escramble_758()
""".replace("document.write", "return ")

js2 = """
var search = require('youtube-heatmap');
getHeatMap('https://www.youtube.com/watch?v=_lEzN8C5c7k')
    .then(heatMap => {
        console.log(heatMap)
    })
"""
# result = js2py.eval_js(js1)

"""
vid = cv2.VideoCapture('lebron.mp4')
pTime = 0
while True:
    success, img = vid.read()
    cv2.imshow("Image", img)
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    #在每一帧放字幕
    cv2.putText(img )
    cv2.waitKey(1)
"""

from scenedetect import open_video, SceneManager, split_video_ffmpeg
from scenedetect.detectors import ContentDetector
from scenedetect.video_splitter import split_video_ffmpeg

def split_video_into_scenes(video_path, threshold=75):
    # Open our video, create a scene manager, and add a detector.
    video = open_video(video_path)
    scene_manager = SceneManager()
    scene_manager.add_detector(
        ContentDetector(threshold=threshold))
    scene_manager.detect_scenes(video, show_progress=True)
    scene_list = scene_manager.get_scene_list()
    # split_video_ffmpeg(video_path, scene_list, show_progress=True)
    return scene_list

def standardize_scene_list(scene_list):
    timestamp = []
    for i in range(len(scene_list)):
        stamp = tuple((round(scene_list[i][0].get_seconds(), 2), 
                       round(scene_list[i][1].get_seconds(), 2)))
        timestamp.append(stamp)
    return timestamp

#test
# x = split_video_into_scenes(path_1)
# print(standardize_scene_list(x))