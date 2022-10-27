import time

from selenium.webdriver.common.by import By

from web_test.base import Base

"""
1.打开百度
2.点击登陆
3.弹窗中点击"立即注册"，输入用户名和账号
4.返回刚才的登陆页面
5.输入用户名和密码点击登陆

"""


class TestWindows(Base):
    def test_window(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.ID, "s-top-loginbtn").click()
        # print(self.driver.current_window_handle)
        # print(self.driver.window_handles)
        self.driver.find_element(By.ID, "TANGRAM__PSP_11__regLink").click()
        # print(self.driver.current_window_handle)
        # print(self.driver.window_handles)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        # print(self.driver.current_window_handle)

        self.driver.find_element(By.ID, "TANGRAM__PSP_4__userName").send_keys("username")
        self.driver.find_element(By.ID, "TANGRAM__PSP_4__phone").send_keys("18900000000000")
        time.sleep(3)
        self.driver.switch_to.window(windows[0])
        # print(self.driver.current_window_handle)
        self.driver.find_element(By.ID, "TANGRAM__PSP_11__submit").click()
        time.sleep(3)

