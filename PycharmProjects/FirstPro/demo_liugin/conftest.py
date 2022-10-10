from typing import Optional


def pytest_collection_modifyitems(session, config, items):
    for item in items:
# name是用例的名字 nodeid是测试用例路径
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


def pytest_runtest_setup(item: "Item") -> None:
    print("hook : setup")


def pytest_runtest_teardown(item: "Item", nextitem: Optional["Item"]) -> None:
    print("teardown")
