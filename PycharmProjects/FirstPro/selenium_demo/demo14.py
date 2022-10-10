# selenium 定位frame
# switch_to.frame(reference) 切换frame，reference是传入参数，用来定位frame，可以是ID，name,index,webelement对象
# switch_to.default_content()返回主文档
# switch_to.parent_frame()返回父文档

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://sahitest.com/demo/frameTest.htm')
        # self.driver.maximize_window()
    def test1(self):
        self.driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td[1]/a[1]').click()
        top = self.driver.find_element(By.NAME, 'top')
        self.driver.switch_to.frame(top)
        sleep(5)
        self.driver.quit()

if __name__ == '__main__':
    case = TestCase()
    case.test1()
