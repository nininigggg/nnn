import json

def get_json():
    with open('demo.json', 'r') as f:
        # 解码json数据返回python字典对象
        # data = json.loads(f.read())
        # 从json文件中读取数据并返回python字典对象
        data = json.load(f)
        # print(data, type(data))
        # {'name:': 'hogwarts ', 'detail': {'course': 'python', 'city': '北京'}, 'remark': [1000, 666, 888]} <class 'dict'>
        # 将python字典对象编译成json字符串
        # s = json.dumps(data, ensure_ascii=False)
        # 将python字典对象编译成json字符串 并写入文件中
        # s = json.dump(data, f)
        print(s, type(s))

        #{"name:": "hogwarts ", "detail": {"course": "python", "city": "北京"}, "remark": [1000, 666, 888]} <class 'str'>

if __name__=='__main__':
    get_json()