'''Histogram of Marks
Limpho Parkies
24-04-2014'''

F=0
three=0
twom=0
twop=0
one=0

A=input('Enter a space-separated list of marks:\n').split(" ")
for a in A:
    if int(a)<50:
        F += 1
    elif int(a)<60:
        three += 1
    elif int(a)<70:
        twom += 1
    elif int(a)<75:
        twop += 1
    elif int(a)>=75:
        one+=1
        

print("1 |", "X"*one, sep = "")
print("2+|", "X"*twop, sep = "")
print("2-|", "X"*twom, sep = "")
print("3 |", "X"*three, sep = "")
print("F |", "X"*F, sep = "")