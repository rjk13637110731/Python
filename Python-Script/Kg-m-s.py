def calculationKML(ww, ll, tt):
    w = [1 / 1000000, 1 / 1000, 1 / 1.0]
    L = [1 / 1000000, 1 / 1000, 1 / 100.0, 1 / 1.0]
    t = [1 / 1000000, 1 / 1000, 1 / 1.0]

    Energy = w[ww] * L[ll] ** 2 / (t[tt]) ** 2
    pressureValue = w[ww] / L[ll] / (t[tt]) ** 2
    velocity = L[ll] / t[tt]

    print("Energy-单位是:", '{:e}'.format(Energy), 'J')
    print("Pressure-单位是:", '{:e}'.format(pressureValue), 'Pa')
    print("velocity-单位是:", '{:e}'.format(velocity), 'm/s')


while (1):
    weight = input("请输入质量单位-mg-g-kg-exit(退出)：")

    flag1 = False
    flag2 = False

    if weight == 'exit':
        break
    elif weight != 'mg' and weight != 'g' and weight != 'kg':
        continue
    else:
        while 1:
            length = input("请输入长度单位-um-mm-cm-m：")
            if length == 'exit':
                flag1 = True
                break
            elif length != 'um' and length != 'mm' and length != 'cm' and length != 'm':
                continue
            else:
                while 1:
                    time = input("请输入时间单位-us-ms-s：")
                    if time == 'exit':
                        flag2 = True
                        break
                    elif time != 'us' and time != 'ms' and time != 's':
                        continue
                    elif time == 'us' or time == 'ms' or time == 's':
                        break
                break
        if flag1 or flag2:
            break
