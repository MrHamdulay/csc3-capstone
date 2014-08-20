import math
vectorA=(input("Enter vector A:\n"))
vectorB=(input("Enter vector B:\n"))

array1=vectorA.split(" ")
array2=vectorB.split(" ")

for i in range (3):
    array1[i]=eval(array1[i])
    array2[i]=eval(array2[i])
    


print("A+B = [",array1[0]+array2[0],", ",array1[1]+array2[1],", ",array1[2]+array2[2],"]",sep="")
print("A.B =",(array1[0]*array2[0])+(array1[1]*array2[1])+(array1[2]*array2[2]))
print("|A| = %.2f"%(math.sqrt(array1[0]**2+array1[1]**2+array1[2]**2)))
print("|B| = %.2f"%(math.sqrt(array2[0]**2+array2[1]**2+array2[2]**2)))



