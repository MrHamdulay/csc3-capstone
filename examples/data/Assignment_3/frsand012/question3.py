def sq():
    x = input("Enter the message: \n")
    y = eval(input("Enter the message repeat count: \n"))
    z = eval(input("Enter the frame thickness: \n"))
    
    top = 0
    length = len(x) + z*2
    for a in range (z):
        print(top * "|", "+", length * "-", "+", top * "|", sep = "")
        length -= 2
        top += 1
    
    for b in range (y):
        print("|"*z,x,"|"*z)
        
    lengthofnew = len(x) + 2
    verticalsofnew = z - 1
    for c in range(z):
            print(verticalsofnew * "|", "+", lengthofnew * "-", "+", verticalsofnew * "|", sep = "")    
            lengthofnew += 2
            verticalsofnew -= 1  
    
        
sq()
        
        