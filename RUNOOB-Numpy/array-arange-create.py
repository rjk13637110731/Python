import numpy as np
x = np.arange(5)
print(x)



import numpy as np
x = np.arange(5,dtype=float)
print(x)



import numpy as np
x = np.arange(10,20,2,dtype=float)
print(x)



import numpy as np
x = np.linspace(1,10,10)
print(x)



import numpy as np
x = np.linspace(1,1,10)
print(x)



import numpy as np
x = np.linspace(1,10,10,retstep=True)
print(x)
y = np.linspace(1,10,10).reshape([10,1])
print(y)



import numpy as np
x = np.logspace(1.0,2.0,num=10)
print(x)




import numpy as np
x = np.logspace(0,9,10,base=2)
print(x)
