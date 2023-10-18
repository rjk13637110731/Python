message = input(">>>")
data_list = []
for item in message:
    if item.isdecimal():
        data_list.append(item)
data_string = "".join(data_list)
bin_string = bin(int(data_string))
data = bin_string[2:]
print(data)
