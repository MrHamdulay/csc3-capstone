height=4
    for rows in range (2, -1, -1): 
         
                
                
######################################################################
   
    for i in range (3): 
        for col in range (1,height): 
            for rows in range (height): 
                if grid[rows][col-1]==" " or grid[rows][col-1] is 0:
                    grid[rows][col-1]=grid[col][rows] 
                    grid[rows][col]=0
                      
    for col in range (1,height): 
        for rows in range (height):
            if grid[rows][col-1]==grid[rows][col]:
    """Merge like tiles"""                
    for col in range (1,height): 
        for rows in range (height):
                grid[rows][col-1]=grid[rows][col]
                grid[rows][col]=0  



    """ Arrange and delete spaces of lists for merge"""     
    for i in range (3):  
        for col in range (2, -1, -1): 
            for rows in range (height): 
                if grid[rows][col+1]==" " or grid[rows][col+1] is 0:
                    grid[rows][col+1]=grid[rows][col] 
                    grid[rows][col]=0 
                       
    for col in range (2, -1, -1): 
        for rows in range (height):
            if grid[rows][col+1]==grid[rows][col]:
                grid[rows][col+1]=(2*grid[rows][col+1])
                grid[rows][col]=0 
            if grid[rows][col+1]==" " or grid[rows][col+1] is 0:
                grid[rows][col+1]=grid[rows][col]
                grid[rows][col]=0       