

# 读取Excel文件
import openpyxl
import pytest

from read_excel.func.operation import my_add


def get_excel():
    # 获取工作簿
    book = openpyxl.load_workbook('../data/params.xlsx')

    # 获取活动行（非空白的）
    sheet = book.active

    # 提取数据，格式：[[1, 2, 3], [3, 6, 9], [100, 200, 300]]
    values = []
    for row in sheet:
        line = []
        for cell in row:
            line.append(cell.value)
        values.append(line)
    return values

class TestWithEXCEL:
    @pytest.mark.parametrize('x,y,expected', get_excel())
    def test_add(self, x, y, expected):
        assert my_add(int(x), int(y)) == int(expected)