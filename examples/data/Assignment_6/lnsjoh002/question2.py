""""Program to do basic vector caluclations
JP Lanser
20 April 2014"""

import math



#Create a function to do the addition
#Input fron the user will be split into a list when entered by user, so parameters are lists

def add(a,b):
    count = 0  
    new_vector = []    #Create empty list
    #loop through both lists and add corresponding numbers. i.e add first number of first list to first number of second list and so on
    for i in a :
        x = eval(i)     
        y = eval(b[count]) 
        new_vector.append(x+y)  #add this new number to the list
        count+=1  
    return new_vector


#Create function to do the dot product of two lists, using similar method as above function
def dot_product(a,b):
    count = 0
    value = 0   #Set initial value of dot product to zero then add to it
    for i in a :
        x = eval(i)
        y = eval(b[count])
        value+= (x*y) 
        count+=1
    return value

#Create funtion to do the norm, again loop through both lists 
def norm(a):
    Norm = 0  #Set initial  norm value to zero and then add to it
    for i in a:
        x = eval(i)
        x = x**2
        Norm += x
    Norm = math.sqrt(Norm)
    return Norm


if __name__=="__main__":
    
    #Prompt user for the two vectors and then do the required calculations using the functions created above
    #Print as required per sample I/O
    
    vector_A = input("Enter vector A:\n").split(" ")
    
    vector_B = input("Enter vector B:\n").split(" ")    
    
    addition = add(vector_A, vector_B)
    print("A+B =", addition)
    
    dot_product = dot_product(vector_A,vector_B)
    
    print("A.B =", dot_product)
    
    norm_A = norm(vector_A)
    norm_B = norm(vector_B)
    norm_A = "{0:4.2f}".format(norm_A) #format to two decimal places 
    norm_B = "{0:4.2f}".format(norm_B)
    
    
    print("|A| =",norm_A)
    print("|B| =",norm_B)
    
    


    


        
    
    


        
        

        
        
        
