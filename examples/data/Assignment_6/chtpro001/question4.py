print("Enter a space-separated list of marks:")
lisA=[]
a=input()
a=a.split()
for i in a:
        lisA.append(i)
lisA.sort()

lisGr=[]

for i in lisA:
        
        b=int(i)
        if b<50:
                i="F"
        elif b<60:
                i="3"
        elif b<70:
                i="2-"
        elif b<75:
                i="2+"
        else:
                i="1"
        lisGr.append(i)
        
lisFr=[] 
XX=["1","2+","2-","3","F"]
for j in range(5) :
        v=XX[j]
        u=lisGr.count(v)
        lisFr.append(u)
    

for i in range(5):
        z=XX[i]
        zz ="{0:<2}".format(z)
        y=lisFr[i]
        print(zz,"|","X"*y,sep="")