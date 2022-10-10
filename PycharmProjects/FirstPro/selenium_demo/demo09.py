# selenium 三种等待方式
# time.sleep()固定等待 脚本调试可用 代码中不用，会延长自动化时间
# implicitly_wait 隐式等待 是设置一个最长等待时间，在规定时间内玩也完成加载则执行下一步，否则等到时间结束，再执行下一步 整个周期起作用，设置一次就可
# WebDriverWait 显式等待
# from selenium.webdriver.support.wait import WebDriverWait
# 参数：driver:传入webdriver实例、timeout：超时时间，等待的最长时间、poll_frequency:调用until或until_not中的方法的间隔时间，默认0.5、ignored_exceptions：忽略的异常
# 方法：until和until_not 参数：method：等待期间，每隔一段时间传入的方法，直到返回值不是false、message：如果超时，抛出timeoutexception，将message传入异常
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
        # self.driver.maximize_window()
        sleep(1)
    def test_sleep(self):
        self.driver.find_element(By.ID, 'kw').send_keys('selenium')
        sleep(2) # 线程阻塞 blocking wait
        self.driver.find_element(By.ID, 'su').click()
        sleep(2)
    def test_implicitly(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID, 'kw').send_keys('selenium')
        self.driver.find_element(By.ID, 'su').click()
    def test_wait(self):
        wait = WebDriverWait(self.driver, 2)
        wait.until(EC.title_is('百度一下，你就直到'))
        self.driver.find_element(By.ID, 'kw').send_keys('selenium')
        self.driver.find_element(By.ID, 'su').click()


if __name__ == '__main__':
    case = TestCase()
    # case.test_sleep()
    # case.test_implicitly()
    case.test_wait()
    case.driver.quit()
