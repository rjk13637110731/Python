dict01 = dict([("a", "b"), ("c", "d")])
dict01["e"] = "f"
for k, v in dict01.items():
    print(k)  # 得到的是字典中的键
    print(v)  # 得到的是字典中的值
