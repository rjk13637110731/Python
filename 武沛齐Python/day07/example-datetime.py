import hashlib
import datetime

DB_FILE_PATH = "db.txt"
SALT = "addhashhash"


def md5(data_string):
    salt = SALT
    # md5加密
    obj = hashlib.md5(salt.encode("utf-8"))
    obj.update(data_string.encode('utf-8'))
    res = obj.hexdigest()
    return res


def login():
    print("用户登录")
    user = input("请输入用户名：")
    pwd = input("请输入用密码：")
    encrypt_pwd = md5(pwd)

    # 逐行读取文件中的内容，然后进行比较
    is_success = False
    with open(DB_FILE_PATH, mode="r", encoding="utf-8") as file_object:
        for line in file_object:
            data_list = line.strip().split(",")
            if data_list[0] == user and data_list[1] == encrypt_pwd:
                is_success = True
    if is_success:
        print("登陆成功")
    else:
        print("登录失败")


def register():
    print("用户注册")
    user = input("请输入用户名：")
    pwd = input("请输入用密码：")
    encrypt_pwd = md5(pwd)
    date_string = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = "{},{},{}\n".format(user, encrypt_pwd, date_string)
    with open(DB_FILE_PATH, mode="a", encoding="utf-8") as file_object:
        file_object.write(line)


def run():
    func_dict = {
        "1": register,
        "2": login
    }

    print("1.注册，2.登录")
    choice = input("序号：")
    func = func_dict.get(choice)
    if not func:
        print("序号选择错误")
        return
    func()


run()
