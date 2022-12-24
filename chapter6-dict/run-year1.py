list_run = []
for item in range(1970, 2051):
    if (item % 4 == 0 and item % 100 != 0) or (item % 400 == 0):
        list_run.append(item)
print(list_run)
