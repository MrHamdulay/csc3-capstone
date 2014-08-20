#13 March 2014
#Finding the are of a circle
import math

def main():
    calc_pi = math.sqrt(2)
    pi_val = 2*(2/calc_pi)

    while calc_pi != 2:
        calc_pi = math.sqrt(2 + calc_pi)
        pi_val = pi_val * (2/calc_pi)
    print("Approximation of pi:", round(pi_val,3))
    radius_1 = (eval(input("Enter the radius:\n")))
    area = (pi_val * (radius_1 ** 2))
    print("Area:", round(area,3))
main()