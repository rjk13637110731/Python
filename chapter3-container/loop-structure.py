str = input("请输入一个字符串：")
for item in range(len(str)):
    if ord(str[item]) == ord(str[-(item + 1)]):
        if item == len(str) - 1:
            print("是回文")
    else:
        print("不是回文")
        break
