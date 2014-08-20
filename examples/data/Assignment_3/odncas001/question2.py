def tri(height):
    for i in range(height):
        odd=2*i+1
        space=height-(i+1)
        print(space*" ",odd*"*",sep="")

height=eval(input("Enter the height of the triangle:\n"))
tri(height)
        
    