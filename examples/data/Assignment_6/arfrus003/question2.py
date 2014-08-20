import math #makes functions defined in math library available

A_lst = input("Enter vector A:\n") #prompt for vector A
A = A_lst.split()

B_lst = input("Enter vector B:\n") #prompt for vector B
B = B_lst.split()

#list of all operations

s0 = (int(A_lst[0]) + int(B_lst[0]))
s1 = (int(A_lst[2]) + int(B_lst[2]))
s2 = (int(A_lst[4]) + int(B_lst[4]))

print("A+B = [",s0,", ",s1,", ",s2,"]", sep="") #output list of A+B


m0 = (int(A_lst[0]))*(int(B_lst[0]))
m1 = (int(A_lst[2]))*(int(B_lst[2]))
m2 = (int(A_lst[4]))*(int(B_lst[4]))
m3 = m0 + m1 + m2

print("A.B =", m3) #output list of A*B


mA0 = int(A_lst[0])**2
mA1 = int(A_lst[2])**2
mA2 = int(A_lst[4])**2
sumA = math.sqrt(mA0 + mA1 + mA2)

print("|A| =","{0:.2f}".format(sumA)) #output list of sqrtA
            

mB0 = int(B_lst[0])**2
mB1 = int(B_lst[2])**2
mB2 = int(B_lst[4])**2
sumB = math.sqrt(mB0 + mB1 + mB2)

print("|B| =","{0:.2f}".format(sumB)) #output list of sqrtB