def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def get_day_by_month(year, month):
    if month < 1 or month > 12:
        return 0
    if month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    if month in (4, 6, 9, 11):
        return 30
    return 31


re = get_day_by_month(2023, 1)
print(re)
