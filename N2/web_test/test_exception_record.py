# 装饰器逻辑
import time

import allure

from web_test.log_utils import logger


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
            image_path = f"./images/image_{timestamp}.PNG"
            page_source_path = f"./page_source/{timestamp}_page_source.html"
            # page_source
            with open(f"./page_source/{timestamp}_page_source.html", "w", encoding="u8") as f:
                f.write(self.driver.page_source)
            self.driver.save_screenshot(image_path)
            allure.attach.file(image_path, name="image", attachment_type=allure.attachment_type.PNG)
            # allure.attach.file(page_source_path, name="page_source", attachment_type=allure.attachment_type.HTML)
            allure.attach.file(page_source_path, name="page_source", attachment_type=allure.attachment_type.TEXT)
            raise e
    return run