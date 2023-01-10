def get_score_level(score):
    if score > 100 or score < 0:
        return "输入有误！"  # return具有退出程序的作用，不用elif了
    if score >= 90:
        return "优秀！"
    if score >= 80:
        return "良好！"
    if score >= 60:
        return "及格！"
    return "不及格！"


re = get_score_level(80)
print(re)
