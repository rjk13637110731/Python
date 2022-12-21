number = int(input("请输入整数边长："))
print("* " * number)
for item in range(number - 2):
    print("* " + "  " * (number - 2) + "*")
print("* " * number)
