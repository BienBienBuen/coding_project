import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def login_google(driver, video_path, cover_path, description):
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






