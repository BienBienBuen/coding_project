import time
from selenium import webdriver
from csv import DictReader
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re
def get_cookies_values(file):
    with open(file, 'r') as fin:
        print(fin.readlines())
        for i in fin.readlines():
            i.replace('\ufeff', '')
            i.replace('\t', '')
            
        fin.seek(0)
        dict_reader = DictReader(fin)
        list_of_dicts = list(dict_reader)
        print(list_of_dicts)
    return list_of_dicts
get_cookies_values('/Users/Tiger/Desktop/GitHub/coding_project/cookies/百宝音.csv')

def upload_douyin(cookie_path, driver, url, video_path, cover_path, title, vid_type, tags):
    # 登录抖音
    cookies = get_cookies_values(cookie_path)
    driver.get(url)
    for i in cookies: driver.add_cookie(i)
    driver.refresh()
    time.sleep(7)
    try:
        driver.find_element(By.XPATH, '//*[@id="dialog-0"]/div/div/button/span').click()
        driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div/div/div/div/div/div/button/span').click()
        driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div/div/div/div/div/div/button/span').click()
    except:
        print('didnt work')
    
    driver.find_element(By.XPATH,'//*[text()="发布视频"]').click()
    time.sleep(5)
    
    try:
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="dialog-1"]/div/div/div/div[3]').click()
    except:
        print('didnt work')
    
    time.sleep(5)
    driver.find_element(By.XPATH,'//input[@type="file"]').send_keys(video_path)
    
    # 等待视频上传完成
    while True:
        time.sleep(3)
        try:
            driver.find_element(By.XPATH,'//*[text()="重新上传"]')
            break
        except Exception as e:
            print("视频还在上传中···")
    print("视频已上传完成！")

    try:
        driver.find_element(By.XPATH, '//*[@id="dialog-1"]/div/div/div/div[3]').click()
    except:
        print('didnt work')
    # 添加封面
    time.sleep(5)
    driver.find_element(By.XPATH,'//*[text()="编辑封面"]').click()
    time.sleep(5)
    driver.find_element(By.XPATH,'//div[text()="上传封面"]').click()
    time.sleep(5)
    driver.find_element(By.XPATH,'//input[@type="file"]').send_keys(cover_path)
    time.sleep(5)
    driver.find_element(By.XPATH,'//*[text()="裁剪封面"]/..//*[text()="确定"]').click()
    time.sleep(5)
    driver.find_element(By.XPATH,'//*[text()="设置封面"]/..//*[contains(@class,"upload")]//*[text()="确定"]').click()
    time.sleep(10)

    # 加标题
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div/div/div').send_keys(title)
    time.sleep(5)
    # 视频分类
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div[6]/div[2]/div[2]/svg').click()
    time.sleep(5)
    driver.find_element(By.XPATH,f'//*[text()="{vid_type[0]}"]').click()
    time.sleep(5)
    driver.find_element(By.XPATH,f'//*[text()="{vid_type[1]}"]').click()
    time.sleep(5)
    # 输入tags，tags 应该是一个list
    for tag in tags:
        #driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div[6]/div[4]/div[1]/div/input').click()
        driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[1]/div[6]/div[4]/div[1]/div/input').send_keys(tag)  
        driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[1]/div[6]/div[4]/div[1]/div/input').send_keys(Keys.ENTER)
    time.sleep(5)
    # 关联西瓜视频
    driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[1]/div[10]/div[1]/div/div[2]/div/input').click()
    time.sleep(5)
    # publish that bad boy
    driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[1]/div[14]/button[1]').click()

    time.sleep(999)

options = uc.ChromeOptions()
driver = uc.Chrome(use_subprocess=True)
video_path = '/Users/Tiger/Desktop/GitHub/coding_project/videos_storage/vid1.mp4'
cover_path = '/Users/Tiger/Desktop/GitHub/coding_project/videos_storage/pic1.jpg'
description = 'i love you babyyyy'
title = 'haha'
tags = 'wow'
vid_type = ('体育', '球类项目')
#upload_douyin('/Users/Tiger/Desktop/GitHub/coding_project/cookies/speech.csv', 
#driver, 'https://creator.douyin.com/creator-micro/content/upload', video_path, cover_path,  title, vid_type,tags)

def text_to_audio(cookie_path, driver, url, text):
    cookies = get_cookies_values(cookie_path)
    driver.get(url)
    for i in cookies: driver.add_cookie(i)
    driver.refresh()
    time.sleep(99)

text_to_audio('/Users/Tiger/Desktop/GitHub/coding_project/cookies/百宝音.csv', driver, 'https://peiyin.baibaoyin.com/', '你好吗')