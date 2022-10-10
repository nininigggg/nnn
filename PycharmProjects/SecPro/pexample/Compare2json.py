# 方法一：引入json_tool类
# 安装pip install json_tools
# 使用json_tools.diff(old,new)
# 读取两个json文件，利用diff比对，将比对结果存于文件中
import datetime
import json
import os
import json_tools as json_tools

with open('data/03.json', 'r', encoding='utf-8') as f:
    new01 = json.load(f)
with open('data/04.json', 'r', encoding='utf-8') as f:
    old01 = json.load(f)
c_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
with open(os.path.join("data/compare", "cmp{}.json".format(c_time)), "w+", encoding='utf-8') as f:
    json.dump(json_tools.diff(old01, new01), f, ensure_ascii=False, indent=4)


# 方法二：zip()函数
# import json
#
# with open("data/01.json", "r") as f:
#     dict1 = json.load(f)
#     # print(dict1)
# with open("data/02.json", "r") as f:
#     dict2 = json.load(f)
#
# for src_list, dst_list in zip(sorted(dict1), sorted(dict2)):
#     if str(dict1[src_list]) != str(dict2[dst_list]):
#         print(src_list, dict1[src_list], dst_list, dict2[dst_list])
#         # print(list(zip(sorted(dict1), sorted(dict2)))) #[('case1', 'case1'), ('case2', 'case2'), ('case3', 'case3')]

# 方法三：递归
# import json
#
# with open("data/03.json", "r") as f:
#     dict1 = json.load(f)
#     # print(dict1)
# with open("data/04.json", "r") as f:
#     dict2 = json.load(f)
#
#
# def cmp(src_data, dst_data):
#     if isinstance(src_data, dict):
#         """若为dict格式"""
#         for key in dst_data:
#             if key not in src_data:
#                 print("src不存在这个key")
#         for key in src_data:
#             if key in dst_data:
#                 """递归"""
#                 cmp(src_data[key], dst_data[key])
#             else:
#                 print("dst不存在这个key")
#     elif isinstance(src_data, list):
#         """若为list格式"""
#         if len(src_data) != len(dst_data):
#             print("list len: '{}' != '{}'".format(len(src_data), len(dst_data)))
#         for src_list, dst_list in zip(sorted(src_data), sorted(dst_data)):
#             """递归"""
#             cmp(src_list, dst_list)
#     else:
#         if str(src_data) != str(dst_data):
#             print(src_data, dst_data)
#
#
# if __name__ == '__main__':
#     cmp(dict1, dict2)
