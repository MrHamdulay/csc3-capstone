def Triangle():
    height = eval(input("Enter the height of the triangle:\n"))
    baseLength = (height*2) - 1
    out='{0:^' + str(baseLength) +'}' 
    for i in range (0,height):
        print(out.format(((1+(i*2))*'*')))
Triangle()
