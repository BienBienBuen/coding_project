from pyyoutube import Api
from main import get_playist_from_channel
import yt_dlp

get_playist_from_channel()

from yt_dlp import YoutubeDL

URLS = ['https://www.youtube.com/watch?v=BaW_jenozKc']
with YoutubeDL() as ydl:
    ydl.download(URLS)