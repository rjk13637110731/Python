list_person_hobby = []
while True:
    name = input("请输入姓名：")
    if name == "":
        break
    dict_person = {name: []}
    list_person_hobby.append(dict_person)
    while True:
        hobby = input("请输入喜好：")
        if hobby == "":
            break
        dict_person[name].append(hobby)
print(list_person_hobby)
