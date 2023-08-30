import numpy as np
x = np.empty([3,2],dtype=int)
print(x)




import numpy as np

x = np.zeros(5)
print(x)

y = np.zeros((5,),dtype=int)
print(y)

z = np.zeros((2,2),dtype=[('x','i4'),('y','i4')])
print(z)




import numpy as np

x = np.ones(5)
print(x)

x = np.ones([2,2],dtype=int)
print(x)



import numpy as np
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
zeros_arr = np.zeros_like(arr)
print(zeros_arr)



import numpy as np
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
ones_arr = np.ones_like(arr)
print(ones_arr)
