def get_video_length(duration):
    
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    time, index, count, num = 0, 0, 0, ''
    while index < len(duration):
        if duration[index] == ':':
            if count == 0:
                time += int(num) * 3600
                num = ''
                count += 1
            else:
                time += int(num) * 60
                num = ''
        elif duration[index] in numbers:
            num += duration[index]  
        
        if index == len(duration)-1:
            time += int(num) 
        index += 1
    
    return time

print(get_video_length('00:03:48.370'))