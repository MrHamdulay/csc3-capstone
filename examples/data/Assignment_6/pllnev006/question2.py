#Program to perform vector calculations
#Nevarr Pillay - PLLNEV006
#22 April 2014

def readIn_vec(vec_letter): #Reads in a vector using the letter passed as its name
    values = input("Enter vector " + vec_letter + ":\n")
    vector = values.split(" ")
    for i in range(len(vector)):
        vector[i] = eval(vector[i])
    return vector

def vec_add(vector1,vector2): #Adds two vectors
    new_vector = []
    for i in range(len(vector1)):
        tempsum = vector1[i] + vector2[i]
        new_vector.append(tempsum)
    return new_vector

def vec_multiply(vector1,vector2): #Multiplies two vectors
    product = 0
    for i in range(len(vector1)):
        product += vector1[i]*vector2[i]
    return product

def single_vec(vector): #Returns the resultant of a single vector
    sqrdsum = 0
    for i in range(len(vector)):
        sqrdsum += vector[i]**2
    return (sqrdsum**(1/2))    

def main():
    vecA = readIn_vec("A")
    vecB = readIn_vec("B")
    add = "A+B = {sum}" # Formats for the outputs
    multiply = "A.B = {prod}"
    single = "|{0}| = {resultant:.2f}"
    print(add.format(sum = vec_add(vecA,vecB)))
    print(multiply.format(prod = vec_multiply(vecA,vecB)))
    print(single.format("A",resultant = single_vec(vecA)))
    print(single.format("B",resultant = single_vec(vecB)))
    
if __name__ == "__main__":
    main()
        