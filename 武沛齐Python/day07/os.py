import os

file_path = os.path.join("files", "db.txt")

# 判断路径是否存在
if os.path.exists(file_path):
    # 读取文件时，如果文件不存在就会报错 FileNotFoundError
    f = open(file_path, mode="r", encoding="utf-8")
    data = f.read()
    f.close()
else:
    print("文件不存在")
