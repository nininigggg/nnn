# 17种元素等待条件
from selenium import webdriver
from selenium.webdriver.common.by import By
class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
        # self.driver.maximize_window()
        sleep(1)