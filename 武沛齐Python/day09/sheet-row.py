import os
from openpyxl import load_workbook

# 1.获取work_book对象
file_path = os.path.join("files", "output.xlsx")
work_book_object = load_workbook(file_path)

# 2.获取所有的sheet对象（内部包含很多数据）
sheet_object_list = work_book_object.worksheets

# 3.获取某一个sheet对象：方式1:
sheet_object = sheet_object_list[0]

# 4.读取sheet中的某一行的数据:如第一行数据，excel中读取行时，是从1开始的，不是从0开始
row_list = sheet_object[1]
# 读取行对象是从0开始，这是Python规定的，读取excel行列数据时从1开始，这是Excel规定的
print(row_list[0])
for cell_object in row_list:
    print(cell_object.value)
    
# 输出
-0.015709151
-0.015700703
-0.14263368
