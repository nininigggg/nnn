#encoding:UTF-8
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

#封装
class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
        self.driver.maximize_window()
        sleep(1)

    def test_id(self):
        #self.driver.find_element(By.ID, "kw").send_keys('selenium')
        element = self.driver.find_element(By.ID, 'kw')
        element.send_keys('selenium')
        print(type(element))
        #<class 'selenium.webdriver.remote.webelement.WebElement'>
        self.driver.find_element(By.ID, 'su').click()
        sleep(3)

    def test_name(self):
        #driver.find_element_by_name(),可查找到多个元素，返回第一个
        #driver.find_elements_by_name()，返回一个集合
        self.driver.find_element_by_name('wd').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        sleep(3)

    def test_linktext(self):
        self.test_id()
        self.driver.find_element_by_link_text('百度首页').click()
        sleep(3)

    def test_partial_link_text(self):
        self.test_id()
        self.driver.find_element_by_partial_link_text('首页').click()
        sleep(3)

    def test_xpath(self):
        self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys('极客时间')
        self.driver.find_element_by_id('su').click()
        sleep(3)

        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.test_id()
    # case.test_name()
    # case.test_linktext()
    # case.test_partial_link_text()
    # case.test_xpath()
'''
find_element()
ID = "id"
XPATH = "xpath" 
LINK_TEXT = "link text" 
PARTIAL_LINK_TEXT = "partial link text"
NAME = "name"
CLASS_NAME = "class name"
TAG_NAME = "tag name"
CSS_SELECTOR = "css selector"
'''