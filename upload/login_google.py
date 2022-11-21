import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def upload_video(driver, video_path, cover_path, description):
    """
    log into google account
    """
    driver.get("https://stackoverflow.com/")
    driver.maximize_window()
    driver.find_element(By.XPATH, '/html/body/header/div/nav/ol/li[3]/a').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="openid-buttons"]/button[1]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys('tigerzouxk@gmail.com')
    driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()
    
    time.sleep(2)
    password = input('google account password: ')
    driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()
    time.sleep(5)

    """
    upload to douyin
    """
    driver.get("https://creator.douyin.com/creator-micro/content/upload")
    time.sleep(2)
    driver.find_element_by_xpath('//*[text()="发布视频"]').click(video_path)
    time.sleep(2)
    driver.find_element_by_xpath('//input[@type="file"]').send_keys()

    # 等待视频上传完成
    while True:
        time.sleep(3)
        try:
            driver.find_element_by_xpath('//*[text()="重新上传"]')
            break
        except Exception as e:
            print("视频还在上传中···")
    
    print("视频已上传完成！")
    
    # 添加封面
    driver.find_element_by_xpath('//*[text()="编辑封面"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//div[text()="上传封面"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//input[@type="file"]').send_keys(cover_path)
    time.sleep(3)
    driver.find_element_by_xpath('//*[text()="裁剪封面"]/..//*[text()="确定"]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[text()="设置封面"]/..//*[contains(@class,"upload")]//*[text()="确定"]').click()
    
    time.sleep(5)
    # 输入视频描述, 可以定制tags
    driver.find_element_by_xpath('//div[@aria-autocomplete="list"]//br').send_keys(description + " #上热门 #dou上热门 #我要上热门")
    
    

def login1(driver):
    driver.get("https://medium.com/")
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/div/div/div/div[3]/span[4]/div/p/span/a').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div[2]/a/div').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys('tigerzouxk@gmail.com')
    driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()
    
    time.sleep(2)
    password = input('google account password: ')
    driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()
    time.sleep(9999)

import undetected_chromedriver as uc
options = uc.ChromeOptions()
#options.headless = True
#options.add_experimental_option("debuggerAddress", "127.0.0.1:5003")
#options.add_argument("user-data-dir=/Users/Tiger/Library/Application Support/Google/Chrome/Profile 8")
#options.add_argument = ("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36")
driver = uc.Chrome(use_subprocess=True)
video_path = '/Users/Tiger/Desktop/GitHub/coding_project/videos_storage/vid1.mp4'
cover_path = 'pic1.jpg'
description = 'i love you babyyyy'
upload_video(driver, video_path, cover_path, description)




