import numpy as np
x = [1,2,3]
a = np.asarray(x)
print(a)



import numpy as np
x = (1,2,3)
a = np.asarray(x)
print(a)



import numpy as np
x = [(1,2,3),(4,5)]
a = np.asarray(x)
print(a)



import numpy as np
x = [1,2,3]
a = np.asarray(x,dtype=float)
print(a)



import numpy as np
s = b'Hello World'
a = np.frombuffer(s,dtype='S1')
print(a)



import numpy as np
list = range(5)
it = iter(list)
x = np.fromiter(it,dtype=float)
print(x)
