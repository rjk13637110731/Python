import random
score = 0
for item in range(3):
    random_num1 = random.randint(1, 100)
    random_num2 = random.randint(1, 100)
    print(str(random_num1) + " + " + str(random_num2) + " = ")
    if int(input("请输入两个数计算之和：")) == (random_num1 + random_num2):
        score += 10
print(score)
