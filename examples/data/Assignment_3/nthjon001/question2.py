height=eval(input("Enter the height of the triangle:\n"))
gap=height
stars=1
for i in range (height):
    gap-=1
    print(gap*' ', stars*'*', sep='')
    stars+=2