import numpy as np

H = 100

from module_of_physical_constants import pi

a = pi / 3
b = np.radians(30)

from module_of_physical_constants import g

V = (g * H * (np.tan(b) ** 2)) / (2 * (np.cos(a) **2) * (1 - (np.tan(b)) * (np.tan(a)))) ** 0.5
print(V)

T = 200
ę = 300

from module_of_physical_constants import k, e, h

N = (2 / (pi) ** 0.5) * (h / ((k*T) ** (3/2))) * (e ** (-ę / (k*T))) * (ę ** (T/2))
print(N)