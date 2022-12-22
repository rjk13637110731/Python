list_temp = []
for item in range(10):
    list_temp.append(str(item))
result = "".join(list_temp)
print(result)
print(type(result))
# 优点是：每次循环只向列表中添加字符串，没有创建新列表
# join:list ---> str(把列表编程字符串)
result = "*".join(list_temp)
print(result)
