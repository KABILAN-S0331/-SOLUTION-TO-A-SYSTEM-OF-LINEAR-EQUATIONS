#Program to find the solution for the given linear equations.
#Developed by: Kabilan S
#RegisterNumber: 212225230119

import numpy as np

A=np.array([[5,-3,-10],[2,2,-3],[-3,-1,5]])
b=np.array([-9,4,-1])
print(np.linalg.solve(A,b))
