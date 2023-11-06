class UserInfo:
    def __init__(self, a1, a2):
        self.username = a1
        self.password = a2


# [对象]
user_list = []
while True:
    user = input("Enter username:")
    if user.upper() == "Q":
        break
    pwd = input("Enter password:")

    # 1.实例化一个对象，空对象
    # 2.执行__init__方法
    obj = UserInfo(user, pwd)

    user_list.append(obj)
for item in user_list:
    msg = "{}={}".format(item.username, item.password)
    print(msg)

# 输出
Enter username:小猪佩奇
Enter password:1232
Enter username:小白
Enter password:2345
Enter username:q
小猪佩奇=1232
小白=2345
