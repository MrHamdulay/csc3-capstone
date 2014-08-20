k = eval(input("Enter the height of the triangle:\n"))

for p in range(k):
    print((" "*(k-p-1)),"*"*(2*p+1),sep="")