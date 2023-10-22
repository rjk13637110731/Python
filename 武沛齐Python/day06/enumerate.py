goods = ["飞机", "迫击炮", "AK47"]

# 以前
for i in range(len(goods)):
    msg = "{} {}".format(i + 1, goods[i])
    print(msg)

# 现在
for idx, item in enumerate(goods, 1):
    msg = "{} {}".format(idx, item)
    print(msg)

# 输出
1 飞机
2 迫击炮
3 AK47
1 飞机
2 迫击炮
3 AK47
