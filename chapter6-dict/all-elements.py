dict01 = dict([("a", "b"), ("c", "d")])
dict01["e"] = "f"
for key in dict01:  # 遍历字典得到的是key
    print(key)  # 得到的是字典中的键
    print(dict01[key])  # 得到字典中的值
