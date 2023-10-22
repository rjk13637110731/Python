def do():
    print("do")

def func(a1,a2):
    print(a1)
    res = a2()
    print(res)
    return 123

res = func(11,do)
print(res)

# 输出
11
do
None
123
