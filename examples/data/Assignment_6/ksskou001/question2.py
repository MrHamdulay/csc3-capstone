'''This program does three basic vector calculations in 3 dimensions
Hermann KOUASSI
19 april 2014'''

import math
    
def addition(A,B):
    '''Finds and returns the three coordinates of the resultant from adding two verctors A and B'''
    #create an array to store the coordinates
    resultant = []
    #iterate over the three coordinates
    for i in range(len(A)):
        #add the corresponding coordinates of vector A and B using eval to convert string into integer
        x = eval(A[i]) + eval(B[i])
        #store the resultant coordinate into the created array 
        resultant.append(x)
    #returns the resultants coordinates 
    return resultant   
    

def dot_product(A,B):
    '''calculate and returns the dot product of two vectors A and B'''
    dot_product = 0
    #iterate over the three coordinates
    for i in range(len(A)):
        #multiply the corresponding coordinates of A and B
        x = eval(A[i])*eval(B[i])
        #add the three products
        dot_product += x
    return dot_product


def normalization(A):
    '''calculates and returns the norm of a given vector knowing its coordinates'''
    x = 0
    #iterate over the three coordinates
    for i in range(len(A)):
        #comput the sum of the squares the three coordinates
        x += eval(A[i])**2
    #take the square root of the sum of the squares of the coordinates to get the norm  
    norm = math.sqrt(x)
    #format norm to two decimal positions
    norm = '{0:.2f}'.format(norm)
    return norm


def main():
    '''main function'''
    #get the coordinates of the function A as strings seperated by spaces
    A_str = input('Enter vector A:\n')
    #split it using spaces to get a list of coordinates
    A = A_str.split(' ')
    #see the above:(line 49 to 52)
    B_str = input('Enter vector B:\n')
    B = B_str.split(' ')
    #add vectors A and B and print out the coordinates of the resultant a
    a = addition(A,B)
    print('A+B =',a)
    #comput dot product of A and B and print the result d out
    d = dot_product(A,B)
    print('A.B =',d)
    #comput the norm n of A and B and print them out  
    n = normalization(A)
    print('|A| =',n)
    normalization(B)
    n = normalization(B)
    print('|B| =',n)
    
if __name__=="__main__":
    main()