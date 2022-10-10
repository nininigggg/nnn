import pytest


@pytest.mark.parametrize('name', ['哈利波特', '赫敏'])
def test_mm(name):
    print(f"name: {name}")


# @pytest.fixture(scope='session')
# def cmd_option(request):
#     return request.config.getoption("--env")
