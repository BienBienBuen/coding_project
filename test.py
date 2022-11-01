import os
import cv2
os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/Cellar/ffmpeg@4/4.4.3/bin/ffmpeg"

path = os.path.join('/Users/bx/Documents/GitHub/coding_project/videos/Dad Slander.mp4')

"""
os.mkdir(path)
print(path)
path = os.path.join('/Users/Tiger/Desktop/GitHub/videos/vid')

video = mpy.VideoFileClip(path)
subclip1 = video.subclip(0,1)
subclip2 = video.subclip(2, 3)
list = [subclip1, subclip2]
final = mpy.concatenate_videoclips(list)


"""
import moviepy.editor as mpy


cap = cv2.VideoCapture(path)

video_fps = cap.get(cv2.CAP_PROP_FPS),
total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

print(total_frames)

video = mpy.VideoFileClip(path)
cap.write_videofile('/Users/bx/Documents/GitHub/coding_project/videos/', codec = 'libx264')