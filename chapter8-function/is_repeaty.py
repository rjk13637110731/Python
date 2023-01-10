def is_reaping(list_target):
    for r in range(0, len(list_target) - 1):
        for c in range(r + 1, len(list_target)):
            if list_target[r] == list_target[c]:
                return "具有相同项！"  # 不用break，直接退出代码
    return "没有相同项！"


list01 = [1, 2, 3, 4, 5, 6, 7, 8, 88, 99, 1, 2]
re = is_reaping(list01)
print(re)
