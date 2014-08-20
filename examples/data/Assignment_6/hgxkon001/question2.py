#Konrad Hugo question 2
#25 April 2014

'''Inputs for user'''
vectorA = input("Enter vector A:\n")
vectorB = input("Enter vector B:\n")
listA = vectorA.split(" ")
listB = vectorB.split(" ")


import math

#This function adds values from lists A and B
def add_function(vectorA,vectorB):
    adding_list = []
    for i in range(3): #3 piece vectors
        add = eval(vectorA[i]) + eval(vectorB[i])
        adding_list.append(add)
    print("A+B =",adding_list)

#Function that first multiplies units in the lists, then adds the products and displays
def product_func(vectorA,vectorB):
    summed = 0
    for i in range(3): #3 part vectors
        prod = eval(vectorA[i]) * eval(vectorB[i]) #This is the variable representing the multiplication
        summed += prod #adds the products within list
    print("A.B =",summed) #answer displayed

#Function calculating absolute value of vectorA list:

def absolute_function_incorporated(vectorA):
    if vectorA == listA:
        squar_sum = 0
        for i in range(3):
            sq = eval(vectorA[i])**2 
            squar_sum += sq
        squarrt_squar_sum = math.sqrt(squar_sum) #math square root function 
       
        print("|A| = {0:0.2f}".format(squarrt_squar_sum))        
#absolute value function of B
    elif vectorA == listB:
        sqr_sum = 0
        for i in range(3):
            sq = eval(vectorA[i])**2 #squares element of list B to make positive 
            sqr_sum += sq
        sqroot_sqr_sum = math.sqrt(sqr_sum)
        
        print("|B| = {0:0.2f}".format(sqroot_sqr_sum))
    
add_function(listA,listB)
product_func(listA,listB)
absolute_function_incorporated(listA)
absolute_function_incorporated(listB)