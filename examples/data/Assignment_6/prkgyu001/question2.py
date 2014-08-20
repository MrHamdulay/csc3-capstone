import math

dataA = input("Enter vector A: \n")
dataB = input("Enter vector B: \n")
new_A = dataA.split(" ")
new_B = dataB.split(" ")

grid_A = []
grid_B = []
for i in new_A:
    grid_A.append(int(i))
for i in new_B:
    grid_B.append(int(i))

#addition
added_grid = []
for i in range(3):
    added_grid.append(grid_A[i]+grid_B[i]) 
print ("A+B =",added_grid)


#dot product
final = 0
for i in range(3):
    final = final + (grid_A[i]*grid_B[i])
print("A.B =",final)


#normalization
lAl = math.sqrt(grid_A[0]**2 + grid_A[1]**2 + grid_A[2]**2)
lBl = math.sqrt(grid_B[0]**2 + grid_B[1]**2 + grid_B[2]**2)
print("|A| =", round(lAl,2))
print("|B| =", round(lBl,2))
