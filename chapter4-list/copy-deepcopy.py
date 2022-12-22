list01 = [800, [1000, 500]]
# 浅拷贝
list02 = list01[:]

# 等价上行代码的浅拷贝
list02 = list01.copy()
list01[1][0] = 900
print(list02[1][0])
