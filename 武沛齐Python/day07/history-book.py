import os
from datetime import datetime

DB_FOLDER = "db"


def history(user_file_path):
    # 1.检测文件是否存在
    if not os.path.exists(user_file_path):
        print("无历史记录")
        return
    # 2.存在逐行打印文件内容
    print("====历史记录====")
    with open(user_file_path, mode='r', encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            print(line)


def booking(user_file_path):
    # 预定
    location = input("请输入景区名称>>>")
    count = input("订票数量>>>")
    ctime_string = datetime.now().strftime("%Y-%m-%d-%H-%M")
    line = "{},{},{}".format(location, count, ctime_string)

    with open(user_file_path, mode='a', encoding="utf-8") as f:
        f.write(line)


def run():
    # 1.检测db文件是否存在，不存在就创建
    if not os.path.exists(DB_FOLDER):
        os.makedirs(DB_FOLDER)

    # 2.输入用户名
    name = input("Enter>>>")
    file_path = os.path.join(DB_FOLDER, "{}.txt".format(name))
    if os.path.exists(file_path):
        print("欢迎老用户")
    else:
        print("新用户")

    # 3.功能的选择
    func_dict = {
        "1": history,
        "2": booking
    }

    while True:
        print("1.查询历史订单，2.预定")
        choice = input("请选择（Q/q）:")
        if choice.upper() == "Q":
            return
        func = func_dict.get(choice)
        if not func:
            print("序号输入错误，请重新输入！")
            continue
        func(file_path)


run()
