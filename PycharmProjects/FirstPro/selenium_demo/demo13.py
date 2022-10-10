# selenium 屏幕截图
# save_screenshot(filename)获取当前屏幕截图并保存为指定文件，filename是指定保存的路径或图片文件名
# get_screenshot_as_base64()获取当前屏幕截图base64编码字符串
# get_screenshot_as_file(filename)获取当前屏幕截图,使用完整的路径
# get_screenshot_as_png()获取当前屏幕截图的二进制文件数据
import os.path

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep, strftime, localtime, time


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com')
        # self.driver.maximize_window()

    def test1(self):
        self.driver.find_element(By.ID, 'kw').send_keys('selenium')
        self.driver.find_element(By.ID, 'su').click()
        sleep(2)
        # self.driver.save_screenshot('baidu.png')
        # st = strftime("%Y-%m-%d-%H-%M-%S", localtime(time()))
        # file_name = st + '.png'
        # self.driver.save_screenshot(file_name)
        st = strftime("%Y-%m-%d-%H-%M-%S", localtime(time()))
        file_name = st + '.png'
        path = os.path.abspath('../screenshot')
        file_path = path + '/' + file_name
        self.driver.get_screenshot_as_file(file_path)

if __name__ == '__main__':
    case = TestCase()
    case.test1()
    case.driver.quit()