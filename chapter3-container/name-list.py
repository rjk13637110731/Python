name_list = []
while True:
    name = input("请输入西游记中你喜欢的人物名称：")
    name_list.append(name)
    if name == "":
        break
for item in name_list:
    print(item)
