import numpy as np
x = np.array([[1,2],[3,4],[5,6]])
y = x[[0,1,2],[0,1,0]]
print(y)



import numpy as np
x = np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])
print("我们的数组是：")
print(x)
print('\n')
rows=np.array([[0,0],[3,3]])
cols=np.array([[0,2],[0,2]])
y = x[rows,cols]
print("这个数组的四个角元素是：")
print(y)
print(rows)
print(cols)



import numpy as np
x = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = a[1:3,1:3]
c = a[1:3,[1,2]]
d = a[...,1:]
print(b)
print(c)
print(d)



import numpy as np 
x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]]) 
print(x)
print(x[x>5])



import numpy as np
a = np.array([np.nan,1,2,np.nan,3,4,5])
print(a[~np.isnan(a)])



import numpy as np
a = np.array([1,2+6j,5,3.5+5j])
print(a[np.iscomplex(a)])import numpy as np
x = np.arange(9)
print(x)
x2 = x[[0,6]]
print(x2)
print(x2[0])
print(x2[1])



import numpy as np
x = np.arange(32).reshape((8,4))
print(x)
print(x[[4,2,1,7]])
print (x[[-4,-2,-1,-7]])



import numpy as np
x = np.arange(32).reshape((8,4))
print(x[np.ix_([1,5,7,2],[0,3,1,2])])
