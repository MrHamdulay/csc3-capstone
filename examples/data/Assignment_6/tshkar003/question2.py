#TSHKAR003

import math

vector_a = input("Enter vector A:\n")
vector_b = input("Enter vector B:\n")
a = vector_a.split(" ")
b = vector_b.split(" ")
a0,a1,a2,b0,b1,b2 = a[0],a[1],a[2],b[0],b[1],b[2]
c,d,e,f,g,h = int(a0),int(a1),int(a2),int(b0),int(b1),int(b2)
add = [c+f,d+g,e+h]
multi = (c*f)+(d*g)+(e*h)
sq_a = math.sqrt((c**2)+(d**2)+(e**2))
sq_a = round(sq_a,2)
sq_b = math.sqrt((f**2)+(g**2)+(h**2))
sq_b = round(sq_b,2)
print("A+B = ",add)
print("A.B = ",multi)
print("|A| = ",sq_a)
print("|B| = ",sq_b)