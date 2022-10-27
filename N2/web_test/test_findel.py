import time

from selenium.webdriver.common.by import By

from web_test.base import Base


class TestWindows(Base):
    def test_findById(self):
        self.driver.get('http://www.ceshiren.com')
        self.driver.find_element(By.ID, 'ember37').click()
        time.sleep(1)

    def test_findByName(self):
        self.driver.get('http://www.ceshiren.com')
        self.driver.find_element(By.NAME, '筛选条件：所有标签').click()
        time.sleep(1)

    def test_findByLink(self):
        self.driver.get('http://www.ceshiren.com')
        self.driver.find_element(By.LINK_TEXT, '学习笔记').click()
        time.sleep(1)

    def test_Id_text(self):
        self.driver.get('https://vip.ceshiren.com/#/ui_study')
        el = self.driver.find_element(By.ID, 'openWindows').text
        print(el)

    def test_Id_html(self):
        self.driver.get('https://vip.ceshiren.com/#/ui_study')
        el = self.driver.find_element(By.ID, 'locate_id').get_attribute('name')
        print(el)
