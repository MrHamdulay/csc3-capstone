"""basic vector calculations in 3 dimensions: addition, dot product and normalization.
Kmaogelo Mphela
20 April 2014"""

import math
# get vectors A and B from the user
A = input("Enter vector A:\n")
B = input("Enter vector B:\n")
vA = A.split()
vB = B.split()

# convert strings in the lists to numbers
vectorB=[]
vectorA=[]
for i in vA:
    i = eval(i)
    vectorA.append(i)
for i in vB:
    i = eval(i)
    vectorB.append(i)

#add vecters A and B
add = []
for i in range(3):
    for n in vectorB:
        x = vectorA[i] + vectorB[i]
        add.append(x)
        break

#dot product
product = []
for i in range(3):
    for n in vectorB:
        x = vectorA[i] * vectorB[i]
        product.append(x)
        break
dot_product =product[0] +product[1] + product[2]


# normalization
norm = 0
for i in vectorA:
    norm += i**2
normA = round(math.sqrt(norm),2)


x = 0
for i in vectorB:
    x += i**2
normB = round(math.sqrt(x),2)


# output calculations

print("A+B =",add)
print("A.B =", dot_product)
if normA ==0.0:
    print("|A| =",'0.00')
else:
    print("|A| =", normA)
if normB==0.0:
    print("|B| =","0.00")
else:
    print("|B| =", normB)