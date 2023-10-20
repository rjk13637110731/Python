def func(data_string, key="a"):
    num = 0
    for item in data_string:
        if item == key:
            num += 1
    return num


res0 = func("adkvjavsosdhjadf jpojfowjadfahsfgc[aaDadf")
print(res0)

res1 = func("adkvjavsosdhjadf jpojfowjadfahsfgc[aaDadf", "a")
print(res1)

res2 = func("adkvjavsosdhjadf jpojfowjadfahsfgc[aaDadf", "d")
print(res2)

# 输出
8
8
5
