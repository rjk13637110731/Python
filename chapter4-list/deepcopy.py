import copy

list01 = [800, [1000, 500]]
list02 = copy.deepcopy(list01)
list01[1][0] = 900
print(list02[1][0])
