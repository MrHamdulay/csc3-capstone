import math
equation = input("Enter a function f(x):\n")
x = 0

for i in range(10, -11,-1):
    for j in range(-10, 11, 1):
        x = j
        y = round(eval(equation))
        if y == i:
            print("o", end = "")
        if i == 0 and j == 0 and y != i:
            print("+", end = "")
        if i == 0 and j!= 0 and y != i:
            print("-", end = "")
        if j == 0 and i != 0 and y!= i:
            print("|", end = "")
        elif j != 0 and i != 0 and y != i:
            print(" ", end = "")
    print()  
            
        
            