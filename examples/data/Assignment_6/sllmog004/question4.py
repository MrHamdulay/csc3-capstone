marks=input("Enter a space-separated list of marks:\n").split(" ")
a=""
b=""
c=""
d=""
e=""
for i in range(len(marks)):
   
    if (int(marks[i])<50):
        a+="X"
    if (50<=int(marks[i])<60):
        b+="X"
    if (60<=int(marks[i])<70):
        c+="X"
    if (70<=int(marks[i])<75):
        d+="X"
    if (int(marks[i])>=75):
        e+="X"
print("1 |"+e)
print("2+|"+d)
print("2-|"+c)
print("3 |"+b)
print("F |"+a)