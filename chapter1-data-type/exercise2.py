minute = int(input("请输入分钟数："))
hour = int(input("请输入小时数："))
day = int(input("请输入天数："))
second = minute*60 + hour*3600 + day*3600*24
print("总秒数为："+str(second))
