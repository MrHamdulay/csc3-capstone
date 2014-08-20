fails=0
thrd=0
lsec=0
usec=0
first=0

mlist=(input("Enter a space-separated list of marks:\n").split())
mlist=list(map(int,mlist))

for i in range(len(mlist)):
    if mlist[i]<50:
        fails+=1
    elif mlist[i]<60:
        thrd+=1
    elif mlist[i]<70:
        lsec+=1
    elif mlist[i]<75:
        usec+=1
    else:
        first+=1
        
print("1 |","X"*first,"\n2+|","X"*usec,"\n2-|","X"*lsec,"\n3 |","X"*thrd,"\nF |","X"*fails,sep="")
