from math import sqrt
A = input('Enter vector A:\n').split(' ')
B = input('Enter vector B:\n').split(' ')
l = len(A)
C = []
D = 0
E = 0
F = 0
for i in range(l):
    C.append((int(B[i])+int(A[i])))
    D += int(B[i])*int(A[i])
    E += int(A[i])**2
    F += int(B[i])**2
print('A+B = {}\nA.B = {}\n|A| = {:.2f}\n|B| = {:.2f}'.format(C,D,sqrt(E),sqrt(F)))
    
