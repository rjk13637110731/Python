# 案例
name_list = []
while True:
    name = input("请输入购买火车票用户姓名（Q/q退出）：")
    if name.upper() == "Q":
        break
    if name.startswith("刁"):
        name_list.insert(0, name)
    else:
        name_list.append(name)
print(name_list)
