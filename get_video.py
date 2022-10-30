

#All available info from channel
def get_channel_info(c_id):
    Channel_by_id = api.get_channel_info(channel_id= c_id)
    Channel_info = Channel_by_id.items[0].to_dict()
    return Channel_info

#从一个specific channel里return a list of video ID
def get_upload(c_id, number):
    info = get_channel_info(c_id)
    playlist_id = info["contentDetails"]["relatedPlaylists"]["uploads"]
    upload_list = api.get_playlist_items(playlist_id = playlist_id)
    videoID = []

    for i in range (number):
        videoID.append(upload_list.items[i].to_dict()["contentDetails"]["videoId"])
    return videoID

def get_newest_video(c_id):
    vid_id = get_upload(c_id, 1)
    return vid_id

