import random

list_ticket = []
# 6个不重复的红球
while len(list_ticket) < 6:
    # random.randrange(1,33)能取到最后一个33，左闭右闭区间
    random_number = random.randrange(1, 33)
    # 如果随机数不存在，则存储
    if random_number not in list_ticket:
        list_ticket.append(random_number)
# 1个蓝球
list_ticket.append(random.randrange(1, 16))
print(list_ticket)
