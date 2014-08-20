"""program to do basic vector calculations in 3 dimensions: addition, dot product and normalization.
Gary Finkelstein
22 April 2014"""
#allow for user input
vectorA_input = input("Enter vector A:\n")
#split input into array on space
vector_A = vectorA_input.split(" ")
#allow for user input
vectorB_input = input("Enter vector B:\n")
#split input into array on space
vector_B = vectorB_input.split(" ")

#create new arrays to store new calculated values
new = ["","",""]
new2 = ["","",""]
new3 = ["","",""]
new4 = ["","",""]

#function that adds the number in a position in array1 with the number in the corresponding position in array2
def add(vector_A,vector_B):
    count = 0
    while count < len(vector_A):
        num = int(vector_A[count])
        num2 = int(vector_B[count])
        new[count] = num + num2 
        count +=1
    print("A+B = ", end="")
    print(new)

#function that multiplies the number in a position in array1 with the number in the corresponding position in array2 and then adds the products together to get a value      
def dot_product(vector_A,vector_B):
    count = 0
    while count <= 2:
        num = int(vector_A[count])
        num2 = int(vector_B[count])
        new2[count]= num*num2 
        count +=1
    print("A.B = ", end="")
    print(new2[0] + new2[1] + new2[2])    

#function that sums the squares of the elements in array1 and then square roots this value to produce a new value
def normalisationA(vector_A):
    count = 0
    while count <= 2:
        num = int(vector_A[count])
        new3[count]= num**2 
        count +=1
    x = new3[0] + new3[1] + new3[2]
    print("|A| = ", end="")
    print("%.2f" % round((x**0.5),2))       

#function that sums the squares of the elements in array2 and then square roots this value to produce a new value
def normalisationB(vector_B):   
    count = 0
    while count <= 2:
        num = int(vector_B[count])
        new4[count]= num**2 
        count +=1
    y = new4[0] + new4[1] + new4[2]
    print("|B| = ", end="")
    print("%.2f" % round((y**0.5),2))          
    
    
    
#calls the various functions
add(vector_A,vector_B)
dot_product(vector_A,vector_B)
normalisationA(vector_A)
normalisationB(vector_B)



