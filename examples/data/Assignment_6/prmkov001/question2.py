#Kovlin Perumal
#21/04/14
#Question2 - Vector Calculator

from math import *

vectsa = input("Enter vector A:\n").split() #recieve vectors

vectsb = input("Enter vector B:\n").split()  

vectsa = list(map(int, vectsa))#mutate them into integers
vectsb = list(map(int, vectsb))

print("A+B = [",vectsa[0] + vectsb[0],", ",vectsa[1] + vectsb[1],", ", vectsa[2] + vectsb[2],"]" ,sep = '')#add

vectprod = 0

for i in range(len(vectsa)) :
    vectprod += vectsa[i] * vectsb[i] #Sum the products of the vectors

    
print("A.B =",vectprod)

vectasquare = 0
vectbsquare = 0

for i in range(len(vectsa)) :
    vectasquare += vectsa[i]**2 #Square and sum each vector
    vectbsquare += vectsb[i]**2
    
print("|A| =",'{0:.2f}'.format(round(sqrt(vectasquare),2)))#Output Results
      
print("|B| =",'{0:.2f}'.format(round(sqrt(vectbsquare),2)))

