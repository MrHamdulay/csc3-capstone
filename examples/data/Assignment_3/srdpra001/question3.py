'''
Prashanth Sridharan
SRDPRA001
Assignment 3
Question 04
'''

msg = input("Enter the message:\n")
rpt = eval(input("Enter the message repeat count:\n"))
tks = eval(input("Enter the frame thickness:\n"))

i=1
nds=len(msg)+(2*tks)
dh="-"*nds
br=("+"+dh+"+")
sp=1
fl=""
while(i<=tks):    
    print(br)
    fl=br+"\n"+fl
    nds-=2
    dh="-"*nds
    br=("|"*sp+"+"+dh+"+"+"|"*sp)
    i+=1
    sp+=1
t=1
while(t<=rpt):
    print(("|"*tks)+" "+msg+" "+("|"*tks))
    t+=1
i=1
print(fl)