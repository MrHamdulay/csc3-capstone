def tri():
        h=eval(input("Enter the height of the triangle:\n"))
        x=0
        space=h-2
        for i in range (1,h):
                print(" "*space,"*"*(x+1)," "*space)
                x+=2
                space-=1
        if h!=1:
                if h!=0:
                        print("*"*(x+1),""*space)
                else:
                                print("")
        else:
                print("*")
                        
tri()
        
    