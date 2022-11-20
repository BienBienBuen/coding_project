from selenium import webdriver
from csv import DictReader

driver = webdriver.Chrome()
driver.get('https://creator.douyin.com/creator-micro/content/upload')

def get_cookies_values(file, endcoding = 'utf-8'):
    with open(file) as fin:
        dict_reader = DictReader(fin)
        print(dict_reader)
        list_of_dicts = list(dict_reader)
    return list_of_dicts


import os
cookies_path = os.path.abspath('/Users/Tiger/Desktop/GitHub/coding_project/upload/cookies.csv')
cookies = get_cookies_values(cookies_path)
print(cookies)
for i in cookies:

    driver.add_cookie(i)

driver.refresh()