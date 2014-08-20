def message():
    x = input("Enter the message: \n")
    y = eval(input("Enter the message repeat count: \n"))
    z = eval(input("Enter the frame thickness: \n"))
    a = len(x)
    b = "+" 
    c="-"
    d="|"
    for i in range(0, z):
        print(d*i, b, c*(a + 2*(z-i)), b, d*i, sep="")
    for i in range (y):
        print(d*z, x, d*z, end="\n")
    for i in range(z-1, -1, -1):
        print(d*i, b, c*(a + 2*(z-i)), b, d*i, sep="")  
               #first line length + 4, second line length +2
message()    