def func(*a1):
    # 同意被打包成元组
    print(a1)


func(1)
func(11, 22, 33)
func(11, 22, [11, "aa", True], ("Hello", "World"), False)
func([11, 22, 33])
func((11, 22, 33))


# 输出
(1,)
(11, 22, 33)
(11, 22, [11, 'aa', True], ('Hello', 'World'), False)
([11, 22, 33],)
((11, 22, 33),)
