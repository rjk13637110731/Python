month = int(input("请输入月份："))
if month < 1 or month > 12:
    print("输入有误！")
else:
    # 将每月天数存入元组中
    day_of_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # 数据的统一管理
    print(day_of_month[month - 1])
