import math

a=input("Enter vector A:\n")
b=input("Enter vector B:\n")
A=a.split(" ")
B=b.split(" ")
addition=[]
x=0
for c in A:
    y=eval(c)
    z=eval(B[x])
    answer=y+z
    addition.append(answer)
    x+=1
print("A+B = " + str(addition))

x=0
v=0
for c in A:
    y=eval(c)
    z=eval(B[x])
    answer=y*z
    v+=answer
    x+=1

print("A.B = " + str(v))

x=0
v=0
for c in A:
    y=eval(c)
    answer=y**2
    v+=answer
    x+=1
print_answer=round(math.sqrt(v),2)

print("|A| = " + str(print_answer))

x=0
v=0
for c in B:
    y=eval(c)
    answer=y**2
    v+=answer
    x+=1
print_answer=round(math.sqrt(v),2)

print("|B| = " + str(print_answer))