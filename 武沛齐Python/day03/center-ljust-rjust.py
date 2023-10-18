name = "小白大神"
text1 = name.center(13, "*")  # 13指定长度，"*"填充字符
text2 = name.ljust(13, "#")
text3 = name.rjust(13, "&")
print(text1)
print(text2)
print(text3)

# 输出
*****小白大神****
小白大神#########
&&&&&&&&&小白大神
