"""Basic Vector Calculations
Claudia Pastellides
23 April 2014"""

import math

def main():
    a=input("Enter vector A:\n")
    b=input("Enter vector B:\n")
    
    a_one,a_two,a_three=a.split(" ")
    b_one,b_two,b_three=b.split(" ")
    
    a_one=eval(a_one)
    a_two=eval(a_two)
    a_three=eval(a_three)
    b_one=eval(b_one)
    b_two=eval(b_two)
    b_three=eval(b_three)
    
    sum1=[a_one+b_one,a_two+b_two,a_three+b_three] #sum
    prod=a_one*b_one+a_two*b_two+a_three*b_three #product
    
    norm2_a=(a_one**2+a_two**2+a_three**2)
    norm2_b=(b_one**2+b_two**2+b_three**2)
    norm_a=math.sqrt(norm2_a)
    norm_b=math.sqrt(norm2_b) #norm calculation

    print("A+B =",sum1) #printing function
    print("A.B =",prod)
    round_a=round(norm_a,2)
    string_a=str(round_a)
    if len(string_a)<4:
        print("|A| = ",round_a,"0",sep="")
    else:
        print("|A| = ",round_a,sep="")
    round_b=round(norm_b,2)
    string_b=str(round_b)
    if len(string_b)<4:
        print("|B| = ",round_b,"0",sep="")
    else:
        print("|B| = ",round_b,sep="")    
    

    
main()


