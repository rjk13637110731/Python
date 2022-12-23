dict01 = dict([("a", "b"), ("c", "d")])
dict01["e"] = "f"
for item in dict01.items():
    print(item[0])  # 得到的是字典中的键
    print(item[1])  # 得到的是字典中的值
