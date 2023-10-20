file_data = open("user_info1.txt", mode="ab")
while True:
    user = input("请输入用户名：")
    if user.upper() == "Q":
        break
    pwd = input("请输入密码：")
    if pwd.upper() == "Q":
        break

    line = "{},{}\n".format(user, pwd)
    file_data.write(line.encode("utf-8"))
file_data.close()

login_data = open("user_info1.txt", mode="rb")
user_in = input("请输入用户名")
for line_in in login_data:
    line_data = line_in.decode("utf-8").strip().split(",")
    if user_in in line_data:
        pwd_in = input("请输入密码")
        if pwd_in in line_data:
            print("登陆成功")
        else:
            print("登录失败")
            break

login_data.close()
