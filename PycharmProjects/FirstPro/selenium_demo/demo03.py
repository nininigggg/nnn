from selenium import webdriver
# webdriver属性和方法
from selenium.webdriver.common.by import By
from time import sleep

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
        self.driver.maximize_window()
    def test_prop(self):
        print(self.driver.name)#浏览器名称
        print(self.driver.current_url)#当前url
        print(self.driver.title)#当前页面标题
        print(self.driver.page_source)#当前页面源码
        print(self.driver.current_window_handle)#窗口句柄
        print(self.driver.window_handles)#当权窗口所有句柄
        self.driver.quit()

    def test_method(self):
        self.driver.find_element(By.ID, 'kw').send_keys('selenium')
        self.driver.find_element(By.ID, 'su').click()
        sleep(2)
        self.driver.back()
        sleep(2)
        self.driver.refresh()
        sleep(2)
        self.driver.forward()

        self.driver.close() #只关闭当前tab
        self.driver.quit() #关闭浏览器

    def test_windows(self):
        self.driver.find_element(By.LINK_TEXT, '新闻').click()
        windows = self.driver.window_handles

        while 1:
            for w in windows:
                self.driver.switch_to.window(w)
                sleep(2)

if __name__ == '__main__':
    case = TestCase()
    # case.test_prop()
    # case.test_method()
    case.test_windows()