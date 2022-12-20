month=int(input("请输入月份："))
if month < 1 or month > 12:
    print("输入有误")
elif month >= 10:
    print("冬")
elif month >= 7:
    print("秋")
elif month >= 4:
    print("夏")
elif month >= 1:
    print("春")
