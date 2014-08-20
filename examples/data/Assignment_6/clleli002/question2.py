"""basic vector calculations in 3 dimensions
Elizabeth Cilliers
20/04/2014"""

def vcalc():
    InputVectorA = input ("Enter vector A:\n")
    vectorA = InputVectorA.split (" ")
    

    InputVectorB = input ("Enter vector B:\n")
    vectorB = InputVectorB.split (" ")
    
    
#Addition
    answer=[]
    for i in range(len(vectorA)):
        elemA= eval(vectorA[i])
        elemB= eval(vectorB[i])
        add=elemA+elemB #add elements in vectors
        answer.append (add) #add answer to the list
    print("A+B =", answer)

#DotProduct
    count=0
    for i in range(len(vectorA)):
        elemA= eval(vectorA[i]) 
        elemB= eval(vectorB[i])
        answer=elemA*elemB #multiply the value of each corresponding element together
        count= count+answer #add this to count
    print("A.B =", count)    


#Norm    
    count=0
    for i in range(len(vectorA)):
        elemA= eval(vectorA[i])
        elemAsqr=elemA**2 #square element
        count=count+elemAsqr #add this count
    answer=count**0.5 #squareroot total of count 
    f_answer='{0:0.2f}'.format(answer) #put it to 2 decima places
    print("|A| =",f_answer)
    
    count=0
    for i in range(len(vectorB)):
        elemB= eval(vectorB[i])
        elemBsqr=elemB**2
        count=count+elemBsqr
    answer=count**0.5
    f_answer= '{0:0.2f}'.format(answer)
    print("|B| =",f_answer)    
        

vcalc()