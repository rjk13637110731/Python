file_data = open("user_info.txt", mode="wb")
while True:
    user = input("请输入用户名：")
    if user.upper() == "Q":
        break
    pwd = input("请输入密码：")
    if pwd.upper() == "Q":
        break

    line = "{},{}\n".format(user, pwd)

    # 写到计算机内存中了（缓冲区），还没写到文件中（硬盘中）
    file_data.write(line.encode("utf-8"))

    # 强制将内存中的数据写到硬盘中(文件中)
    file_data.flush()
file_data.close()
