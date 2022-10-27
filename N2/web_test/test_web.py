import time

from selenium.webdriver.common.by import By

from web_test.base import Base


class TestWindows(Base):
    def test_window_start(self):
        self.driver.get('http://www.ceshiren.com')
        time.sleep(1)

    def test_window_refresh(self):
        self.driver.get('http://www.ceshiren.com')
        time.sleep(1)
        self.driver.refresh()
        time.sleep(1)

    def test_window_back(self):
        self.driver.get('http://www.ceshiren.com')
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id='ember35']").click()
        time.sleep(1)
        self.driver.back()
        time.sleep(1)

    def test_window_size(self):
        self.driver.get('http://www.ceshiren.com')
        time.sleep(1)
        self.driver.maximize_window()
        time.sleep(1)
        self.driver.minimize_window()
        time.sleep(1)