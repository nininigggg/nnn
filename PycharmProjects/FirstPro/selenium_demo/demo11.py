# selenium鼠标和键盘事件 被封装在ActionChains类中，ActionChains(driver).click(btn).perform()
from selenium import webdriver
from selenium.webdriver.common.by import By
class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://sahitest.com/demo/clocks.htm')
        sleep(1)
if __name__ == '__main__':
    case = TestCase()