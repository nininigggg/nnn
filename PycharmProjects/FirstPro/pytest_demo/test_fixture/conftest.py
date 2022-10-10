import pytest


@pytest.fixture(scope="session", autouse=True)
def login():
    # setup操作
    print("登陆操作")
    token = "aaaaaaaaa"
    yield token  # 相当于return
    # teardown 操作
    print("登出操作")


@pytest.fixture()
def connectDB():
    print("连接数据库")
    yield
    print("断开数据库")
