height=4def push_up (grid):    """ Arrange and delete spaces of lists for merge"""       #def deletspaces_up(grid):    for i in range (3):         for rows in range (1,height):             for col in range (height):                 if grid[rows-1][col]==' ' or grid[rows-1][col] is 0:                    grid[rows-1][col]=grid[rows][col]                    grid[rows][col]=0            #def merge_tiles_up(grid):    """Merge like tiles"""    for rows in range (1,height):         for col in range (height):            if grid[rows-1][col]==grid[rows][col]:                grid[rows-1][col]=(2*grid[rows-1][col] )                 grid[rows][col]=0                                               """Re-arrange tiles after merge"""    #def delespaces_up_aftermerge(grid):    for rows in range (1,height):             for col in range (height):                if grid[rows-1][col]==' ' or grid[rows-1][col] is 0:                    grid[rows-1][col]=grid[rows][col]                    grid[rows][col]=0                              ###############################################################################def push_down (grid):    """ Arrange and delete spaces of lists for merge"""    for i in range (3):         for rows in range (2, -1, -1):             for col in range (height):                 if grid[rows+1][col]==" " or grid[rows+1][col] is 0:                    grid[rows+1][col]=grid[rows][col]                     grid[rows][col]=0                       #def merge_tiles_down(grid):    """Merge like tiles"""
    for rows in range (2, -1, -1):         for col in range (height):            if grid[rows+1][col]==grid[rows][col]:                grid[rows+1][col]=(2*grid[rows+1][col])                 grid[rows][col]=0                                 #def deletespaces_down_aftermerge(grid):    """Re-arrange tiles after merge"""    for rows in range (2, -1, -1):         for col in range (height):            if grid[rows+1][col]==" " or grid[rows+1][col] is 0:                grid[rows+1][col]=grid[rows][col]                grid[rows][col]=0                                        
         
                
                
######################################################################def push_left (grid):           
       """ Arrange and delete spaces of lists for merge"""  
    for i in range (3): 
        for col in range (1,height): 
            for rows in range (height): 
                if grid[rows][col-1]==" " or grid[rows][col-1] is 0:
                    grid[rows][col-1]=grid[col][rows] 
                    grid[rows][col]=0
                      
    for col in range (1,height): 
        for rows in range (height):
            if grid[rows][col-1]==grid[rows][col]:                grid[rows][col-1]=(2*grid[rows][col-1])                 grid[rows][col]=0    
    """Merge like tiles"""                
    for col in range (1,height): 
        for rows in range (height):            if grid[rows][col-1]==" " or grid[rows][col-1] is 0:
                grid[rows][col-1]=grid[rows][col]
                grid[rows][col]=0                          """Re-arrange tiles after merge"""


def push_right(grid):
    """ Arrange and delete spaces of lists for merge"""     
    for i in range (3):  
        for col in range (2, -1, -1): 
            for rows in range (height): 
                if grid[rows][col+1]==" " or grid[rows][col+1] is 0:
                    grid[rows][col+1]=grid[rows][col] 
                    grid[rows][col]=0                                             
                           """Merge like tiles""" 
    for col in range (2, -1, -1): 
        for rows in range (height):
            if grid[rows][col+1]==grid[rows][col]:
                grid[rows][col+1]=(2*grid[rows][col+1])
                grid[rows][col]=0                                         """Re-arrange tiles after merge"""               for col in range (2, -1, -1):         for rows in range (height):
            if grid[rows][col+1]==" " or grid[rows][col+1] is 0:
                grid[rows][col+1]=grid[rows][col]
                grid[rows][col]=0                                                                          