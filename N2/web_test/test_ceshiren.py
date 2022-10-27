import time

from selenium.webdriver.common.by import By

from web_test.base import Base


class Test_CeShiRen(Base):
    def test_findById(self):
        """
        测试条件：打开论坛
        测试步骤：1.输入关键字
                2.点击搜索按钮

        :return:
        """
        self.driver.get('http://www.ceshiren.com')
        self.driver.find_element(By.ID, 'search-button').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="search-term"]').send_keys('selenium')
        time.sleep(1)
        # self.driver.find_element(By.XPATH,
        #                          '//*[@id="ember7"]/header/div/div/div[2]/div/div/div/div/div[2]/ul/li/a').click()
        self.driver.find_element(By.XPATH,
                                 "//*[@href='#']").click()
        time.sleep(1)
        # 添加断言
        # web_el = self.driver.find_element(By.XPATH,
        #                                   '//*[@id="ember7"]/header/div/div/div[2]/div/div/div/div/div[2]/div/ul/li[1]/a')
        web_el = self.driver.find_element(By.XPATH, "//*[@class='list']//li[1]")
        assert 'selenium' in web_el.text
