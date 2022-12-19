weight_liang = int(input("请输入两："))
jin = weight_liang // 16  # 求商
liang = weight_liang % 16  # 求余
print(str(jin) + "斤零" + str(liang) + "两")
