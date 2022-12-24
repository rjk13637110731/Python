list01 = [3, 80, 45, 5, 80, 1]
result = False
for r in range(len(list01) - 1):
    for c in range(r + 1, len(list01)):
        if list01[r] == list01[c]:
            print(f"具有相同的元素：{list01[r]}")
            result = True
if not result:
    print("没有相同项")
