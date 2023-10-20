def func(data):
    res = []
    for item in data:
        if item.startswith("a"):
            res.append(item)
    return res


res1 = func(["ab", "wupeiq", "cad", "abb", "caf"])
print(res1)

# 输出
['ab', 'abb']
