'''Q3 of Assignment 7: Merging functions for 2048 game
Patrick Boroughs
27 April 2014'''

def push_up (grid):
    """merge grid values upwards"""
    
    def shiftU():
        for loop in range(3): 
            blank_pos=-1        #position where 0 found
            blank_found=False   #if 0 has been found
            
            for col in range(4):
                for row in range(4): #from top to bottom
                    
                    #if value needs to be shifted
                    if blank_found and grid[row][col]: 
                        grid[row][col],grid[blank_pos][col],blank_pos=0,grid[row][col],row
                    
                    #if first 0 of the column is found                   
                    elif not grid[row][col] and not blank_found:
                        blank_pos=row
                        blank_found=True
                    
                    #end of column - reset variables for new column    
                    if row==3:
                        blank_found=False
                        blank_pos=-1        
            
             
    def mergeU():
        #merging values if adjacent numbers equal
        for col in range(4):
            for row in range(3):
                if grid[row][col]==grid[row+1][col]:
                    grid[row][col],grid[row+1][col]=grid[row][col]*2,0
                    
    shiftU() #shift everything up
    mergeU() #merge adjacent values
    shiftU() #shift everything up
    return grid    


def push_down (grid):
    """merge grid values downwards"""
    
    def shiftD():
        for loop in range(3):
            blank_pos=-1        #position where 0 found
            blank_found=False   #if 0 has been found
            
            for col in range(4):
                for row in range(3,-1,-1): #from bottom to top
                    
                    #if value needs to be shifted
                    if blank_found and grid[row][col]:
                        grid[row][col],grid[blank_pos][col],blank_pos=0,grid[row][col],row
                    
                    #if first 0 of the column is found                      
                    elif not grid[row][col] and not blank_found:
                        blank_pos=row
                        blank_found=True
                    
                    #end of column - reset variables for new column     
                    if row==0:
                        blank_found=False
                        blank_pos=-1        
    def mergeD():
        #merging values if adjacent numbers equal
        for col in range(4):
            for row in range(3,0,-1):
                if grid[row][col]==grid[row-1][col]:
                    grid[row][col],grid[row-1][col]=grid[row][col]*2,0          
                       
    shiftD() #shift everything down
    mergeD() #merge adjacent values
    shiftD() #shift everything down
    return grid    

def push_left (grid):
    """merge grid values left"""
    def shiftL():

        for loop in range(3):
            blank_pos=-1        #position where 0 found
            blank_found=False   #if 0 has been found
            for row in range(4):
                for col in range(4): #from left to right
                
                    #if value needs to be shifted
                    if blank_found and grid[row][col]:
                        grid[row][col],grid[row][blank_pos],blank_pos=0,grid[row][col],col
                
                        #if first 0 of the row is found                      
                    elif not grid[row][col] and not blank_found:
                        blank_pos=col
                        blank_found=True
                
                    #end of row - reset variables for new row     
                    if col==3:
                        blank_found=False
                        blank_pos=-1
            
    def mergeL():
        #merging values if adjacent numbers equal
        for row in range(4):
            for col in range(3):
                if grid[row][col]==grid[row][col+1]:
                    grid[row][col],grid[row][col+1]=grid[row][col]*2,0    
    
    shiftL() #shift everything left
    mergeL() #merge adjacent values
    shiftL() #shift everything left
    return grid    

def push_right (grid):
    """merge grid values right"""  
    
    def shiftR():
        for loop in range(3):
            blank_pos=-1        #position where 0 found
            blank_found=False   #if 0 has been found
            for row in range(4):
                for col in range(3,-1,-1): #from right to left
                    
                    #if value needs to be shifted
                    if blank_found and grid[row][col]:
                        grid[row][col],grid[row][blank_pos],blank_pos=0,grid[row][col],col
                    
                    #if first 0 of the row is found                      
                    elif not grid[row][col] and not blank_found:
                        blank_pos=col
                        blank_found=True
                    
                    #end of row - reset variables for new row     
                    if col==0:
                        blank_found=False
                        blank_pos=-1        
    def mergeR():       
        #merging values if adjacent numbers equal
        for row in range(4):
            for col in range(3,0,-1):
                if grid[row][col]==grid[row][col-1]:
                    grid[row][col],grid[row][col-1]=grid[row][col]*2,0    
                    
    shiftR() #shift everything up
    mergeR() #merge adjacent values
    shiftR() #shift everything up
    return grid 
    
