import pytest


# fixture作用域
# 定义登陆的fixture，尽量避免以test_开头

# @pytest.fixture(scope="class")
# def login():
#     # setup操作
#     print("登陆操作")
#     token = "aaaaaaaaa"
#     yield token  # 相当于return
#     # teardown 操作
#     print("登出操作")


def test_search(login):
    # login返回none
    token = login
    print(f"token : { token }")
    print("搜索")


def test_cart():
    print("购物车")


def test_order():
    print("下单")


def test_get_product(connectDB):
    print("验证 获取单品信息")