# select类
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from time import sleep
from selenium.webdriver.support.select import Select

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///' + path + '/form3.html'
        self.driver.get(file_path)
        sleep(2)
    def test_select(self):
        se = self.driver.find_element(By.ID, 'provise')
        select = Select(se)
        select.select_by_index(1)
        sleep(2)
        select.select_by_value('bj')
        sleep(2)
        select.select_by_visible_text('Shanghai')
        sleep(2)

        for i in range(3):
            select.select_by_index(i)
            sleep(1)
        sleep(3)
        select.deselect_all()
        sleep(3)

        for option in select.options:
            print(option.text)

if __name__ == '__main__':
    case = TestCase()
    case.test_select()
    case.driver.quit()