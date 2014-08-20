import math

a = input("Enter vector A:\n")
b = input("Enter vector B:\n")

vectora = a.split(" ")
vectorb = b.split(" ")
add = []
dot = 0
magA = 0
magB = 0
for i in range(3):
    add.append(eval(vectora[i])+eval(vectorb[i]))
    dot += eval(vectora[i])*eval(vectorb[i])
    magA += eval(vectora[i])**2
    magB +=eval(vectorb[i])**2

print("A+B =", add)
print("A.B =", dot)
if len(str(round(math.sqrt(magA),2)).split(".")[1])==1 :
    print("|A| =", str(round(math.sqrt(magA),2))+"0")
else:
    print("|A| =", round(math.sqrt(magA),2))

if len(str(round(math.sqrt(magB),2)).split(".")[1])==1:
    print("|B| =", str(round(math.sqrt(magA),2))+"0")
else:
    print("|B| =", round(math.sqrt(magB),2))


    
    
          
