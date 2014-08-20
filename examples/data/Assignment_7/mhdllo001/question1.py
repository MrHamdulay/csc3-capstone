print("Enter strings (end with DONE):")
x=[]
a=""
c=0
while(c==0):
   
    a=input()
    if(a=="DONE"):
        c=1    
    x.append(a)
x.remove("DONE")
count=0
now=[]
k=0
while(k<len(x)):
    if(x.index(x[k])==k):
        now.append(x[k])
    k=k+1

print()
print("Unique list:")
for i in range(len(now)):
    print(now[i])