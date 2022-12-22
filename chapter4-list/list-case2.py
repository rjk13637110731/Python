list01 = [54, 25, 12, 42, 35, 17]
max_number = list01[0]
for item in range(len(list01) - 1):  # 可考虑以下方式：range(1,len(list01))
    if max_number <= list01[item + 1]:
        max_number = list01[item + 1]
print(max_number)
