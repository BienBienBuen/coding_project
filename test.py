import os
path = os.path.join('/Users/Tiger/Desktop/GitHub/videos/vid')
"""
os.mkdir(path)
print(path)
"""
import moviepy.editor as mpy

video = mpy.VideoFileClip(path)

subclip1 = video.subclip(0,1)
subclip2 = video.subclip(2, 3)
list = [subclip1, subclip2]
final = mpy.concatenate_videoclips(list)
final.write_videofile('/Users/Tiger/Desktop/GitHub/videos')