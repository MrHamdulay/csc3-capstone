#code for 2048 game
#F.J.Chigwaza
#02 April 2014

#merging grid values upwars
def push_up (grid):
    
    for row in range (4):
        for column in range (4):
            
            if grid[row][column]==' ':
                grid[row][column]=0
                cell=grid[row][column]
                
                num_row = row
                while num_row >3:
                    num_row +=1
                    
                    if grid[num_row][column]==0:
                        grid[num_row]=cell
                        grid[num_row-1][column]=0
                        
                    else:
                        if cell== grid[num_row][column]:
                            grid[num_row][column] += cell
                            grid[num_row-1][column]=0
                    
                
            
#merging grid values downwards
def push_down (grid):
    
    for row in range (4):
        for column in range (4):
            
            if grid[row][column]==' ':
                grid[row][column]=0
                cell=grid[row][column]
                               
                num_row = row
                while num_row >3:
                    num_row +=1
                                   
                    if grid[num_row][column]==0:
                        grid[num_row]=cell
                        grid[num_row-1][column]=0
                                       
                    else:
                        if cell== grid[num_row][column]:
                            grid[num_row][column] -= cell
                            grid[num_row-1][column]=0                
                