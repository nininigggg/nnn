from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


# def test2():
#     # 用selenium 打开浏览器
#     driver = webdriver.Chrome()
#     driver.get('https://www.baidu.com')
#     sleep(1)
#     driver.find_element(By.ID, "kw").send_keys('selenium')
#     # driver.find_element_by_id('kw').send_keys('selenium')
#     sleep(1)
#     driver.find_element(By.ID, "su").click()
#     # driver.find_element_by_id('su').click()
#     sleep(3)
#     driver.quit()

# 自己实现调用Chrome
# def test():
#     import subprocess
#     p = subprocess.Popen("chromedriver")
#     p.communicate()
# if __name__ == '__main__':
#     test()

# 使用面向对象方法封装程序
class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def sel1(self):
        self.driver.get('https://www.baidu.com')
        sleep(1)
        self.driver.find_element(By.ID, "kw").send_keys('selenium')
        # driver.find_element_by_id('kw').send_keys('selenium')
        sleep(1)
        self.driver.find_element(By.ID, "su").click()
        # driver.find_element_by_id('su').click()
        sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.sel1()
