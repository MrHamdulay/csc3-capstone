import math
def main():
    answer=2
    num=2
    current_deno=math.sqrt(2)
    while (current_deno<2):
        answer*=num/current_deno
        current_deno=math.sqrt(2+current_deno)
    pi=answer
    pi_calc=round(answer,3)
    print("Approximation of pi:",pi_calc)
    r=eval(input("Enter the radius:\n"))
    area=round(pi*r*r,3)
    print("Area:",area)
main()
           