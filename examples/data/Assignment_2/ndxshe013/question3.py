#Assignment 2 question3
#STUDENT NO.:NDXSHE013


import math
def main():
    ans=2
    num=2
    current_deno=math.sqrt(2)
    while (current_deno<2):
        ans*=num/current_deno
        current_deno=math.sqrt(2+current_deno)
    pi=ans
    pi_calc=round(ans,3)
    print("Approximation of pi:",pi_calc)
    r=eval(input("Enter the radius:\n"))
    area=round(pi*r**2,3)
    print("Area:",area)
main()
           