string01 = input("请输入一个字符串：")
dict01 = {}
for item in string01:
    if item not in dict01:
        dict01[item] = 1
    else:
        dict01[item] += 1
print(dict01)
