dict_person_hobby = {}
while True:
    name = input("请输入姓名：")
    if name == "":
        break
    dict_person_hobby[name] = []
    while True:
        hobby = input("请输入喜好：")
        if hobby == "":
            break
        dict_person_hobby[name].append(hobby)

# 打印
for name, list_hobby in dict_person_hobby.items():
    print(f"{name}喜欢：")
    for item in list_hobby:
        print(item)
