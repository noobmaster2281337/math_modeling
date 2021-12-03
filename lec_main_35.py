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
c1 = 1
c2 = 2
c3 = 3
c4 = 4
for i in range(N):
  NxM[i][c1], NxM[i][c2] = NxM[i][c2], NxM[i][c1]
  NxM[i][c3], NxM[i][c4] = NxM[i][c4], NxM[i][c3]
print(NxM)