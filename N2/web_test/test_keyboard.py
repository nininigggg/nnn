import sys
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from web_test.base import Base


class TestKeyboard(Base):
    def test_shift(self):
        self.driver.get('https://ceshiren.com/')
        self.driver.find_element(By.ID, 'search-button').click()
        el = self.driver.find_element(By.ID, 'search-term')
        ActionChains(self.driver).key_down(Keys.SHIFT, el).send_keys("selenium").perform()
        time.sleep(3)

    def test_enter(self):
        self.driver.get('https://www.sogou.com/')
        self.driver.find_element(By.ID, 'query').send_keys("霍格沃滋")
        # 第一种回车
        # self.driver.find_element(By.ID, 'query').send_keys(Keys.ENTER)
        # 第二种回车
        ActionChains(self.driver).key_down(Keys.ENTER).perform()
        time.sleep(3)

    def test_copy(self):
        self.driver.get('https://ceshiren.com/')
        self.driver.find_element(By.ID, 'search-button').click()
        el = self.driver.find_element(By.ID, 'search-term')
        command_control = Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL
        ActionChains(self.driver)\
            .key_down(Keys.SHIFT, el)\
            .send_keys("selenium")\
            .key_down(Keys.ARROW_LEFT).key_down(command_control).send_keys("xvv").key_up(command_control).perform()
        time.sleep(3)
