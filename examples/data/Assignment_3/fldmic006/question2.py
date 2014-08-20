def triangle(height):
    gap = " "
    width = "*"
    count = 1
    for i in range (0, height):
        print(gap*(height-1), end = '')
        print(width*count)
        count+=2
        height-=1
        
height = eval(input("Enter the height of the triangle:\n"))
triangle(height)