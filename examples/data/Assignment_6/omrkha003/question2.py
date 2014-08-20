# program to do basic vector calculations in 3 dimensions
# khadeejah omar
# 20 april 2014

import math

a = input("Enter vector A: \n")
b = input("Enter vector B: \n")




# function to do vector addition calculation
def vector_addition() :
    
    addition_list = []
    for a_number in a.split() : # for each number in vector A
        a_number = eval(a_number) # for each number in vector B
        for b_number in b.split() :
            b_number = eval(b_number)
            addition = a_number + b_number # addition of elements
            addition_list.append(addition)

    # convert number back to string
    str_addition_list = []
    for number in addition_list :
        number = str(number)
        str_addition_list.append(number)

    # delete numbers that aren't the result of the addition of corresponding elements due to nested loop
    str_addition_list.pop(1)
    str_addition_list.pop(1)
    str_addition_list.pop(1) # index remains 1 and then 2, because as an element is deleted from a list, the list becomes shorter and the index value of the next element to be deleted decreases
    str_addition_list.pop(2)
    str_addition_list.pop(2)
    str_addition_list.pop(2)

    s = ", ".join(str_addition_list)
    print("A+B = [" + s + "]") 




# function to do dot product calculation
def dot_product() :
   
    product_list = []
    for a_number in a.split() : # for each number in vector A
        a_number = eval(a_number) # for each number in vector B
        for b_number in b.split() :
            b_number = eval(b_number)
            product = a_number * b_number # multiplication of elements
            product_list.append(product)
    
    # delete numbers that aren't the result of the multiplication of corresponding elements due to nested loop
    product_list.pop(1)
    product_list.pop(1)
    product_list.pop(1) # index remains 1 and then 2, because as an element is deleted from a list, the list becomes shorter and the index value of the next element to be deleted decreases
    product_list.pop(2)
    product_list.pop(2)
    product_list.pop(2)    

    # convert number back to string
    str_product_list = []
    for number in product_list :
        number = str(number)
        str_product_list.append(number)

    s = "+".join(str_product_list)
    add_products = eval(s)
    print("A.B = " + str(add_products))
    
    
    

# function to do normalisation
def norm() :
    
    # FOR VECTOR A
    
    squared_list = []
    global a
    for a_number in a.split() : # for each number in vector A
        a_number = eval(a_number)
        square = a_number ** 2 # square each number in vector A
        squared_list.append(square)
    
    # convert each number in list of squared number to string
    str_squared_list = []
    for number in squared_list :
        number = str(number)
        str_squared_list.append(number)
        
    a = "+".join(str_squared_list) # place addition symbol between each number-string
    a = eval(a)
    a = math.sqrt(a) # find the squareroot of the added squares
    square_root = round(a,2)
    print("|A| = " + "{0:.2f}".format(square_root))


    # FOR VECTOR B
    
    squared_list = []
    global b
    for b_number in b.split() : # for each number in vector B
        b_number = eval(b_number)
        square = b_number ** 2 # square each number in vector B
        squared_list.append(square)
    
    # convert each number in list of squared number to string
    str_squared_list = []
    for number in squared_list :
        number = str(number)
        str_squared_list.append(number)
        
    b = "+".join(str_squared_list) # place addition symbol between each number-string
    b = eval(b)
    b = math.sqrt(b) # find the squareroot of the added squares
    square_root = round(b,2)
    print("|B| = " + "{0:.2f}".format(square_root))



vector_addition()
dot_product()
norm()