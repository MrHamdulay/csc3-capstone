#Assignment 6, Question 2
#Author: Muhammad Sabir Buxsoo (BXSMUH001)
#Class: CSC1015F 2014
#Date Created: 21/04/2014

#This program is designed to do basic 3-D vector calulations; addition, dot product and normalization.
#Pre-condition: Input vectors A and B.
#Post-condition: Output results of vector operations.
from math import * #Importing math library to make use of sqrt() function.

#Defining function vectorCalculation() which will compute addition, dot product and normalization, using specified parameters.
#.#Pre-condition: Grab parameters from inputs and compute accordingly.
#.#Post-condition: Output computer result.
def vectorCalculation(vectorA, vectorB, sign):
    #SPlitting vectors A and B to a list, stripping out all the space.
    vectorA = vectorA.split()
    vectorB = vectorB.split()
    
    #Conditions for the calculations to be executed:
    #.# Length of the two vectors should be the same.
    #.# Length of the vector should be exactly 3.
    #.# The sign used should be either '+', '*' or '**'.
    if((len(vectorA) == len(vectorB)) and (len(vectorA) == 3) and (sign == "*" or sign == "+" or sign == "**")):
        #Computing vector addition or dot product, depending on the sign.
        if(sign == "+" or sign == "*"):
            for i in range(len(vectorA)):
                if(i == 0):
                    ab1 = eval(vectorA[i] + sign + vectorB[i]) #Evaluating the arithmetic string to convert it to a number.
                elif(i == 1):
                    ab2 = eval(vectorA[i] + sign + vectorB[i])
                else:
                    ab3 = eval(vectorA[i] + sign + vectorB[i]) 
            if(sign == "+"):
                answer = ("A+B = [" + str(ab1) + ", " + str(ab2) + ", " + str(ab3) + "]") #Answer is converted back to a string, making it easier to print.
                
            if(sign == "*"):
                AdotB = ab1 + ab2 + ab3
                answer = ("A.B = " + str(AdotB)) #Answer is converted back to a string, making it easier to print.
        
        #Computing vector normalization.
        elif(sign == "**"):
            #Converting each element of the vector lists to integers(numbers).
            for j in range(len(vectorA)):
                if(j == 0):
                    A1 = abs(eval(vectorA[j] + sign + "2")) #Evaluating the arithmetic string to convert it to a number. abs() is used to make square of negative number become positive.
                    B1 = abs(eval(vectorB[j] + sign + "2"))
                elif(j == 1):
                    A2 = abs(eval(vectorA[j] + sign + "2"))
                    B2 = abs(eval(vectorB[j] + sign + "2"))
                else:
                    A3 = abs(eval(vectorA[j] + sign + "2"))
                    B3 = abs(eval(vectorB[j] + sign + "2"))
    
            modA = str("{0:.2f}".format(sqrt(A1+A2+A3))) #Formatting the calculated normalized value to 2d.p and converting it to a string.
            modB = str("{0:.2f}".format(sqrt(B1+B2+B3)))
            
            answer = "|A| = " +  modA + "\n" + "|B| = " + modB
        
        #Output result.    
        print(answer)
        

#Checking if program is run as a standalone. If TRUE, execute body, else, use of definitions and statements above only.
if(__name__ == '__main__'):
    #Input vector A and vector B
    vectorA = input("Enter vector A:\n")
    vectorB = input("Enter vector B:\n")
    
    #Calculating and printing results.
    vectorCalculation(vectorA, vectorB, "+") #Addition
    vectorCalculation(vectorA, vectorB, "*") #Dot Product
    vectorCalculation(vectorA, vectorB, "**") #Normalization