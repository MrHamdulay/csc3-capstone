# Vector Program
a = input("Enter vector A:\n")
b = input("Enter vector B:\n")
          
#import math
import math

#split input into lists
va = a.split(" ")
vb = b.split(" ")
#addition calculation
add = [int(va[0])+int(vb[0]),int(va[1])+ int(vb[1]),int(va[2])+ int(vb[2])]

#multiplication
multiply = (int(va[0])*int(vb[0]))+(int(va[1])* int(vb[1])) + (int(va[2])* int(vb[2]))

        
#normal calculation      
Na = round(math.sqrt(int(va[0])**2 + int(va[1])**2 + int(va[2])**2),2)
Nb = round(math.sqrt(int(vb[0])**2 + int(vb[1])**2 + int(vb[2])**2),2)



#Display
print('A+B =',add)
print('A.B =',multiply)

# control statements
if Na ==0.0:
    print("|A| =","0.00")
else:
    print("|A| =",Na)   
    
if Nb ==0.0:
    print("|B| =","0.00")
else:
    print("|B| =",Nb)