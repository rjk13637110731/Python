sum = 0
for item in range(1,101):
    if item % 5 != 0:   #不满足则跳过
        continue   # 跳过本次循环，继续下次循环，continue语句
    sum += item
print(sum)
