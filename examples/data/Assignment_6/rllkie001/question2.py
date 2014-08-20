#Kieran Reilly, RLLKIE001
#Vector Calculations
#Assignment 6, question 2
#21/04/14


import math

def vector_add(vectorA, vectorB):
    """adds two vectors"""
    vectorA = vectorA
    vectorB = vectorB
    vectorC = []        #empty vector
    vectorAdd = 0       #variable used in trasnfering added vectors to C
    
    #adds the two vectors into vectorC
    for i in range(3):
        vectorAdd = vectorA[i] + vectorB[i] #adding vectors
        vectorC.append(vectorAdd)   #putting the values into C
     
    print("A+B = "+str(vectorC))          
    
def vector_dotProduction(vectorA, vectorB):
    """dot production of two vectors"""
    vectorA = vectorA
    vectorB = vectorB
    vectorC = []        #empty vector
    dotProduct = 0      #variable used in dot production of vectors 
    
    #fills vectorC
    for i in range(3):
        vectorC.append(vectorA[i-1]*vectorB[i-1]) #multiplication of vectors and appending
    
    for i in range(3):
        dotProduct = dotProduct + vectorC[i] #creates the final dot production
    print("A.B = " + str(dotProduct))
    
     
def vectorA_norm(vectorA):
    """prints the norm of vectorA"""
    vectorA = vectorA 
    squares = []        #squares list to hold squared values of vectorA  
    sumSquares = 0      #sumSquares holds sum of squares inside squares list  
    norm = 0.00         #final norm variable
    out = "{0:0.2f}"    #formatt string
    
    #populates squares list with the squares of vectorA
    for i in range(3):
        squares.append(vectorA[i]**2)
        
    #adds and assigns the sum of squares to sumSquares
    for i in range(3):
        sumSquares = sumSquares + squares[i]
    
    #final norm used to hold the norm
    norm = math.sqrt(sumSquares)
    print("|A| = " + out.format(norm))
    
    
def vectorB_norm(vectorB):
    """prints the norm of vectorB"""
    #same as vectorA_norm, just for vectorB
    vectorB = vectorB
    squares = []        
    sumSquares = 0
    norm = 0.00
    out = "{0:0.2f}"
    
    for i in range(3):
        squares.append(vectorB[i]**2)
        
    for i in range(3):
        sumSquares = sumSquares + squares[i]
    
    norm = math.sqrt(sumSquares)
    print("|B| = " + out.format(norm))
    
    
if __name__ == "__main__":
    
    #empty vectors
    vectorA = []
    vectorB = []
    
    vectorIn = input("Enter vector A:\n")
    vectorA = vectorIn.split(" ")   #splits user's string into list
    
    #sorts whether the user entered a float or int, into vectorA
    for i in range(3):
        if len(vectorA[i]) > 1:
            vectorA[i] = float(vectorA[i])
        else:
            vectorA[i] = int(vectorA[i])
    
    vectorIn = input("Enter vector B:\n")
    vectorB = vectorIn.split(" ")
                
    #sorts whether the user entered a float or int, into vectorB
    for i in range(3):
        if len(vectorB[i]) > 1:
            vectorB[i] = float(vectorB[i])
        else:
            vectorB[i] = int(vectorB[i])
            
    #functions called
    vector_add(vectorA, vectorB)
    vector_dotProduction(vectorA, vectorB)    
    vectorA_norm(vectorA)
    vectorB_norm(vectorB)