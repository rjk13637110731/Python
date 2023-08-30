import numpy as np
a = np.arange(10)
s = slice(2,7,2)
print(a[s])



import numpy as np
a = np.arange(10)
b = a[2:7:2]
print(b)



import numpy as np
a = np.arange(10)
b = a[5]
print(b)



import numpy as np
a = np.arange(10)
b = a[5:]
print(b)



import numpy as np
a = np.arange(10)
b = a[2:5]
print(b)



import numpy as np
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
b = a[1:]
print(b)



import numpy as np
 
a = np.array([[1,2,3],[3,4,5],[4,5,6]])  
print (a[...,1])   # 第2列元素
print (a[1,...])   # 第2行元素
print (a[...,1:])  # 第2列及剩下的所有元素
