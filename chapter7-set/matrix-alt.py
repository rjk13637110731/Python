list01 = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
result = []
for r in range(4):
    for c in range(r + 1, 4):
        list01[r][c], list01[c][r] = list01[c][r], list01[r][c]
print(list01)
