'''program to do simple vector calculations
Wandile Khowa
20-04-2014
'''
def addition(a, b): #creates a function for vector addition
    list_n = []
    a_new = a.split()   #splits a into list/sub-strings
    b_new = b.split()   #splits b into list/sub-strings  
    x_comp = (eval(a_new[0]) + eval(b_new[0]))  #adds first numbers of both list
    y_comp = (eval(a_new[1]) + eval(b_new[1]))  #adds second numbers of both lists
    z_comp = (eval(a_new[2]) + eval(b_new[2]))  #adds third numbers of both lists
    x_comp_n = "["+str(x_comp)+","
    y_comp_n = str(y_comp)+","
    z_comp_n = str(z_comp)+"]"
    print("A+B =", x_comp_n, y_comp_n, z_comp_n) #prints out the numbers in required vector format
    
    
def dot(a, b):          #creates a function for dot products
    a_new = a.split()   #splits a into list/sub-strings
    b_new = b.split()   #splits b into list/sub-strings
    x_comp = (eval(a_new[0]) * eval(b_new[0]))  #multiplies x-components of both vectors
    y_comp = (eval(a_new[1]) * eval(b_new[1]))  #multiplies y-components of both vectors
    z_comp = (eval(a_new[2]) * eval(b_new[2]))  #multiplies z-components of both vectors
    print("A.B =", x_comp + y_comp + z_comp)    #prints out final solution
    
def normal(a):                  #creates function for normalization
    a_new = a.split()           #splits a into list/sub-strings   
    x_comp = float(eval(a_new[0])**2)  #squares x-component of a
    y_comp = float(eval(a_new[1])**2)  #squares y-component of a
    z_comp = float(eval(a_new[2])**2)  #squares z-component of a
    sum_vect = float(x_comp + y_comp + z_comp) #finds the sums of all squares
    ans = (float(sum_vect))**(1/2) #finds the square root
    final = "%.2f" % ans #formats the answer so that it shows two decimal places
    return final #returns the solution back to the caller

def main(): #main program where all the sub-programs are going to be called
    vect_A = input("Enter vector A: \n")
    vect_B = input("Enter vector B: \n")
    addition(vect_A, vect_B)
    dot(vect_A, vect_B)
    print("|A| =", normal(vect_A))
    print("|B| =", normal(vect_B))
    
if __name__== '__main__':   #controls which function is run when the whole program is run
    main()
    