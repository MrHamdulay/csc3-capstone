"""Name: Sibulele Hlongwane
Date: 1 May 2014
My failed attempt at a Simulation of 2048"""
import util
def push_up(grid):
    """merge grid with values upwards"""
def push_down(grid):
    """merge grid values downwards"""
def push_left(grid):
    """merge grid values left"""
    count=0
    for row in range(4):      
            for col in range(3):  
               
                    block= grid[row][col]
                    if block!= 0:
                        #if adjacent block equals current block
                            if (grid[row][col+1]==grid[row][col]):
                                #newblock is equal to the combination of the blocks
                                    newblock= (grid[row][col+1]+grid[row][col])
                                    position=grid[row][col]
                                    #make old blocks equal to 0
                                    grid[row][col]=0
                                    grid[row][col+1]=0
                                    for column in range(4):
                                            if grid[row][column]==0:
                                                    zeropos=column
                                                    break
                                    grid[row][column]=newblock
                    
            else:
                    for col in range(4):
                      #counts the number of zero's
                            if grid[row][col]==0:
                                    count=count+1
                                    break
                                
                    if grid[row][col+1]==0:
                            count=count+1
                            if grid[row][col+2]==0:
                                    count=count+1
                        #current block equals adjacent values
                    grid[row][col]=grid[row][col+count]
                    grid[row][col+count]=0
                    count=0
                    #same as top, which merges adjacent values after they have been shifted
                    for col in range(3):  
                            block= grid[row][col]
                            if block!= 0:
                                    if (grid[row][col+1]==grid[row][col]):
                                            newblock= (grid[row][col+1]+grid[row][col])
                                            position=grid[row][col]
                                            grid[row][col]=0
                                            grid[row][col+1]=0
                                            for column in range(4):
                                                    if grid[row][column]==0:
                                                            zeropos=column
                                                            break
                                            grid[row][column]=newblock
                    
    
                
                    
                    
                    
    util.print_grid(grid)               
                
def push_right(grid):
    """merge grid values right"""
