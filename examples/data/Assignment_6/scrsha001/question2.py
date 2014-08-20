#Shaaheen Sacoor SCRSHA001
#19 April 2014
#Program to utilize 3d calculations of addition,multiplication and normalization

def main():
    import math
    vector_A = input("Enter vector A:\n")
    vectorA_list = vector_A.split() #makes vectors into list
    vector_B = input("Enter vector B:\n")
    vectorB_list = vector_B.split()
    additions = [] #Empty Variables to use later
    multiplications = []
    absoluteA =[]
    add_absoluteA = 0
    add_absoluteB = 0
    for i in range(len(vectorA_list)): #Goes through list
        addition = eval(vectorA_list[i]) +eval(vectorB_list[i]) #Adds the two numbers that are in the 
        additions.append(addition)                              #same position in the list.Adds this number to a list
        multiplication = eval(vectorA_list[i]) * eval(vectorB_list[i]) #same as before but multiplies
        multiplications.append(multiplication)
        add_absoluteA+=((eval(vectorA_list[i])))**2     #Adds the squares of the current number
        add_absoluteB+=((eval(vectorB_list[i])))**2
        
    add_multiplication = 0
    for j in range(len(multiplications)):            #Adds the multiplied numbers
        add_multiplication=add_multiplication + multiplications[j]
        
    print("A+B =",additions)
    print("A.B =",add_multiplication)
    print("|A| =",'{:.2f}'.format(math.sqrt(add_absoluteA),2))
    print("|B| =",'{:.2f}'.format(math.sqrt(add_absoluteB),2))        
main()
        
    