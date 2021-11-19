import numpy as np

a = [1, 5, 3, 6]

slice = a[0:2:1] # вместо слайс можно что угодно написать, главное двоеточие
print(slice)

slice = a[3:0:-1]
print(slice)

slice = a[::-1]
print(slice)

b = np.array([a, np.array(a)*3])
print(b)

slice = b[::, 1]# берем все из строки 1 столбца, это команда - срез столбцов
print(slice)

slice = b[1,2:3:1]
print(slice)