import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import os

chrome_driver = os.getcwd() + '/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get("http://www.python.org")

#模拟键盘输入

#填写表格
from selenium.webdriver.support.ui import Select
driver.get("http://sahitest.com/demo/selectTest.htm")
s1 = Select(driver.find_element_by_id('s1Id'))  # 实例化Select

s1.select_by_index()  # 选择第二项选项：
s1.select_by_value()  # 选择value="o2"的项
s1.select_by_visible_text()  # 选择text="o3"的值，即在下拉时我们可以看到的文本

#不同窗口和框架之间移动
driver.switch_to_window("windowName")

#弹出对话框
alert = driver.switch_to_alert()

#访问浏览器历史记录
driver.forward()
driver.back()

#断言

#显式等待，隐式等待