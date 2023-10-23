"""
用户注册
    - 用户信息需要存储在 db/users/account.txt 文件中
"""

import os

while True:
    user = input("用户名：")
    line = "{}\n".format(user)

    folder_path = os.path.join("db", "users")
    if not os.path.exists(folder_path):
        # 创建目录
        os.makedirs(folder_path)

    file_path = os.path.join(folder_path, "account.txt")
    # 文件夹必须已存在
    file_object = open(file_path, mode="a", encoding="utf-8")
    file_object.write(line)
    file_object.close()
