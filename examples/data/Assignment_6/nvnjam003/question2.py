#James Nevin
#Assignment 6, Question 2
#23/04/2014
import math

vecA = input("Enter vector A:\n").split()
vecB = input("Enter vector B:\n").split() #Getting strings, turning to lists
calc = []
productSum = 0
for x in range (0, 3):
    vecA[x] = int (vecA[x])
    vecB[x] = int (vecB[x]) #Converting to ints
    calc.append (str(vecA[x]+vecB[x])) #Adding sum to new list
print ("A+B = [" + calc[0] + ", " + calc[1] + ", " + calc[2] + "]") #Printing new list

for x in range (0, 3):
    productSum += int(vecA[x])*int(vecB[x]) #Calculating product and adding
print ("A.B = " + str(productSum)) #Printing dot product

squareSum = 0
for x in range (0, 3):
    squareSum += int(vecA[x]**2) #Squaring and adding to total
print ("|A| = " + str("{:.2f}".format(squareSum**(1/2)))) #Printing results

squareSum = 0 #Same as above
for x in range (0, 3):
    squareSum += int(vecB[x]**2)
print ("|B| = " + str("{:.2f}".format(squareSum**(1/2))))