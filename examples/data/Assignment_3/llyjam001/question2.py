height=eval(input("Enter the height of the triangle:\n"))

gap=height-1
number=1

for i in range(height):
    print(gap*' ',end='')
    print('*'*number)
    
    gap=gap-1
    number=number+2