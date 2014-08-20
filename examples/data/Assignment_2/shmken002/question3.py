#program that calculates the value of PI and then computes and displays the area of a circle with radius entered by the user
#kenneth shimabukuro
#12/03/14
import math
def main():
    print("Approximation of pi:", (round(math.pi, 3)))
    r=eval(input("Enter the radius:\n"))
    ans=(print("Area:", (round(math.pi*r**2, 3))))
main()