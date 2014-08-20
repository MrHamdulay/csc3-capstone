# Author : Rayaan Fakier FKRRAY001
# Date : 20 - 03 - 2014
# Question 2

def main():
    h = int(input("Enter the height of the triangle:\n"))
    # Nested for loops to print *
    for i in range(0,h,1):
        for j in range(1): # Range of 1 to print one row of * per i iteration
            print(" " * (-i) + ((h-1)-i)*(" ") + "*" * (2*(i-j)+1))
        
main()