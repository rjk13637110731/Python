list_string = []
while True:
    string_inp = input("请输入字符串：")
    if string_inp == "":
        break
    list_string.append(string_inp)
result = "".join(list_string)
print(result)
