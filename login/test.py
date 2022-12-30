import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import requests

options = uc.ChromeOptions()
driver = uc.Chrome(use_subprocess=True)

def drop_down():
    for x in range(1, 30, 4):
        time.sleep(1)
        j = x/9
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' %j
        driver.execute_script(js)


def get_url_from_user(user_name):
    url = 'https://www.tiktok.com/@' + user_name
    driver.get(url)
    drop_down()
    lis = driver.find_elements(By.CSS_SELECTOR, '.tiktok-yz6ijl-DivWrapper.e1cg0wnj1')
    for li in lis:
        link = li.find_element(By.TAG_NAME, 'a').get_attribute('href')
        print(link)

headers = {
    'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

def download_tiktok(url):
    print(2)
    response = requests.get(url=url, headers=headers)
    print(1)
    response.encoding = 'utf-8'
    print(response.text)


download_tiktok('https://www.tiktok.com/@twice_tiktok_official')

