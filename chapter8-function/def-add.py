def add(number01, number02):
    result = number01 + number02  # 逻辑计算（定义者）
    return result  # 上面两行代码简化为：return number01 + number02


number01 = int(input("请输入第一个数字："))  # 获取数据，调用者
number02 = int(input("请输入第二个数字："))
result = add(number01, number02)
print("结果是：" + str(result))  # 显示结果（调用者）
