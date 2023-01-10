def get_day_by_month(year, month):
    if month < 1 or month > 12:
        return "输入有误！"  # -1,返回值-1或者0
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return "29天"  # 29,返回整型，不建议方法的返回值类型可能是多种
        else:
            return "28天"
    if month in (4, 6, 9, 11):
        return "30天"
    return "31天"
