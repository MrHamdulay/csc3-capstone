print("Enter strings (end with DONE):")
a=""
lis=[]
while a != "DONE" :
    a=str(input())
    lis.append(a)
    
lis.remove("DONE")
    
j=len(lis) 
leng_lis=[]
for i in range(j):
    b=lis[i]
    if b not in leng_lis:
        leng_lis.append(b)
print()

print("Unique list:")

k=len(leng_lis)
for j in range(k):
    print(leng_lis[j])
