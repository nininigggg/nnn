import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from web_test.base import Base


class TestScroll(Base):
    def test_scroll_to_element(self):
        self.driver.get('https://ceshiren.com')
        el = self.driver.find_element(By.XPATH, '//*[contains(text(), "解码方法")]')
        ActionChains(self.driver).scroll_to_element(el).perform()
        time.sleep(3)

    def test_scroll_to_xy(self):
        self.driver.get('https://ceshiren.com')
        ActionChains(self.driver).scroll_by_amount(0, 3000).perform()
        time.sleep(10)
        