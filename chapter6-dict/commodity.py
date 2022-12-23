dict_commodity_info = {}
while True:
    name = input("请输入商品名称：")
    if name == "":
        break
    price = float(input("请输入商品的价格："))
    dict_commodity_info[name] = price

for key, value in dict_commodity_info.items():
    print(f"{key}商品的单价是：{value}元/斤")
