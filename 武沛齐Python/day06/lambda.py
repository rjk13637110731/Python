def func():
    return 123
--->
# func是函数名（变量）
# lambda:后面是函数体，函数体中写了123，内部会自动执行一个return动作
func = lambda : 123
res = func()
print(res) # 123



def func(a1,a2):
    return a1+a2
--->
func = lambda a1,a2 : a1 + a2
res = func(100,200)
print(res)  # 300



def func(data_string):
    return data.upper()
--->
func = lambda data_string : data_string.upper()
res = func("root")
print(res) # "ROOT"



def func(data_list):
    return data_list[0]
--->
func = lambda data_list : data_list[0]
res = func([11,22,33,44])
print(res)  # 11
