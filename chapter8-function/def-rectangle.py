# 定义函数：起函数名建议使用动词
def print_rectangle(row, column):
    """
    绘制矩形图
    :param row:行
    :param column:列
    :return:
    """
    for r in range(row):
        for c in range(column):
            print("*", end=" ")
        print()


# 调用函数：
print_rectangle(3, 4)
