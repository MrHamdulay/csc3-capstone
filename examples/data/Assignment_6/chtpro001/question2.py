lisA=[]
print("Enter vector A:")
a=input()
a=a.split()
j=len(a)
for i in range(j) :
    b=a[i]
    lisA.append(b)
    
    
lisB=[]
print("Enter vector B:")
a=input()
a=a.split()
j=len(a)
for i in range(j) :
    b=a[i]
    lisB.append(b)

# addition

lisC=lisA+lisB
ans=[]
for i in range(0,3):
    b=eval(lisC[i]) + eval(lisC[i+3])
    ans.append(b)
    
print("A+B","=",ans)

# dot product
anse=0
for i in range (0,3):
    b=eval(lisC[i]) * eval(lisC[i+3])
    anse+=b
    
print("A.B","=",anse)

# normalization
import math
ansA=0
ansB=0
for i in range (0,3):
    b=eval(lisA[i])
    c=b*b
    ansA+=c
    d=eval(lisB[i])
    e=d*d
    ansB+=e
ansa = math.sqrt(ansA)
ansb = math.sqrt(ansB)
ansa=round(ansa,2)
ansb=round(ansb,2)
ra="{0:.2f}".format(ansa)
rb="{0:.2f}".format(ansb)

print("|A|","=",ra)
print("|B|","=",rb)

    