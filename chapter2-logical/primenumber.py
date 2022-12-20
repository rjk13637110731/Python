num = int(input("请输入整数："))
if num <= 1:
    print("不是素数")
else:
    for item in range(2, num):
        if num % item == 0:
            print("不是素数")
            break  # 若发现满足条件的数字，就不再判断后面的了，不执行else语句。
    else:
        print("是素数")
