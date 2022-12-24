list01 = [3, 80, 45, 5, 7, 1]
# 取元素
for r in range(len(list01) - 1):
    # 作比较
    for c in range(r + 1, len(list01)):
        # 交换元素
        if list01[r] > list01[c]:
            list01[r], list01[c] = list01[c], list01[r]
print(list01)
