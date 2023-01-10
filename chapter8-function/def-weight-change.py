def get_weight_for_jin(liang_weight):
    jin = liang_weight // 16
    liang = liang_weight % 16
    return (jin, liang)  # 使用元组返回两个结果，元组(斤，两)


re = get_weight_for_jin(154)
print(str(re[0]) + "斤零" + str(re[1]) + "两")
