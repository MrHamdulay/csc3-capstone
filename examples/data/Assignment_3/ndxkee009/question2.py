#Keegan Naidoo
#NDXKEE009

h=eval(input("Enter the height of the triangle: \n"))

ch=1

gap=h

for i in range(0,h):
   
    print(' '*(gap-1),end='')
    print('*'*(ch))
    
    #print(' '*(h),'*'*ch,' '*(h))
    
    #print(h-1)
    
    gap+=-1
    ch+=2

