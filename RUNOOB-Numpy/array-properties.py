import numpy as np
a = np.arange(24)
print(a.ndim)
b = a.reshape(2,4,3)
print(b.ndim)



import numpy as np

a = np.array([[1,2,3],[4,5,6]])
print(a.shape)



import numpy as np

a = np.array([[1,2,3],[4,5,6]])
a.shape = (3,2)
print(a)



import numpy as np

a = np.array([[1,2,3],[4,5,6]])
b = a.reshape(3,2)
print(b)



import numpy as np

x = np.array([1,2,3,4,5],dtype=np.int8)
print(x.itemsize)

y = np.array([1,2,3,4,5],dtype = np.float64)
print(y.itemsize)



import numpy as np

x = np.array([1,2,3,4,5,6])
print(x.flags)
