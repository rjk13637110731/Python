def get_score_level(score):
    if score > 100 or score < 0:
        return "输入有误！"
    elif score >= 90:
        return "优秀！"
    elif score >= 80:
        return "良好！"
    elif score >= 60:
        return "及格！"
    else:
        return "不及格！"


re = get_score_level(80)
print(re)
