import allure


@allure.feature("搜索模块")
class TestSearch():
    @allure.story("搜索成功")
    def test_case1(self):
        print("case1")

    @allure.story("搜索失败")
    def test_case1(self):
        print("case2")


@allure.feature("登陆模块")
class TestLogin():
    @allure.story("登陆成功")
    def test_login_success(self):
        with allure.step("步骤1：打开应用"):
            print("打开应用")
        with allure.step("步骤2：进入登陆页面"):
            print("登陆页面")
            # allure.attach.file("", name='截图')
            # allure.attachment_type.JPG
        with allure.step("步骤3：输入用户名信息"):
            print("输入用户名和密码")
        with allure.step("步骤4：成功登陆"):
            print("这是登陆：测试用例，登陆成功")

    @allure.story("登陆成功")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_success_b(self):
        print("这是登陆：用户名缺失")

    @allure.story("登陆失败")
    def test_login_failure(self):
        print("打开应用")
        print("登陆页面")
        print("输入用户名和密码")
        print("这是登陆：测试用例，登陆失败")
