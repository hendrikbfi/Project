from pulp import *
import numpy as np
Box=6
Pallet=6
Variable_range=Box*Pallet
x = {}

from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable
# Define the model
model = LpProblem(name="Container Loading", sense=LpMaximize)

# Define the decision variables

#Decision variables X
for i in range(1, Box+1):
    for j in range (1,Pallet+1):
      x[(i,j)] = pulp.LpVariable('x' + str(i) + '_' + str(j), 0, 1, LpBinary)

# Add constraints

#constraint for restricting unique number of boxes based on orientation
for i in range (1, (Box//2)+1):
     for j in range (1,Pallet+1):
       model += x[(i*2-1,j)] + x[(i*2,j)] <= 1 

#print (model)
#Set the objective
model += lpSum(x.values())

# Solve the optimization problem
status = model.solve()
Soln= np.zeros((Box,Pallet))
print (Soln[5][5])
for i in range (1,Box+1):
  for j in range (1, Pallet+1):
    value=x[(i,j)].value()
    Soln[i-1][j-1]=value