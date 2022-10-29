import time

from selenium.webdriver.common.by import By

from web_test.base import Base

# import allure
from web_test.log_utils import logger


# 问题一：当有异常是期望用例不通过，吐过不抛出异常，则用例状态其实为通过
# 解决方式 except 处理截图等之后 raise e
# 问题二：抛出异常等操作与用例解耦
# 解决方式：定义装饰器，用例方法调用装饰器
# def ui_exception_record(func):
#     def run(*args, **kwargs):
#         try:
#             func(*args, **kwargs)
#         except:
#             pass
#
#     return func
# 问题三：

def ui_exception_record(func):
    def run(*args, **kwargs):
        self = args[0]
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # 这里添加所有的异常情况处理
            # 日志
            logger.warning("执行过程中发生异常")
            # 截图
            timestamp = int(time.time())
            image_path = f"../images/image_{timestamp}.PNG"
            page_source_path = f"../page_source/{timestamp}_page_source.html"
            # page_source
            with open(f"../page_source/{timestamp}_page_source.html", "w", encoding="u8") as f:
                f.write(self.driver.page_source)
            self.driver.save_screenshot(image_path)
            # allure.attach.file(image_path, name="image", attachment_type=allure.attachment_type.PNG)
            # # allure.attach.file(page_source_path, name="page_source", attachment_type=allure.attachment_type.HTML)
            # allure.attach.file(page_source_path, name="page_source", attachment_type=allure.attachment_type.TEXT)
            raise e

    return run


class TestShot(Base):
    @ui_exception_record
    def test_shot(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element(By.ID, "su1")

# class TestShot(Base):
#     def test_shot(self):
#         self.driver.get("https://www.baidu.com")
#         try:
#             self.driver.find_element(By.ID, "su1")
#         except Exception:
#             # print("出现异常啦")
#             timestamp = int(time.time())
#             # 截图存放路径
#             image_path = f"../image/image_{timestamp}.PNG"
#             # page_source存放路径
#             page_source_path = f"../page_source/page_source{timestamp}.html"
#             # 获取截图
#             self.driver.save_screenshot(image_path)
#             # 获取page_source
#             with open(page_source_path, "w", encoding="u8") as f:
#                 f.write(self.driver.page_source)
#
#             # 测试报告加截图和page_source
#             allure.attach.file(image_path, name="picture",
#                                attachment_type=allure.attachment_type.PNG)
#             allure.attach.file(page_source_path, name="pagesource",
#                                attachment_type=allure.attachment_type.HTML)
