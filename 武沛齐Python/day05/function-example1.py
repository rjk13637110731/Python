def count(str_a):
    num = 0
    for item in str_a:
        if item == "a":
            num += 1
    return num


res = count("abceefgabsjojjopaaDVSA")
print(res)

# 输出
4
