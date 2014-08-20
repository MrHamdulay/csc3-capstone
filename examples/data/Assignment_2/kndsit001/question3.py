import math

def main():
    answer = 2
    num = 2
    currentdenominator = math.sqrt(2)
    while currentdenominator < 2:
        answer = answer*(num/currentdenominator)
        currentdenominator = math.sqrt(2+currentdenominator)
    mypi = answer
    mypical = round(answer, 3)
    print("Approximation of pi:",mypical)
    radius = eval(input("Enter the radius:\n"))
    area = round(mypi*radius*radius, 3)
    print("Area:", area)
main()