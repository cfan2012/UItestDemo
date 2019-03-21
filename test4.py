from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import getCode

#使用Selenium在ThoughtApi实现publish一个api的jounery
chrome_driver = os.getcwd() + '/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver)

#登录oktapreview
driver.get("https://platform-qa.thoughtworks.net/")

#跳转到publish页面

#填写api信息并发布


