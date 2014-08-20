height = eval(input("Enter the height of the triangle: \n"))
real_height = height + height
gap = ((real_height//2)-1)
#if height%2==0 or height%2!=0:
gap-=1
b = real_height-2
#else:
            #gap = gap
            #b = real_height-1 
for i in range(0, real_height, 2):
            if i >= 0 and i < b:
                        print(' '*(gap), end=' ')
                        print('*'*(i+1))
                        gap-=1
            
            else:
                        print('*'*(i+1))    
        
    