#Program to manipulate 2-dimensional arrays of size 4x4
#Saul Bloch
#29 April 2014

#create a 4x4 grid
def create_grid(grid):
    
    for i in range(4):
        grid.append([0]*4)
        
    return grid

#print out a 4x4 grid in 5-width columns within a box
def print_grid(grid):
    print('+','-'*20,'+', sep="")
    for i in range(4):
        print('|', end="")
        for j in range(4):
            if grid[i][j] == 0:
                temp=" "
            else: temp= grid[i][j]
            formatted_string = "{0:<5}".format(temp)
            print(formatted_string, end="")            
            
        print('|')
    print('+','-'*20,'+', sep="")
    
#return True if there are no 0 values and no adjacent values that are equal; otherwise False  
def check_lost(grid):
    for x in range(4):   
        for y in range(4):
            if grid[x][y] == 0:
                return False 
        
    for i in range(4):
        for j in range(4):
            #Checks all corner blocks and sees if there are any blocks that are the same around it
             
            if i==3 and j==0:
                if grid[i][j] == grid[i][j+1] or grid[i][j] == grid[i-1][j]:
                    return False
                                            
            elif i==3 and j==3:
                if grid[i][j] == grid[i][j-1] or grid[i][j] == grid[i-1][j]:
                    return False            
            
            elif i ==0 and j==0:
                if grid[i][j] == grid[i][j+1] or grid[i][j] == grid[i+1][j]:
                    return False
                
            elif i==3 and j==0:
                if grid[i][j] == grid[i][j+1] or grid[i][j] == grid[i-1][j]:
                    return False
                                
            elif i==3 and j==3:
                if grid[i][j] == grid[i][j-1] or grid[i][j] == grid[i-1][j]:
                    return False
                
            elif i==0 and j==3:
                if grid[i][j] == grid[i][j-1] or grid[i][j] == grid[i+1][j]:
                    return False
                
            #Checks all side middle blocks and sees if there are any blocks that are the same around it
                
            elif i ==1 and j==0:
                if grid[i][j] == grid[i+1][j]:
                    return False
                    
                    
            elif i ==0 and j==1:
                if grid[i][j] == grid[i][j+1]:
                    return False
                
                
            elif i ==1 and j==3:
                if grid[i][j] == grid[i+1][j]:
                    return False    
                
            elif i ==3 and j==1:
                if grid[i][j] == grid[i][j+1]:
                    return False            
                         
            #Checks all inner blocks and sees if there are any blocks that are the same around it
            
            elif (i==1 and j==1) or (i==1 and j==2) or (i==2 and j==1) or (i==2 and j==2) :
                
                if grid[i][j] == grid[i][j-1] or grid[i][j] == grid[i+1][j] or grid[i][j] == grid[i][j+1] or grid[i][j] == grid[i-1][j] :
                    return False
                        
    return True
    
        
    
#return True if a value>=32 is found in the grid; otherwise False   
def check_won(grid):
    
    for i in range(4):        
        for j in range(4):      
            if grid[i][j]>=32:             
                return True
    return False
            
            
            
#return a copy of the grid
def copy_grid(grid):
    copied_grid=[[],[],[],[]] 
    #put info from old grid to new one
    for i in range(4):        
        for j in range(4):            
            copied_grid[i].append(grid[i][j])
               
            
    return copied_grid
            

#check if 2 grids are equal - return boolean value
def grid_equal(grid1, grid2):
    
    for i in range(4):
        for j in range(4):
            if grid1[i][j] != grid2[i][j]:
                return False
            
    return True

                       
            
    
        
    
    
    
    
    
    
    
            


    
    
    
