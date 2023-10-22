def register():
    print("注册")


def login():
    print("登录")


def show_users():
    print("展示")


func_dict = {
    "1": register,
    "2": login,
    "3": show_users
}
print("欢迎xx系统")
print("1.注册;2.登录;3.查看所有用户")

choice = input("请输入序号：")
func_choice = func_dict.get(choice)
if not func_choice:
    print("输入有误")
else:
    func_choice()
    
# 输出
欢迎xx系统
1.注册;2.登录;3.查看所有用户
请输入序号：2
登录
