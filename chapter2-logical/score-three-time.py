count = 0
while count < 3:
    str_score = input("请输入成绩：")
    if str_score == "":
        break  # 不执行while对应的else语句
    score = int(str_score)
    if score > 100 or score < 0:
        print("输入有误！")
        count += 1
    elif score >= 90:
        print("优秀")
    elif score >= 80:
        print("良好")
    elif score >= 60:
        print("及格")
    else:
        print("不及格")
else:
    print("成绩错误过多！")
