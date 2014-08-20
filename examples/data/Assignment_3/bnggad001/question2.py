h = eval(input("Enter the height of the triangle:\n"))
y= h*2
gap = (y//2) - 1

for i in range(0,y,2):
    
    print(' '*gap, end = '')
    
    print('*' * (i+1)) 
    
    gap = gap -1
    