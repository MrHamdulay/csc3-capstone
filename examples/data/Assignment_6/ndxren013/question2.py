#Reneshan Naidoo
#Outputs basic vector functions

import math

x = []
x = input("Enter vector A:\n")
#reads a
    
x = x.split() 

a = []
a.append(eval(x[0]))
a.append(eval(x[1]))
a.append(eval(x[2]))
#evals a

y = []
y = input("Enter vector B:\n")
#reads b
    
y = y.split() 

b = []
b.append(eval(y[0]))
b.append(eval(y[1]))
b.append(eval(y[2]))
#evals b

#print(a[0], a[1], a[2])

c = [(a[0]+b[0]), (a[1]+b[1]), (a[2]+b[2])]
d = ((a[0]*b[0])+(a[1]*b[1])+(a[2]*b[2]))
e = math.sqrt((a[0]**2)+(a[1]**2)+(a[2]**2))
f = math.sqrt((b[0]**2)+(b[1]**2)+(b[2]**2))
#does math for each

print ("A+B =", c)
print ("A.B =", d)
print ("|A| =", "{0:.2f}".format(e))
print ("|B| =", "{0:.2f}".format(f))
#outputs accordingly
