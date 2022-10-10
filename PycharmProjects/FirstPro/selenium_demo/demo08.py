# 弹窗处理
# alert:用来提示
# confirm：用来确认
# prompt：用来输入内容 accept():接受 dismiss():取消 text:显示文本 send_keys:输入内容
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from time import sleep
from selenium.webdriver.support.select import Select

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///' + path + '/form4.html'
        self.driver.get(file_path)
        sleep(2)

    def test_alert(self):
        self.driver.find_element(By.ID, 'alert').click()
        # 切换到alert
        alert = self.driver.switch_to.alert
        print(alert.text)
        sleep(3)
        alert.accept()
    def test_confirm(self):
        self.driver.find_element(By.ID, 'confirm').click()
        confirm = self.driver.switch_to.alert
        print(confirm.text)
        sleep(3)
        confirm.accept()
        sleep(3)
        confirm.dismiss()
    def test_prompt(self):
        self.driver.find_element(By.ID, 'prompt').click()
        prompt = self.driver.switch_to.alert
        print(prompt.text)
        sleep(2)
        prompt.accept()

if __name__ == '__main__':
    case = TestCase()
    # case.test_alert()
    # case.test_confirm()
    case.test_prompt()
    case.driver.quit()

