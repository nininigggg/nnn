from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_chrome_remote():
    # 定义配置的实例对象option
    option = Options()
    option.debugger_address = "localhost:9222"
    driver = webdriver.Chrome(options=option)
    driver.get("https://work.weixin.qq.com/wework_admin/frame")

    driver.find_element_by_css_selector(".ww_indexImg_AddMember").click()

