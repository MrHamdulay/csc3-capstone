def rectangle():
    #INPUT
    height = eval(input("Enter the height of the rectangle: \n"))
    width = eval(input("Enter the width of the rectangle: \n"))
   
    #output -- processing
    for i in range(0,height):
        print("*"*width)
         
rectangle()