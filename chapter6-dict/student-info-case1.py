dict_commodity_info = {}
while True:
    name = input("请输入姓名：")
    if name == "":
        break
    age = int(input("请输入年龄："))
    score = int(input("请输入成绩："))
    sex = input("请输入性别：")
    dict_commodity_info[name] = [age, score, sex]

for name, list_info in dict_commodity_info.items():
    print(f"{name}的年龄是：{list_info[0]}岁，成绩是：{list_info[1]}，性别是：{list_info[2]}")
