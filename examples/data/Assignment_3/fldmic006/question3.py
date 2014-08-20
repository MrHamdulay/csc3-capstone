def frame (message, repeat, thickness):
    
    dash = len(message)+2* thickness
    
    #adding in the '|' and printing frame thickness for the top of the frame
    for i in range(thickness):
        print("|"*i, "+", "-"*dash, "+", "|"*i, sep = "")
        dash -= 2
    
    #adding the message within the frame    
    for j in range(repeat):
        print("|"*thickness, message, "|"*thickness)
        
    #increase dash as on last edition of for loop i, it decreased. increase to get back to length output in i
    dash +=2
        
    for k in range(thickness, 0, -1):
        print("|"*(k-1), "+", "-"*dash, "+", "|"*(k-1), sep = "")
        dash += 2       
    
message = input("Enter the message:\n")
repeat = eval(input("Enter the message repeat count:\n"))
thickness = eval(input("Enter the frame thickness:\n"))

frame(message, repeat, thickness)