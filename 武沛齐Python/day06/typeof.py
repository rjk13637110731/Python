def func(data):
    """
    如果data是字符串类型则返回123
    如果data是列表则返回456
    其他返回None
    :param data:
    :return:
    """
    if type(data) == str:
        return 123
    elif type(data) == list:
        return 456
    else:
        return None


v1 = func(123)
print(v1)

# 输出
None
