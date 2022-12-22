list_score = []
# 录入过程
while True:
    str_score = input("请输入成绩：")
    if str_score == "":
        break
    list_score.append(int(str_score))
# 输出过程
for item in list_score:
    print(item)
print(f"最高分：{max(list_score)}")
print(f"最低分：{min(list_score)}")
print(f"平均分：{sum(list_score) / len(list_score)}")
