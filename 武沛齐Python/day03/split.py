file_name = "day01 python编程入门.mp4"

# 切割字符串后得到的是一个列表
# 索引           0                    1
# data_list = ["day01 python编程入门","mp4"]
data_list = file_name.split(".")
print(data_list)
print(data_list[0])
print(data_list[1])

# 输出
['day01 python编程入门', 'mp4']
day01 python编程入门
mp4
