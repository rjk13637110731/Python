list_commodity_info = []
while True:
    name = input("请输入姓名：")
    if name == "":
        break
    age = int(input("请输入年龄："))
    score = int(input("请输入成绩："))
    sex = input("请输入性别：")
    dict_info = {"name": name, "age": age, "score": score, "sex": sex}
    list_commodity_info.append(dict_info)

for dict_info in list_commodity_info:
    print(f"{dict_info['name']}的年龄是：{dict_info['age']}岁，成绩是：{dict_info['score']}，性别是：{dict_info['sex']}")
