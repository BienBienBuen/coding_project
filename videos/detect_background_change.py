import cv2
import time
import os
# import js2py
"""
path_1 = '/Users/bx/Documents/GitHub/coding_project/videos/Dad Slander.mp4'
path_2 = '/Users/Tiger/Desktop/GitHub/coding_project/videos/vid3.mp4'
"""

from scenedetect import open_video, SceneManager, split_video_ffmpeg
from scenedetect.detectors import ContentDetector
from scenedetect.video_splitter import split_video_ffmpeg

def split_video_into_scenes(path, threshold):
    # Open our video, create a scene manager, and add a detector.
    video = open_video(path)
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
"""
path_1 = '/Users/bx/Documents/GitHub/coding_project/videos/Dad Slander.mp4'
path_2 = '/Users/Tiger/Desktop/videos_storage/anime/PLECYMF/Anime Edits  TikTok Compilation  Part 1 🔥.mp4'
#test
x = split_video_into_scenes(path_2, 92)
print(standardize_scene_list(x))

# tiktok_dance: 12
"""