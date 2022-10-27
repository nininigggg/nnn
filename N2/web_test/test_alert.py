import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from web_test.base import Base


class TestFrame(Base):
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        drag = self.driver.find_element(By.ID, 'draggable')
        drop = self.driver.find_element(By.ID, 'droppable')
        ActionChains(self.driver).drag_and_drop(drag, drop).perform()
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()
        self.driver.find_element(By.ID, "submitBTN").click()
        time.sleep(3)