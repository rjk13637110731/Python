text = input(">>>")
data_list = text.split("+")
for i in data_list:
    if i.isdecimal():
        if i == data_list[-1]:
            num1 = int(data_list[0])
            num2 = int(data_list[1])
            data = num1 + num2
            print(data)
    else:
        print("输入有误")

# 输出
>>>5+5+中
输入有误
>>>2+3
5
