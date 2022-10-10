import logging


def inc(x):
    return x + 1


def test_answer():
    logging.info("这是 answer 测试用例")
    logging.info("断言 assert inc(3) == 5")

    assert inc(3) == 5


class TestDemo:
    def test_demo1(self):
        logging.info("这是 answer 测试用例")
        pass

    def test_demo2(self):
        logging.info("这是 answer 测试用例")
        pass
