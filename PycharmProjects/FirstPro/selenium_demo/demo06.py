from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from time import sleep
# 表单checkbox和radio
class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///' + path + '/form2.html'
        self.driver.get(file_path)
    def test_checkbox(self):
        # self.driver.find_element(By.NAME, 'swimming').click()
        # self.driver.find_element(By.NAME, 'reading').click()
        swimming = self.driver.find_element(By.NAME, 'swimming')
        if not swimming.is_selected():
            swimming.click()
        reading = self.driver.find_element(By.NAME, 'reading')
        if not reading.is_selected():
            reading.click()
        sleep(3)
        self.driver.quit()

    def test_radio(self):
        lst = self.driver.find_element(By.NAME, 'gender')
        # print(lst)
        lst.click()
        sleep(3)
        self.driver.quit()
if __name__ == '__main__':
    case = TestCase()
    # case.test_checkbox()
    case.test_radio()