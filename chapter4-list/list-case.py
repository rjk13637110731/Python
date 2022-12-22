list_number = []
for item in range(5):
    number = int(input(f"请输入第{item}个数字："))
    list_number.append(number)
max_number = list_number[0]
for item in list_number:
    if max_number < item:
        max_number = item
print(max_number)
