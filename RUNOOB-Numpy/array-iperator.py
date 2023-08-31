import numpy as np
a = np.arange(9).reshape(3,3)
for row in a:
    print(row)
for element in a.flat:
    print(element)



import numpy as np
a = np.arange(8).reshape(2,4)
print ('原数组：')
print (a)
print ('\n')
# 默认按行
print(a.flatten())
print(a.flatten(order='F'))



import numpy as np
a = np.arange(8).reshape(2,4)
print ('原数组：')
print (a)
print ('\n')
print ('调用 ravel 函数之后：')
print (a.ravel())
print ('\n')
print ('以 F 风格顺序调用 ravel 函数之后：')
print (a.ravel(order = 'F'))
