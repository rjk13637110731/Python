data = "中国联通"
v1 = data.encode("utf-8")  # 将unicode编码的字符串压缩成utf-8编码
print(v1)

v2 = v1.decode("utf-8")  # 解压缩成字符串型unicode
print(v2)

# 输出
b'\xe4\xb8\xad\xe5\x9b\xbd\xe8\x81\x94\xe9\x80\x9a'
中国联通
