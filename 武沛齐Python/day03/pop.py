# 排队买票
# 1. 排队买票的人
user_queue = []
while True:
    name = input("上海-北京火车票。购买者姓名（Q/q）:")
    if name.upper() == "Q":
        break
    user_queue.append(name)

# 2.放了3张票
for i in range(3):
    user_name = user_queue.pop(0)
    message = "恭喜{}，购买成功".format(user_name)
    print(message)

# 3.通知其他人无票，请选择其他出行方式
others = "，".join(user_queue)
data = "票已售罄，请以下成员选择其他出行方式：{}".format(others)
print(data)
