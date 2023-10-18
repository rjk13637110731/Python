import os

data_list = os.listdir("../wupeiqiPython")
for item in data_list:
    if item.split(".")[-1].upper() == "PNG":
        print(item)

# 输出
demo.png
eeworld.png
