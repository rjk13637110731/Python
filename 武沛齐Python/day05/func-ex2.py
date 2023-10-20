def func(data_string, key):
    num = 0
    for item in data_string:
        if item == key:
            num += 1
    return num


res1 = func("adkvjavsosdhjadf jpojfowjadfahsfgc[aaDadf", "a")
print(res1)

res2 = func("adkvjavsosdhjadf jpojfowjadfahsfgc[aaDadf", "d")
print(res2)

# 输出
8
5
