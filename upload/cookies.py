import pathlib, pickle
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import undetected_chromedriver as chromedriver

def save_cookies_file(url):
    chrome_options = Options()
    driver = webdriver.Chrome()
    driver.get(url)
    pickle.dump(driver.get_cookies(), open('cookies.pk1', 'wb'))

save_cookies_file('https://creator.douyin.com/creator-micro/content/upload')


