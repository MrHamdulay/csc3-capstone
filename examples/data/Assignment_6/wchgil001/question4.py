# A program that takes in a list of marks and output a histogram representation of the marks.
#gillian wachira
#26th april 2014


y=input("Enter a space-separated list of marks:\n")
marks=y.split()
a=0
b=0
c=0
d=0
f=0
for i in marks:
    if eval(i)<50:
        f+=1 
    elif 50<=eval(i)<60:
        d+=1
    elif 60<=eval(i)<70:
        c+=1
    elif 70<=eval(i)<75:
        b+=1
    elif eval(i)>=75:
        a+=1
        
print("1 |"+"X"*a)
print("2+|"+"X"*b)
print("2-|"+"X"*c)
print("3 |"+"X"*d)
print("F |"+"X"*f)
 