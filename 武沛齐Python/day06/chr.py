# 1.随机获取65-90的数字，就可以将chr转换成字母
import random

char_list = []
for i in range(6):
    num = random.randint(65, 90)
    char = chr(num)
    char_list.append(char)

print(char_list)  # ['Q', 'N', 'A', 'V', 'Y', 'C']
code = "".join(char_list)
print(code)

# 输出
['Q', 'F', 'D', 'S', 'J', 'S']
QFDSJS
