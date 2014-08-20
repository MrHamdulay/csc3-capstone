#24 march 2014
#sarayn subroyen


def rect(): 
    h = eval(input("Enter the height of the rectangle: \n"))
    w = eval(input("Enter the width of the rectangle: \n"))

    for i in range(h): #height
        print("*" * w) #width
   
rect()