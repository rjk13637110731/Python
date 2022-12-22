list01 = [9, 25, 12, 8]
for item in range(len(list01) - 1, -1, -1):
    if list01[item] > 10:
        list01.remove(list01[item])
print(list01)
