import re

def convert(txt, list):
    with open(txt, 'r') as fin:
        line = ' '
        nums = ['0','1','2','3','4','5','6','7','8','9']
        while len(line) != 0:
            if line[0] in nums:
                start = (re.search(r'\d*\W\d{2}\W.{6}', line).group()) 
                end = (re.search(r' \d*\W\d{2}\W.{6}', line).group())
                # need a function to see if it matches the timestamps given
                subtitle, new = '', ''
                while True:
                    new = fin.readline()[:-1]
                    
                    if len(new) == 0:
                        break
                    else:
                        subtitle += ' ' + new

                list.append([start, end, subtitle])
                
            line = fin.readline()
        return list
print(convert('testfile02.txt', []))


