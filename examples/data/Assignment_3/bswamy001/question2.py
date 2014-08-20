height=eval(input("Enter the height of the triangle:\n"))
for i in range(height): 
    gap=(height-i-1)*' '
    star=(i+i+1)*'*'
    print(gap,star,sep='')
    
            