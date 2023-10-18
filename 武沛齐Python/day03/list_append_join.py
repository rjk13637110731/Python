name = []
flag = True
while flag:
    data = input("》》》")
    if data == "q" or data == "Q":
        flag = False
        data_print = ", ".join(name)
        print(data_print)
    else:
        name.append(data)

# 输出
》》》小白
》》》小小白
》》》大神
》》》大大神
》》》q
小白, 小小白, 大神, 大大神
