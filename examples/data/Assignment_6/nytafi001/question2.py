""" A program to do basic vector calculations in 3 dimensions: addition, dot product and normalization.
Author: Afika Nyati
Date: 20th April 2014"""

from math import sqrt  # Importing the square-root function from the math library. This way, I don't have to write math.sqrt() when square-rooting.


def main():
    
    A,B = new_vector(2) # Assigns the two vectors created by the new_vector function to A and B.
    print("A+B =",vector_addition(A,B)) # Prints a vector addition done in the vector_addition function using vectors A and B.
    print("A.B =", dot_product(A,B)) # Prints a dot product done in the dot_product function using vectors A and B.
    print("|A| =", normalize(A)) # Prints a normalization done in the normalize function using vectors A and B.
    print("|B| =", normalize(B)) # Prints a normalization done in the normalize function using vectors A and B.
    

def new_vector(number): # This is a multipurpose function that creates as many vectors as the user wants. The number parameter is the amount of vectors created.
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # Assuming the user won't want more than 26 vectors, I have created a string of the alphabet and depending on how many vectors the user wants, creates a new vector named by a letter of the alphabet.
    
    return_values = [] # Initializes a list.
    
    for i in range(number): # A definite loop that creates as many vectors as requested by the user.
        Vector = str.split(input("Enter vector " + alphabet[i] + ":\n")) # This statement assigns a list of  three string numbers (the vector) to the Vector variable. Each number represents a dimension of the vector.
        
        for i in range(len(Vector)): # This nested deifinite loop coverts the string numbers in the Vector variable into integers so that they can undergo operations.
            Vector[i] = int(Vector[i]) # Changing each string number in the Vector varibale to an integer using the integer function.
        
        return_values.append(Vector) # Appends the the Vector list to the return_values list, thereby creating a list of lists (i.e. A list containing each vector called.
    
    return return_values # Return the list of vectors


def vector_addition(V1,V2):
    
    Addition = [ (V1[0]+V2[0]), (V1[1]+V2[1]), (V1[2]+V2[2])] # Adds the corresponding numbers of the dimesions of each vector together. This is then stored in a list called Addition.
    
    return Addition # Returns the Addition list which represents the vector addition.


def dot_product(V1,V2):
    
    Product = V1[0]*V2[0] + V1[1]*V2[1] + V1[2]*V2[2] # Multiples the corresponding numbers of the dimesions of each vector together. This is then stored in a list called Product.
    
    return Product # Returns the Product list which represents the vector addition.


def normalize(V): 

    normal_vector = sqrt(V[0]**2 + V[1]**2 + V[2]**2) # Normalizes a vector . Makes use of the math.sqrt function. This is then stored in a list called normal_vector.
    
    return "{0:0.2f}".format(normal_vector) # Returns a formatted list that is rounded to two decimal places.


main()  