import random

# 案例 抽奖
# 1.构造200名员工并存放在列表中
user_list = []
for i in range(1, 201):
    name = "工号-{}".format(i)
    user_list.append(name)

# 2.随机抽取一名员工，抽2等奖
data = random.choice(user_list)
print("获得3等奖的是：", data)

# 3.将用户从列表中删除
user_list.remove(data)
# 4.随机抽取一名员工，抽3等奖
data = random.choice(user_list)
print("获得2等奖的是：", data)

# 5.将用户从列表中删除
user_list.remove(data)

#输出
获得3等奖的是： 工号-117
获得2等奖的是： 工号-173
