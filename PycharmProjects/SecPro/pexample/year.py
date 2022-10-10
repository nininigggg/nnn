# year = int(input("输入一个年份: "))
# if (year % 4) == 0:
#     if (year % 100) == 0:
#         if (year % 400) == 0:
#             print("{0} 是闰年".format(year))  # 整百年能被400整除的是闰年
#         else:
#             print("{0} 不是闰年".format(year))
#     else:
#         print("{0} 是闰年".format(year))  # 非整百年能被4整除的为闰年
# else:
#     print("{0} 不是闰年".format(year))

try:
    year = int(input("请输入一个年份："))
    if year <= 0 or year > 9999:
        print("输入年份：{} 您输入有误！".format(year))
    else:
        if (year % 4 == 0) and (year % 100 != 0) or (year % 400) == 0:
            print("{}年是闰年".format(year))
        else:
            print("{}年不是闰年".format(year))
except ():
    print("您输入有误！")
