import os

target_folder_path = r"C:\Users\FullMoon\Desktop\dan"
key = "节"
# 查看某个目录下的所有的文件和文件夹(多级目录)
data_list = os.walk(target_folder_path)
for in_path, folder_list, name_list in data_list:
    for name in name_list:
        if key in name:
            abs_path = os.path.join(in_path, name)
            print(abs_path)

# 输出
C:\Users\FullMoon\Desktop\dan\靶节点位移.txt
C:\Users\FullMoon\Desktop\dan\靶节点坐标.txt
C:\Users\FullMoon\Desktop\dan\靶节点速度.txt
