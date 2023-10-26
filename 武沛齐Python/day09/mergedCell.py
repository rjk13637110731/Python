import os
from openpyxl import load_workbook
from openpyxl.cell.cell import Cell, MergedCell

# 1.获取work_book对象
file_path = os.path.join("files", "output.xlsx")
work_book_object = load_workbook(file_path)

# 2.获取所有的sheet对象（内部包含很多数据）
sheet_object_list = work_book_object.worksheets

# 3.获取某一个sheet对象：方式1:
sheet_object = sheet_object_list[1]

# 4.获取合并单元格(原始内容)
for row in sheet_object.rows:
    text_list = []
    for cell in row:
        text_list.append(cell.value)
    print(text_list)

# 5.如果是被合并的单元格的值等于 -
for row in sheet_object.rows:
    text_list = []
    for cell in row:
        # 判断cell是Cell对象则是正常单元格，如果是MergeCell对象则是合并单元格
        if type(cell) == MergedCell:
            text_list.append("-")
        elif type(cell) == Cell:
            text_list.append(cell.value)
        else:
            text_list.append("不认识")
    print(text_list)


# 输出
['用户信息', None, '备注']
['学生姓名', '学生ID', None]
['我害怕', '14789456546546', None]
[None, '14789456546545', None]
['大白菜', '14346546546541', None]
['ff', None, None]
[None, None, None]
['用户信息', '-', '备注']
['学生姓名', '学生ID', None]
['我害怕', '14789456546546', None]
['-', '14789456546545', None]
['大白菜', '14346546546541', None]
['ff', '-', '-']
['-', '-', '-']
