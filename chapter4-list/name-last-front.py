list_name = []
while True:
    name = input("请输入姓名：")
    if name == "":
        break
    if name not in list_name:
        list_name.append(name)
    else:
        print(f"姓名{name}已经存在")
for item in range(len(list_name)):
    print(list_name[-(item + 1)])
