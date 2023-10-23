from datetime import datetime, timedelta

v1 = datetime.now()
res = v1 + timedelta(days=280, hours=28, minutes=10, seconds=100)

print(v1, type(v1))
print(res, type(res))

date_string = datetime.strftime(res, '%Y-%m-%d %H:%M:%S')
print(res)

# 输出
2023-10-23 20:30:45.246364 <class 'datetime.datetime'>
2024-07-31 00:42:25.246364 <class 'datetime.datetime'>
2024-07-31 00:42:25.246364
