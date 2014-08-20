h=eval(input('Enter the height of the triangle:\n'))
space=h-1
num=1
for i in range(h):
    print(space*' '+num*'*') 
    space-=1
    num+=2
    
