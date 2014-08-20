"""histrogram represantation of marks
Tafadzwa Moyo
21 April 2014"""

#Get list of marks
marks=input("Enter a space-separated list of marks:\n").split(" ")


#List of variables
fst=0
sdup=0
sddwn=0
thrd=0
f=0

#Draws graph
for i in marks:
    i=int(i)
    if i>=75:
        fst+=1
    elif i>=70:
        sdup+=1
    elif i>=60:
        sddwn+=1
    elif i>=50:
        thrd+=1
    else:
        f+=1
        
print("1 ","|", "X"*fst, sep="")
print("2+","|", "X"*sdup, sep="")
print("2-","|", "X"*sddwn, sep="")
print("3 ","|", "X"*thrd, sep="")
print("F ","|", "X"*f, sep="")