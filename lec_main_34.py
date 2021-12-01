import numpy as np
N = 6
M = 5
NxM = np.zeros((N,M))
for i in range(N):
  for j in range(M):
    if i == 0 and j == 0:
      NxM[i,j] = np.sin(N * (i+1) + M * (j + 1))
    else:
      NxM[i,j] = np.sin(N * i + M * j)
    if NxM[i,j]<0: 
      NxM[i,j] = 0
print(NxM)