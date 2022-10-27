
from selenium.webdriver.common.by import By
from web_test.log_utils import logger
from web_test.base import Base


class TestRecord(Base):
    def test_record(self):
        search_content = "霍格沃茨"
        self.driver.get("https://www.sogou.com/")
        self.driver.find_element(By.ID, "query").send_keys(search_content)
        logger.debug(f"搜索的信息为{search_content}")
        self.driver.find_element(By.ID, "stb").click()
        search_res = self.driver.find_element(By.CSS_SELECTOR, "em")
        logger.info(f"实际结果为{search_res.text}，预期结果为{search_content}")
        assert search_res.text == search_content

    def test_screen_shout(self):
        search_content = "霍格沃茨"
        self.driver.get("https://www.sogou.com/")
        self.driver.find_element(By.ID, "query").send_keys(search_content)
        logger.debug(f"搜索的信息为{search_content}")
        self.driver.find_element(By.ID, "stb").click()
        search_res = self.driver.find_element(By.CSS_SELECTOR, "em")
        logger.info(f"实际结果为{search_res.text}，预期结果为{search_content}")
        self.driver.save_screenshot("./image/search.png")
        assert search_res.text == search_content

    def test_page_source(self):
        search_content = "霍格沃茨"
        self.driver.get("https://www.sogou.com/")
        with open("record/record.html", "w", encoding="utf-8") as f:
            f.write(self.driver.page_source)
        self.driver.find_element(By.ID, "query").send_keys(search_content)
        logger.debug(self.driver.page_source)


