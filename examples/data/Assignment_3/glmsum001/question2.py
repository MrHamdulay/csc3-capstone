def triangleShape():

    height = int(input("Enter the height of the triangle: \n"))
    
    counter = 1

    newH = height

    for i in range(0,height):
   
        print(' '*(newH-1),end='')

        print('*'*(counter))

        newH+=-1

        counter+=2

triangleShape()