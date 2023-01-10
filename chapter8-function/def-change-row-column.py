list01 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
for c in range(1, len(list01)):
    for r in range(c, len(list01)):
        list01[r][c - 1], list01[c - 1][r] = list01[c - 1][r], list01[r][c - 1]

print(list01)
