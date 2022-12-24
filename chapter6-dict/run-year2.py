list_run = [item for item in range(1970, 2051) if (item % 4 == 0 and item % 100 != 0) or (item % 400 == 0)]
print(list_run)
