sHeight = eval(input("Enter the height of the triangle:\n"))
def triangle(height):
    for i in range(height):
        print(' '*((height*2 - i*2)//2 -1) + '*'*(2*i+1) + ' '*((height*2 - i*2)//2 -1) )
triangle(sHeight)