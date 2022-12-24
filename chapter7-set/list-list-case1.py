list01 = ["a", "b", "c"]
list02 = ["A", "B", "C"]
list03 = [r + c for r in list01 for c in list02]
print(list03)
