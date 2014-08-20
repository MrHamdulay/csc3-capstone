def Frame():
    Message=input("Enter the message: \n")
    Repeat=eval(input("Enter the message repeat count:\n"))
    Thickness=eval(input("Enter the frame thickness: \n"))
    n=2*Thickness+Repeat
    if Repeat==0 or Thickness==0:
        print("")
    else:
        for i in range(n-1):
            if i==0 or i==n-1:
                print("+"+(len(Message)+2+2*Thickness -4-2*i+2)*"-"+"+")
            elif (i < Thickness):
                print("|"*i+"+"+"-"*(len(Message)+2+2*Thickness -4-2*i+2)+"+"+"|"*i)
        for i in range(Repeat):
            print("|"*Thickness,Message,"|"*Thickness)
        for i in range(n,-1,-1):
            if i==0:
                print("+"+(len(Message)+2+2*Thickness-4-2*i+2)*"-"+"+")
            elif i<Thickness:
                print("|"*i+"+"+"-"*(len(Message)+2+2*Thickness -4-2*i+2)+"+"+"|"*i)
Frame()