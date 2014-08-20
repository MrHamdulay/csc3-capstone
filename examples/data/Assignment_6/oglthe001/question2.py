"""basic vector calculations
theresa ogallo 2014"""

import math
#getting the vectors
vectorA = [int(i) for i in (input("Enter vector A:\n")).split()]
vectorB= [int(j) for j in (input("Enter vector B:\n")).split()]

#addition of vectors
vectorC=[]
for m in range(len(vectorA)):
   answer=(vectorA[m]+vectorB[m])
   vectorC.append(answer)
print('A+B = ',end='')
print(vectorC)

#dot production of vectors
ans=0
for i in range(len(vectorA)):
   ans=ans+vectorA[i]*vectorB[i]
print('A.B = ',end='')
print(ans)

#norm of vectors
#norm of a single vector is the square root of the sum of the squares of the elements.
ans=0.00
for j in range(len(vectorA)):
   ans=ans+(vectorA[j]**2)
answer=math.sqrt(ans)
answer2='{:.2f}'.format(answer)
print('|A| = ',end='')
print(answer2)

ans2=0.00
for q in range(len(vectorB)):
   ans2=ans2+(vectorB[q]**2)
answer=math.sqrt(ans2)
answer2='{:.2f}'.format(answer)
print('|B| = ',end='')
print(answer2)