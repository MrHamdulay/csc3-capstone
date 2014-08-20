"""shriya roy
4 April 2014
program to do basic vector calculations"""


def main():
    #import math library
    import math
    #get input from user
    
    a=(input("Enter vector A:\n"))
    b=(input("Enter vector B:\n"))
    #create lists from input
    A=a.split(" ")
    B=b.split(" ")
    
    #sum function
    _sum1=eval(A[0])+eval(B[0])
    _sum2=eval(A[1])+eval(B[1])
    _sum3=eval(A[2])+eval(B[2])
    Totalsum=[_sum1 , _sum2 ,_sum3]
    
    
    #multiplication function
    multiply1= eval(A[0])*eval(B[0])
    multiply2=eval(A[1])*eval(B[1])
    multiply3=eval(A[2])*eval(B[2])
    total_multiply= multiply1 + multiply2 + multiply3
    #squarerooting a sum of numbers 
    absolute_A1= (eval(A[0])**2)
    absolute_A2= (eval(A[1])**2)
    absolute_A3= (eval(A[2])**2)
    total_absoluteA= math.sqrt( absolute_A1 + absolute_A2 + absolute_A3 )
    
    #squarerooting a sum of numbers
    absolute_B1= (eval(B[0])**2)
    absolute_B2= (eval(B[1])**2)
    absolute_B3= (eval(B[2])**2)
    total_absoluteB=math.sqrt( absolute_B1 + absolute_B2 + absolute_B3)
    
    
    
    
    
    
    #printing output
    print("A+B =", Totalsum)
    print("A.B =", total_multiply)
    output= "{0:.2f}".format(total_absoluteA)
    print("|A| =", output)
    outputB= "{0:.2f}".format(total_absoluteB)
    
    print("|B| =", outputB)
    
    
    
    
    
main()