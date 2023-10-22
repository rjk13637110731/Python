def func():
    return 123


data_list = [11, 22, 33, func]
# 循环每个元素，如果可执行则执行并获取返回值
for item in data_list:
    if callable(item):
        res = item()
        print(res)
    else:
        print(item)

# 输出
11
22
33
123
