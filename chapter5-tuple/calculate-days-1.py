day_of_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
month = int(input("请输入月份："))
day = int(input("请输入日："))
# 累加前几个月天数
total_day = 0
for i in range(month - 1):
    total_day += day_of_month[i]
# 累加当月天数
total_day += day
print(f"{month}月{day}日是这个月的第{total_day}天")
