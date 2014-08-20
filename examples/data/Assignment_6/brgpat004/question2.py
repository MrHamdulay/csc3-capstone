'''Q1 of Assignment 6: Vector Calculations
Patrick Boroughs
21 April 2014'''

#input values, seperate into array split by space
vectorA=input("Enter vector A:\n").split(" ")
vectorB=input("Enter vector B:\n").split(" ")

#new arrays with evaluated numerical values
evalA=[eval(vectorA[0]),eval(vectorA[1]),eval(vectorA[2])]
evalB=[eval(vectorB[0]),eval(vectorB[1]),eval(vectorB[2])]

#Calculating sum, dot product, and magnitudes using above 2 arrays
sumAB=[evalA[0]+evalB[0],evalA[1]+evalB[1],evalA[2]+evalB[2]]
dotAB=evalA[0]*evalB[0]+evalA[1]*evalB[1]+evalA[2]*evalB[2]
magA=round(((evalA[0]**2)+(evalA[1]**2)+(evalA[2]**2))**(1/2),2)
magB=round(((evalB[0]**2)+(evalB[1]**2)+(evalB[2]**2))**(1/2),2)

#Printing calculations
print("A+B =",sumAB)
print("A.B =",dotAB)

#Ensuring 2 decimal places if magnitude is 0
if magA==0:
    print("|A| = 0.00")
else:
    print("|A| =",magA)
    
if magB==0:
    print("|B| = 0.00")
else:
    print("|B| =",magB)