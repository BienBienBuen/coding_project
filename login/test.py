import time
from selenium import webdriver
from csv import DictReader
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

options = uc.ChromeOptions()
driver = uc.Chrome(use_subprocess=True)
driver.get('https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=ni&fenlei=256&rsv_pq=0x89b9bd0300091688&rsv_t=ebbckVl4KgIlA7fBq8VBOAoTK2C06hNiMAoLMFnlCn1kAnzDsZj5l4m1g3Pm&rqlang=en&rsv_enter=0&rsv_dl=tb&rsv_sug3=3&rsv_sug1=1&rsv_sug7=100&rsv_btype=i&prefixsug=ni&rsp=3&inputT=21523&rsv_sug4=21522')
action = ActionChains(driver)

action.key_down(Keys.COMMAND).perform()
action.key_down("\u2325").perform()
action.send_keys('i').perform()
#action.key_up("\u2325").perform()
#action.key_up(Keys.COMMAND).perform()
time.sleep(100)