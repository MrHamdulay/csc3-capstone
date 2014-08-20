H = eval(input("Enter the height of the triangle:\n"))
y = H-1
space = H//2
for i in range(1,(y*2)+2,2):
        print(' '*(H-1),'*'*i, sep='')
        H=H-1
        
