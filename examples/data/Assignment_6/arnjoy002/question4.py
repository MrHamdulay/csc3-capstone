#Joy Arendse-Gorvalla
m=input("Enter a space-separated list of marks:\n") #asking for input
L=m.split() #seperating strings
L=map(int,L) #converts to integers

fail, third, lower2nd, upper2nd, first = 0,0,0,0,0 #setting counts to 0

for m in L: #creating loop
   
    if 0<=m<50: #creating conditions
        fail = fail + 1
    elif 50<=m<60:
        third += 1
    elif 60<=m<70:
        lower2nd += 1
    elif 70<=m<75:
        upper2nd +=1
    elif 75<=m<=100:
        first = first + 1
    else:
        None

print("1 |", "X"*first, sep="")    #creating histogram
print("2+|", "X"*upper2nd, sep="")
print("2-|", "X"*lower2nd, sep="")
print("3 |", "X"*third, sep="")
print("F |", "X"*fail, sep="")