height=eval(input("Enter the height of the triangle:\n"))
k = 1
for i in range(height,0,-1):
    print(" "*(i-1), '*'*k, sep = "")
    k+=2    