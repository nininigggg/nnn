# test_add.py 文件内容
# 读取json文件
import json
import pytest

from read_json.func.operation import my_add


def get_json():
    """
    获取json数据
    :return: 返回数据的结构：[[1, 1, 2], [3, 6, 9], [100, 200, 300]]
    """
    with open('../data/params.json', 'r') as f:
        data = json.loads(f.read())
        return list(data.values())


class TestWithJSON:
    @pytest.mark.parametrize('x,y,expected', get_json())
    def test_add(self, x, y, expected):
        assert my_add(int(x), int(y)) == int(expected)
