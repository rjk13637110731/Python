height = 100
count = 0
distance = 0
while height / 2 > 0.01:
    count += 1
    height /= 2
    # 计算总共走了多少m
    distance += height * 2
print("总共弹起来%d" % count)  # 只有一个变量，可以不用括号
print("总共走了%fm" % distance)
