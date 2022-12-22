list_tick = []
while len(list_tick) < 6:
    number = int(input("请输入第%d个红球号码：" % (len(list_tick) + 1)))
    if number < 1 or number > 33:
        print("号码不在范围内")
    elif number in list_tick:
        print("号码已重复")
    else:
        list_tick.append(number)
while len(list_tick) < 7:
    number = int(input("请输入蓝球号码："))
    if 1 <= number <= 16:
        list_tick.append(number)
    else:
        print("号码不在范围内")
print(list_tick)
