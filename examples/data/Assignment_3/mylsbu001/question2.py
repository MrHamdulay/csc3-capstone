height = eval(input("Enter the height of the triangle:\n"))
space=" "
odd=1
i=0
c=height
while(i<height):
    i=i+1
    c = c-1
    print(space*(c),end="*"*odd)
    print()
    odd = odd+2 
   
    