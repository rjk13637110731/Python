data_list = {
    '5 编译器和解释器.mp4',
    '17 今日作业.mp4',
    '9 Python解释器种类.mp4',
    '16 今日总结.mp4',
    '2 课堂笔记的创建.mp4',
    '15 Pycharm使用和破解 (win系统).mp4',
    '12 python解释器的安装 (mac系统).mp4',
    '13 python解释器的安装(win系统).mp4',
    '8 Python介绍.mp4',
    '7 编程语言的分类.mp4',
    '3 常见计算机基本概念.mp4"14 Pycharm使用和破解 (mac系统).mp410 CPython解释器版本.mp4',
    '1 今日概要.mp4',
    '6 学习编程本质上的三件事.mp4',
    '18 作业答案和讲解.mp4',
    '20 编程语言.mp4',
    '11 环境搭建说明.mp4'
}

# 获取列表中的序号
result1 = [item.split(" ")[0] for item in data_list]
print(result1)
result2 = [int(item.split(" ")[0]) for item in data_list]
print(result2)

# 输出
['7', '13', '17', '11', '3', '15', '5', '8', '1', '20', '2', '9', '12', '18', '6', '16']
[7, 13, 17, 11, 3, 15, 5, 8, 1, 20, 2, 9, 12, 18, 6, 16]
