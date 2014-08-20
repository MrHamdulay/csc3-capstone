#Tato Moaki MKXTAT001
#Programme to do vector calculations in three dimensions
#4/20/2014
def main():
    import math
    vector_A = input("Enter vector A:\n")
    vector_B = input("Enter vector B:\n")
    vector_Sum = [] #empty list
    vector_Product = 0 #assign accumulator to zero
    norm_A = 0
    norm_B = 0
    
    vector_A = vector_A.split()#split input by white space
    vector_B = vector_B.split()      
       
    for i in range(3):
        vector_Sum.append(eval(vector_A[i]) + eval(vector_B[i])) #evaluate the vector sum
        vector_Product += (eval(vector_A[i]) * eval(vector_B[i]))
        norm_A += (math.pow(float(vector_A[i]),2))
        norm_B += float(math.pow(float(vector_B[i]),2))
        
    norm_A = math.sqrt(norm_A)#round norm_A to two decimal places
    norm_B = math.sqrt(norm_B)
    
    print("A+B =",vector_Sum)
    print("A.B =",vector_Product)
    print("|A| = {:.2f}".format(norm_A))
    print("|B| = {:.2f}".format(norm_B))
    
if __name__=="__main__":
    main()