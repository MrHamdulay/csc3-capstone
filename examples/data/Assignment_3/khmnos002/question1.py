height = eval(input('Enter the height of the rectangle: \n'))
width = eval(input('Enter the width of the rectangle: \n'))
if height > 0 and width > 0:
    for i in range(height):
        for j in range(width-1):
            print('*', end = "")
        print('*')    