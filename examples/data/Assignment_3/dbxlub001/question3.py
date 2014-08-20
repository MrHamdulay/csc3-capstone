def mrFrame():
    message=input("Enter the message:\n")
    count=eval(input("Enter the message repeat count:\n"))
    thick=eval(input("Enter the frame thickness:\n"))
    len1=len(message)
    len2=len1+2
    len3=len2+2*(thick-1)
    j=0
    thick2=thick-1
    leny2=len2
    count2=thick-1
    yay=(len2-len1)//2
    while len3>= len2 and j<thick:
        print("|"*j+"+"+"-"*len3+"+"+"|"*j)
        len3=len3-2
        j=j+1
    for h in range(count):
        print("|"*thick+" "*yay+message+" "*yay+"|"*thick)
    while len2+2*thick>leny2>=len2:
        print("|"*count2+"+"+"-"*leny2+"+"+"|"*count2)
        thick2=thick2-1
        leny2=leny2+2
        count2=count2-1
mrFrame()