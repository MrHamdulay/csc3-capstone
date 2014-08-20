"""Assignment 6: Question 4- histogram
Duncan Saffy
20 April 2014"""
x=input("Enter a space-separated list of marks:\n")
y=x.split(" ")
f=0
one=0
twoP=0
twoM=0
three=0
for i in range(len(y)):
    if eval(y[i])>=75:
        one+=1
    elif eval(y[i])>=70:
        twoP+=1
    elif eval(y[i])>=60:
        twoM+=1
    elif eval(y[i])>=50:
        three+=1
    else:
        f+=1
        
print("1 |","X"*one,sep="")
print("2+|","X"*twoP,sep="")
print("2-|","X"*twoM,sep="")
print("3 |","X"*three,sep="")
print("F |","X"*f,sep="")

