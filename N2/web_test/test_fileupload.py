import time

from selenium.webdriver.common.by import By

from web_test.base import Base


class TestFrame(Base):
    def test_file(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element(By.XPATH, '//*[@id="sttb"]/img[1]').click()
        self.driver.find_element(By.XPATH, '//*[@id="uploadImg"]').send_keys("/Users/N/Documents/N_file/python_test/web_test/image/111.jpg")
        time.sleep(3)
