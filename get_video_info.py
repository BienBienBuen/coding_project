def get_video_info(video_id, api):
    video_info = api.get_video_by_id(video_id=video_id).items[0].to_dict()
    return video_info

def get_useful_info(video_id, api):
    video_info = get_video_info(video_id, api)
    return {
        'title': video_info['snippet']['title'],
        'tags': video_info['snippet']['tags'],
        'categoryId': video_info['snippet']['categoryId'],
        'contentDetails': video_info['contentDetails'],
        'stattistics': video_info['statistics']
    }

def get_video_length(video_id, api):
    duration = get_video_info(video_id, api)['contentDetails']['duration']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    time, index, num = 0, 0, ''
    while index < len(duration):
        if duration[index] in numbers:
            num += duration[index]  
        elif duration[index] == 'H':
            time += int(num)*3600
            num = ''
        elif duration[index] == 'M':
            time += int(num)*60
            num = ''     
        elif duration[index] == 'S':
            time += int(num)
            num = ''  
        else:
            pass
        index += 1
    
    return time








