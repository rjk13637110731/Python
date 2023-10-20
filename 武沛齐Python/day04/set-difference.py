# 方式1：
v1 = {"小白", "小小白", "大神"}
v2 = {"小白", "大大神", "高手"}
res1 = v1.difference(v2)  # v1中有，但v2里面没有
res3 = v2.difference(v1)  # v2中有，但v1中没有
# 方式2：
res2 = v1 - v2
res4 = v2 - v1
print(res1)
print(res2)
print(res3)
print(res4)


# 输出
{'大神', '小小白'}
{'大神', '小小白'}
{'大大神', '高手'}
{'大大神', '高手'}
