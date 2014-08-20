"""Assignment 6 question 2
shannon clacey
23 april 2014"""
import math
def vector():
    A = input("Enter vector A:\n") #getting input for vector a
    B = input("Enter vector B:\n") #getting input for vector b
    a_list = A.split(" ") # creating the list for a
    b_list = B.split(" ") #creating the list for b
    num_a1 = eval(a_list[0]) #getting the numerical value for each item in the list
    num_a2 = eval(a_list[1])
    num_a3 = eval(a_list[2])
    num_b1 = eval(b_list[0])
    num_b2 = eval(b_list[1])
    num_b3 = eval(b_list[2])
    product_1 = eval(a_list[0]) *eval(b_list[0]) #determining the product of corresponding items in the list
    product_2 = eval(a_list[1]) * eval(b_list[1])
    product_3 = add_3 = eval (a_list[2]) * eval(b_list[2])
    add_product = product_1+product_2 +product_3
    power_A1 = eval(a_list[0])**2 #determing the square of items in the list a
    power_A2 = eval(a_list[1])**2
    power_A3 = eval (a_list[2])**2
    sqrt_a = math.sqrt(power_A1 +power_A2 +power_A3) #finding the square root of the sum of the squares
    round_sqrta = round(sqrt_a, 2)  #rounding square root to 2 decimal places                
    power_B1 =eval(b_list[0])**2 #determining square of items in list
    power_B2 =eval(b_list[1])**2
    power_B3 =eval(b_list[2])**2
    sqrt_b = math.sqrt(power_B1 + power_B2 +power_B3) #square rooting the square of the items
    round_sqrtb = round(sqrt_b, 2) #rounding square root to two decimal places
    print("A+B = [", num_a1+num_b1, ", ", num_a2+num_b2, ", ", num_a3+num_b3, "]", sep='')
    print("A.B = ", add_product, sep='')
    str_a =str(round_sqrta)
    str_b =str(round_sqrtb)
    if len(str_a) <4:
        print("|A| = ", round_sqrta, "0", sep='')
    else:
        print("|A| = ", round_sqrta, sep='')
    if len(str_b)<4:
        print("|B| = ", round_sqrtb, "0", sep='') 
    else:
        print("|B| = ", round_sqrtb, sep='')
vector()