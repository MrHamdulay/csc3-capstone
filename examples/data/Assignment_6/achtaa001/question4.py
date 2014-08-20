#TAAHIRAH ACHMAT
#ACHTAA001

tay=(input("Enter a space-separated list of marks:\n")) #marks input by user 
done= tay.split(" ") 
a=0
b=0
c=0
d=0
e=0

for i in done: #restrictions , to sort out marks
    x = eval(i) 
    if 0<=x<50:
        a+=1 
    elif 50<=x<60:
        b+=1
    elif 60<=x<70:
        c+=1
    elif 70<=x<75:
        d+=1
    elif 75<=x<=100:
        e+=1

print("1 |", a * "X" ,sep="") # instructions to print in a specific order
print("2+|", d * "X",sep="")
print("2-|", c * "X",sep="")
print("3 |", b * "X",sep="")
print("F |", a * "X",sep="")