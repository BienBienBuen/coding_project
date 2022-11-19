from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:5003")
driver = webdriver.Chrome(options = options)
driver.get("https://creator.douyin.com/creator-micro/home")