# calculate number of k-permutations of n items
# Saul Bloch
# 14 april 2014

#Gets a string, converts it to a number and then returns it
def get_integer (x):
    y = input("Enter "+x+":\n")
    while not y.isdigit():
        y = input("Enter "+x+":\n")
    y = eval(y)  
    return y

#Taks the number and returns its factorial
def calc_factorial (x):
    for i in range (1, x):
        x = x*i
    return x
       
