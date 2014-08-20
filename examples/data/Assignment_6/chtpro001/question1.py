print("Enter strings (end with DONE):")
a=""
lis=[]
while a != "DONE" :
    a=str(input())
    lis.append(a)
    
j=len(lis) 
leng_lis=[]
for i in range(j):
    b=lis[i]
    leng=len(b)
    leng_lis.append(leng)
print()
    
print("Right-aligned list:")
max_leng=max(leng_lis)
x=max_leng
for i in range(j-1):
    r=lis[i]
    z=len(r)
    print(" "*(x-z),r,sep="")