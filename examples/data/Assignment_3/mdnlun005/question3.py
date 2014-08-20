def frame():
    message=input("Enter the message:\n")
    repeat=eval(input("Enter the message repeat count:\n"))
    thickness=eval(input("Enter the frame thickness:\n"))
    if repeat==0 or thickness==0: print('')
    else:
        n=2*thickness + repeat
        for i in range(n-1):
            if i ==0 or i == n-1:print("+"+(len(message)+2+2*thickness -4-2*i+2)*"-"+"+")
            elif i <thickness:
                print("|"*i+"+"+"-"*(len(message)+2+2*thickness -4-2*i+2)+"+"+"|"*i)
        for i in range(repeat):
            print("|"*thickness,message,"|"*thickness)
        for i in range(n,-1,-1):
                if i ==0 :print("+"+(len(message)+2+2*thickness -4-2*i+2)*"-"+"+")
                elif i <thickness:
                    print("|"*i+"+"+"-"*(len(message)+2+2*thickness -4-2*i+2)+"+"+"|"*i)

frame()