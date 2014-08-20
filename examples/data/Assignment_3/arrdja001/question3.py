m = input("Enter the message: \n")
rc = eval(input("Enter the message repeat count: \n"))
ft = eval(input("Enter the frame thickness: \n"))

l = len(m)

if rc != 0 and ft !=0:

    print("+" + (l+ft)*"-" + "-"*ft +"+")
    if ft != 1:
        num = 1
        dash = ft-1
        while num != (ft):
            print("|"*num + "+" + (l+(dash))*"-" + "-"*(dash)+"+" + "|"*num)
            num = num + 1
            dash = dash - 1

    for i in range(rc):
        print("|"*ft + " "  + m + " " + "|"*ft)

    if ft != 1:
         num = ft-1
         dash = l+2
         
         while num != 0:
            print("|"*num + "+" + dash*"-" + "+" + "|"*num)
            num = num - 1
            dash = dash + 2

    print("+" + (l+ft)*"-" + "-"*ft +"+")
    
    


