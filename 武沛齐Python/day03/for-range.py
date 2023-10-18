message = "伤情最是晚凉天，憔悴私人不堪言"

for item in message:
    print(item)

for i in range(len(message) - 1, -1, -1):
    print(message[i])

text = input("请输入文本：")
cout = 0
for i in range(len(text)):
    if text[i] == "浪":
        cout += 1
data = "浪出现的次数{}".format(count)
print(data)
