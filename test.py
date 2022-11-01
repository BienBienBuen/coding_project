import os
import cv2
#os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/Cellar/ffmpeg@4/4.4.3/bin/ffmpeg"



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

path = os.path.join('/Users/bx/Documents/GitHub/coding_project/videos/Dad Slander.mp4')
video = mpy.VideoFileClip(path)
subclip1 = video.subclip(0,5)
subclip2 = video.subclip(10, 15)
list = [subclip1, subclip2]
final = mpy.concatenate_videoclips(list)
final.write_videofile('/Users/bx/Documents/GitHub/coding_project/videos/vid1.mp4', codec = 'libx264')
final.close()