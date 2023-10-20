
def func(**dt):
    # 自动将数据打包成字典
    print(dt)


# 必须用关键字的形式传参
func(a1=1, b1=88, c1=99)
func(a1=20, b1="kk", k1="world")

# 输出
{'a1': 1, 'b1': 88, 'c1': 99}
{'a1': 20, 'b1': 'kk', 'k1': 'world'}
