print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):")
a=""
a=""
lis=[]
while a != "DONE" :
    a=str(input())
    lis.append(a)
lis.remove("DONE") 
lis.sort()
lisCa=[] 
lisVo=[]
for i in lis :
    if i not in lisCa :
        lisCa.append(i)
        b=lis.count(i)
        lisVo.append(b)  
print()

print("Vote counts:")        
j=len(lisCa)
for i in range(j):
    d=lisCa[i]
    e=lisVo[i]
    f = "{0:<10}".format(d)
    print(f,"-",e)
        