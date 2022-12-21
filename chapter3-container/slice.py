message = "我叫小猪佩奇"
print(message[0:2])
print(message[:2])  # 与上一行代码等同，省略0不写
print(message[-2:])  # 结束值默认是末尾
print(message[:])  # 全部字符
print(message[-2:-5:-1])  # 倒着输出
print(message[::-1])  # 倒着输出
print(message[1:1])  # 空，取不到内容
print(message[3:1])  # 空，索引越界，切片可越界，但不报错，取不到值
