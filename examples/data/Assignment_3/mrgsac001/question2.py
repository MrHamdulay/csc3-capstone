m=eval(input("Enter the height of the triangle: \n"))
n=" "
o=1
while m>=1:
    print(n*(m-1),o*"*", sep="")
    o+=2
    m=m-1