import numpy as np

a = np.zeros((2, 3)) # 2 строки и 3 нуля
print(a) 

a[0,2] = 5
print(a)

b = np.ones((3, 2))
print(b)

d = np.ndarray((3, 3))
print(type(a))
print(type(b))
print(type(d))