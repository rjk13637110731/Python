list01 = ["a", "b", "c"]
list02 = ["A", "B", "C"]
list03 = []
for r in list01:
    for c in list02:
        list03.append(r + c)
print(list03)
