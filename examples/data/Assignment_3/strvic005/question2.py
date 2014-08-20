def triangle():
    x=eval(input("Enter the height of the triangle:\n"))
    y=1                                                      #number of stars
    
    
    for i in range(1,x+1):
        print((x-i)*' ', (2*i-1)*'*', sep='')                                  
        
triangle()
