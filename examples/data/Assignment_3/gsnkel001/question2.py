height=eval(input("Enter the height of the triangle:\n"))
gap=height-1
d=1
for i in range(1,height+1,1):
    print(gap*' '+'*'*(2*i-1))
    gap=gap-1

    
    
