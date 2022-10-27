import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from web_test.base import Base


class TestMouse(Base):
    def test_double_click(self):
        self.driver.get("https://vip.ceshiren.com/#/ui_study/frame")
        el = self.driver.find_element(By.ID, 'primary_btn')
        ActionChains(self.driver).double_click(el).perform()
        time.sleep(3)

    def test_drag_and_drop(self):
        self.driver.get("https://vip.ceshiren.com/#/ui_study/action_chains")
        start_el = self.driver.find_element(By.ID, 'item1')
        target_el = self.driver.find_element(By.ID, 'item3')
        ActionChains(self.driver).drag_and_drop(start_el, target_el).perform()
        time.sleep(3)

    def test_drag_and_drop(self):
        self.driver.get("https://vip.ceshiren.com/#/ui_study/action_chains2")
        el = self.driver.find_element(By.CSS_SELECTOR, '.menu')
        ActionChains(self.driver).move_to_element(el).perform()
        self.driver.find_element(By.XPATH, '//*[contains(text(), "管理")]').click()
        time.sleep(3)
