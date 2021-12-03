import numpy as np
l = np.zeros((2, 3))
o = np.zeros((2, 3))
g = np.zeros((2, 3))
for i in range(0, 2):
  for c in range(0, 2):
    l[i, c] = int(input())
print(l)
for i in range(0, 2):
  for c in range(0, 2):
    o[i, c] = int(input())
print(o)
for i in range(0, 2):
  for c in range(0, 2):
    if l[i, c] > o[i, c]:
      g[i, c] = l[i, c]
    else:
      g[i, c] = o[i, c]
print(g)