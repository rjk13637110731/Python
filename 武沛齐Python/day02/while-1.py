print("开始")

count = 0
while count < 3:
    num = int(input("请输入猜测数字："))
    if num > 66:
        print("大了")
    elif num < 66:
        print("小了")
    else:
        print("正确")
        break
    count += 1

print("结束")
