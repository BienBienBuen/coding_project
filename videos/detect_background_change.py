import cv2
import time

vid = cv2.VideoCapture('1.mp4')
"""
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

def split_video_into_scenes(video_path, threshold=79):
    # Open our video, create a scene manager, and add a detector.
    video = open_video(video_path)
    scene_manager = SceneManager()
    scene_manager.add_detector(
        ContentDetector(threshold=threshold))
    scene_manager.detect_scenes(video, show_progress=True)
    scene_list = scene_manager.get_scene_list()
    print(scene_list)
    #split_video_ffmpeg(video_path, scene_list, show_progress=True)

split_video_into_scenes('/Users/Tiger/Desktop/GitHub/coding_project/videos/ha.mp4')