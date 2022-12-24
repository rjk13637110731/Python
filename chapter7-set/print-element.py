list01 = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
# 打印第二行第三列元素
print(list01[2][3])
# 打印第三行所有元素
for item in list01[2]:
    print(item)
# 打印第一列所有元素
for r in range(len(list01)):
    print(list01[r][0])
