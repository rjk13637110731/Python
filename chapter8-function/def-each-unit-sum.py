def each_unit_sum(number):
    result = number % 10
    result += number // 10 % 10
    result += number // 100 % 10
    result += number // 1000
    return result


number = int(input("请输入4位整数："))
print(each_unit_sum(number))
