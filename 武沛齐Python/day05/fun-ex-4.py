
def data_sum(*args):
    res = 0
    for item in args:
        res += item
    return res


res = data_sum(11, 22, 33, 44, 55, 66, 77)
print(res)

# 输出
308
