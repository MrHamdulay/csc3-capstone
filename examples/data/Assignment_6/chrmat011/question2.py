import math

a = input('Enter vector A:\n').split(' ')

a[0]=int(a[0])
a[1]=int(a[1])
a[2]=int(a[2])

b = input('Enter vector B:\n').split(' ')

b[0]=int(b[0])
b[1]=int(b[1])
b[2]=int(b[2])

print('A+B = ['+str(a[0]+b[0])+', '+str(a[1]+b[1])+', '+str(a[2]+b[2])+']')
print('A.B = '+str((a[0]*b[0]) + (a[1]*b[1]) + (a[2]*b[2])))
normA = str(round(math.sqrt(a[0]**2 + a[1]**2 + a[2]**2),2))
while len(normA.split('.')[1]) < 2:
    normA+='0'
normB = str(round(math.sqrt(b[0]**2 + b[1]**2 + b[2]**2),2))
while len(normB.split('.')[1]) < 2:
    normB+='0'
print('|A| = '+str(normA))
print('|B| = '+str(normB))


