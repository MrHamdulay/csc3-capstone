def align_right(x):
    name=[] #list of names
    x= input("Enter strings (end with DONE):\n") 
    y=len(x)
    while x!= "DONE":
        name.append(x) #adds x to the list name
        x=input() #
        if len(x)>y:
            y=len(x)
    print()
    print("Right-aligned list:")
    for i in name:
        print ("{:>{}}".format(i,y))
              
align_right('x')