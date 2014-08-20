def tri():
    h=eval(input('Enter the height of the triangle:\n'))
    char=1
    space=h-1
    
    for i in range(0,h):
        print(' '*space,'*'*char,sep='')
        
        space-=1
        char+=2
        
        
       
tri()    
        
        

        
        
        
        
        


    
    
    