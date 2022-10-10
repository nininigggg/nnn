# selenium 执行 javascript 脚本
# webdriver 有两个方法执行 javascript：execute_script 同步执行；execute_async_script 异步执行
# 通过javascript 通常可以实现页面滚动
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com')
    def test1(self):
        self.driver.execute_script("alert('test')")
        sleep(2)
        self.driver.switch_to.alert.accept()
        sleep(2)

    def test2(self):
        js = 'return document.title'
        title = self.driver.execute_script(js)
        print(title)

    def test3(self):
        js = 'var q = document.getElementById("kw"); q.style.border="2px solid red"'
        self.driver.execute_script(js)
        sleep(2)

    def test4(self):
        self.driver.find_element(By.ID, 'kw').send_keys('selenium')
        self.driver.find_element(By.ID, 'su').click()
        js = 'window.scrollTo(0,document.body.scrollHeight)'
        self.driver.execute_script(js)
        sleep(2)


if __name__ == '__main__':
    case = TestCase()
    # case.test1()
    case.test4()
    # case.driver.quit()