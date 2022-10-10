# form表单的测试流程：
# 1.定位表单元素
# 2.输入测试值
# 3.判断表单元素属性
# 4.获取表单元素属性
# 5.提交表单进行验证
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from time import sleep


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        # 获取当前文件地址：path = os.path.abspath(__file__)
        # /Users/nnn/PycharmProjects/FirstPro/demo05.py
        path = os.path.dirname(os.path.abspath(__file__))
        # 获取当前文件文件夹：path = os.path.dirname(os.path.abspath(__file__))
        # / Users / nnn / PycharmProjects / FirstPro
        file_path = 'file:///' + path + '/forms.html'
        # 获取本地form表单：file:////Users/nnn/PycharmProjects/FirstPro/forms.html
        # print(file_path)
        self.driver.get(file_path)

    def test_login(self):
        # mac格式化操作：command+option+L
        username = self.driver.find_element(By.ID, 'username')
        username.send_keys('admin')
        pwd = self.driver.find_element(By.ID, 'pwd')
        pwd.send_keys('123')

        # print(username.get_attribute('value'))
        # print(pwd.get_attribute('value'))

        self.driver.find_element(By.ID, 'submit').click()
        self.driver.switch_to.alert.accept()
        sleep(2)
        username.clear()
        pwd.clear()
        sleep(5)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.test_login()
