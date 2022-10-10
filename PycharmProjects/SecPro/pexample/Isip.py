# 方法一：
# def is_ipv4(ip: str) -> bool:
#     """
#     检查ip是否合法
#     """
#     for x in ip.split("."):
#         if [1] * 4 == [x.isdigit() and 0 <= int(x) <= 255]:
#             return True
#         else:
#             return False
#
#
# print(is_ipv4("192.168.1.2a0"))

# 方法二：
# def fun(ip):
#     ip = str(ip).split(".")
#     if len(ip) != 4:
#         raise Exception("格式不正确，请输入正确的ip地址")
#     a, b, c, d = ip
#     a, b, c, d = int(a), int(b), int(c), int(d)
#     if 255 >= max(a, b, c, d) and 0 <= min(a, b, c, d):
#         # print("输入的是正确的ip{}地址!".format(".".join(ip)))
#         return True
#     else:
#         raise Exception("非法ip  {}".format(".".join(ip)))
#         return False

# 方法三：
# import re
#
#
# def isIP(str):
#     p = re.compile(’^(2[0-4][0-9].|25[0-5].|[01]{,1}[0-9]{1,2}.){3}(‘2[0-4][0-9]|25[0-5]|[01]{,1}[0-9]{1,2}’)$’)
#     if p.match(str):
#         return True
#     else:
#         return False
#
#
# myStr = "255.255.abc.255"
#
# if isIP(myStr):
#     print(myStr, "is a IP!")
# else:
#     print(myStr, "is not a IP!")

# 方法四：
import IPy


def is_ip(ip):
    try:
        IPy.IP(ip)
        return True
    except Exception as e:
        return False
