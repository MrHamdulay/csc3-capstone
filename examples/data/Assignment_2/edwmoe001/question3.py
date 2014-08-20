import math

def main():
    rt= math.sqrt(2)
    pi_approx=2
     
    while rt!=2:
        pi_approx=pi_approx*2/rt
        rt+=2
        rt=math.sqrt(rt)
    pi=round(pi_approx,3)
    print("Approximation of pi:",pi)
    r=eval(input("Enter the radius:\n"))
    print("Area:",round(pi_approx*r**2,3))
main()