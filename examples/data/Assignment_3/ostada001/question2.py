h = eval(input("Enter the height of the triangle:\n"))

for i in range (1,h+1,1):
    print(" "*(h-i),("*"*(2*i-1)),sep = "")