import numpy as np
a = np.array([1,2,3,4])
b = np.array([10,20,30,40])
c = a*b
print(c)




import numpy as np 
a = np.array([[ 0, 0, 0],
           [10,10,10],
           [20,20,20],
           [30,30,30]])
b = np.array([0,1,2])
print(a+b)



import numpy as np 
a = np.array([[ 0, 0, 0],
           [10,10,10],
           [20,20,20],
           [30,30,30]])
b = np.array([1,2,3])
bb=np.tile(b,(4,1))
print(a+bb)
