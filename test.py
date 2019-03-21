from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

chrome_driver = os.getcwd() + '/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get("http://www.baidu.com")
assert "百度一下" in driver.title
elem = driver.find_element_by_name("wd")
elem.clear()
elem.send_keys("Kong")
elem.send_keys(Keys.RETURN)
assert "Documentation for Kong - v1.0.x | Kong - Open-Source API" not in driver.page_source
driver.close()