ip = "192.168.11.23"
ip_list = ip.split(".")
ip_change = []
for item in ip_list:
    data = bin(int(item))
    data_split = data[2:].zfill(8)
    ip_change.append(data_split)

ip_join = "".join(ip_change)

num = int(ip_join, base=2)
print(num)


# 输出
3232238359
