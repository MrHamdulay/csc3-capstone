a=input("Enter a space-separated list of marks:\n")
marks=a.split()
b=0
c=0
d=0
e=0
f=0
for n in marks:
    if int(n) <= 49:
        b=b+1
    elif 50<=int(n)<60:
        c=c+1
    elif 60<=int(n)<70:
        d=d+1
    elif 70<=int(n)<=74:
        e=e+1
    elif 75<=int(n)<=100:
        f=f+1
print("1 ",f*"X",sep="|")
print("2+",e*"X",sep="|")
print("2-",d*"X",sep="|")
print("3 ",c*"X",sep="|")
print("F ",b*"X",sep="|")





