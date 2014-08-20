'''This module  completes the code for a 2048 program, using the utility module
Sandile Christopher Mahlangu
1 May 2014'''

def push_up (grid):
    """This fumction merges grid values upwards"""
    for col in range (len(grid)):
        for row in range (len(grid)):
            if col==0:#Looking at the first row 
                #if this block is equal to the block below then add them together
                if grid[col][row]==grid[col+1][row]:
                    grid[col][row]*=2
                    grid[col+1][row]=0
                #If the one below it is equal to zero then check if the 3rd block is equal to it, if so then add them
                elif grid[col+1][row]==0 and grid[col][row]==grid[col+2][row]:
                    grid[col][row]*=2
                    grid[col+2][row]=0
                #if the second and third are empty and the 4th one is eqaul to the current one then add them
                elif grid[col+1][row]==0 and grid[col+2][row]==0 and grid[col][row]== grid[col+3][row]:
                    grid[col][row]*=2
                    grid[col+3][row]=0
            elif col==1:
                #Looking at the second row
                #if this block is equal to the block below then add them together
                if grid[col][row]==grid[col+1][row]:
                    grid[col][row]*=2
                    grid[col+1][row]=0                
                #If the one below it is equal to zero then check if the 4th block is equal to it, if so then add them
                elif grid[col+1][row]==0 and grid[col][row]==grid[col+2][row]:
                    grid[col][row]*=2
                    grid[col+2][row]=0
                #Check if the one obove it is zero if so move it to that position
                if grid[col-1][row]==0:
                    grid[col-1][row]=grid[col][row]
                    grid[col][row]=0
            elif col ==2:
                #Looking at the third row
                #if this block is equal to the block below then add them together
                if grid[col][row]==grid[col+1][row]:
                    grid[col][row]*=2
                    grid[col+1][row]=0 
                if grid[col-1][row]==0:#if the block above is = 0
                    #if the first one is also = 0 then move this one there
                    if grid[col-2][row]==0:
                        grid[col-2][row] = grid[col][row]
                        grid[col][row]=0
                    else:
                        #if the first one is not 0 the move it to the second one
                        grid[col-1][row]=grid[col][row]
                        grid[col][row]=0
            elif col==3: #Looking at the last row
                #check if the above row is 0 
                if grid[col-1][row]==0:
                    if grid[col-2][row]==0 and grid[col-3][row]==0: #If the fist and second row is equal to zero then move it to the first row
                        grid[col-3][row]=grid[col][row]
                        grid[col][row]=0
                    elif grid[col-2][row]==0: #If the second row is empty then move it to the second row
                        grid[col-2][row]=grid[col][row]
                        grid[col][row]=0
                    else: #Otherwise move it to the above row
                        grid[col-1][row]=grid[col][row]
                        grid[col][row]=0
                        
                        
    return grid


def push_down (grid):
    """This function merges grid values downwards"""
    #I'm gonna start the loop from the rows at the bottom 
    for col in range(len(grid)-1,-1,-1):
        for row in range(len(grid)):
            if col ==3: #if it's the bottom part
                if grid[col][row]==grid[col-1][row]: #If this row is equal to the above on the add them
                    grid[col][row]*=2
                    grid[col-1][row]=0
                elif grid[col-1][row]==0 and grid[col][row]==grid[col-2][row]: #If the one above is zero and the second one is equal to this one we add them
                    grid[col][row]*=2
                    grid[col-2][row]=0
                elif grid[col-1][row]==0 and grid[col-2][row]==0 and grid[col][row]==grid[col-3][row]: #If the one above is zero and the second one is also zero and the top one is equal to this one add them
                    grid[col][row]*=2
                    grid[col-3][row]=0
            elif col ==2: #Looking at the second row from the bottom
                if grid[col][row]== grid[col-1][row]: #if the above row is equal to this one add them
                    grid[col][row]*=2
                    grid[col-1][row]=0
                elif grid[col-1][row]==0 and grid[col][row]==grid[col-2][row]: #If the above grid is zero and the first grid is equal to this one add them
                    grid[col][row]*=2
                    grid[col-2][row]=0 
                if grid[col+1][row]==0: #if the grid below is empty then move this grid to that one
                    grid[col+1][row]=grid[col][row]
                    grid[col][row]=0
            elif col == 1 : #Checking the second row
                #Check if the above row is equal to this one, if so add them
                if grid[col][row]==grid[col-1][row]:
                    grid[col][row]*=2
                    grid[col-1][row]=0
                if grid[col+1][row]==0: #Check if the row below is zero
                    if grid[col+2][row]==0:#If the last one is also zero , move the current to the last one
                        grid[col+2][row]=grid[col][row]
                        grid[col][row]=0
                    else:#Otherwise move it to the one below
                        grid[col+1][row]=grid[col][row]
                        grid[col][row]=0
            elif col==0:#Looking at the first row
                if grid[col+1][row]==0: #If the row below is empty
                    if grid[col+2][row]==0 and grid[col+3][row]==0:#if all rows below are empty then move it below to the last one
                        grid[col+3][row]=grid[col][row]
                        grid[col][row]=0
                    elif grid[col+2][row]==0: #If the 3rd row is empty move it to this row:
                        grid[col+2][row]=grid[col][row]
                        grid[col][row]=0
                    else: #Otherwise move it to the one below
                        grid[col+1][row]=grid[col][row]
                        grid[col][row]=0
    
                        
    return grid
def push_left (grid):
    """This function merges grid values left"""
    for col in range (len(grid)):
        for row in range (len(grid)):
            if row==0:#Looking at the first column 
                #if this block is equal to the block on the right then add them together
                if grid[col][row]==grid[col][row+1]:
                    grid[col][row]*=2
                    grid[col][row+1]=0
                #If the one after it is equal to zero then check if the 3rd block is equal to it, if so then add them
                elif grid[col][row+1]==0 and grid[col][row]==grid[col][row+2]:
                    grid[col][row]*=2
                    grid[col][row+2]=0
                #if the second and third are empty and the 4th one is eqaul to the current one then add them
                elif grid[col][row+1]==0 and grid[col][row+2]==0 and grid[col][row]== grid[col][row+3]:
                    grid[col][row]*=2
                    grid[col][row+3]=0
            elif row==1:
                #Looking at the second column
                #if this block is equal to the block after then add them together
                if grid[col][row]==grid[col][row+1]:
                    grid[col][row]*=2
                    grid[col][row+1]=0                
                #If the one after it is equal to zero then check if the 4th block is equal to it, if so then add them
                elif grid[col][row+1]==0 and grid[col][row]==grid[col][row+2]:
                    grid[col][row]*=2
                    grid[col][row+2]=0
                #Check if the one behind it is zero if so move it to that position
                if grid[col][row-1]==0:
                    grid[col][row-1]=grid[col][row]
                    grid[col][row]=0
            elif row ==2:
                #Looking at the third column
                #if this block is equal to the block after it then add them together
                if grid[col][row]==grid[col][row+1]:
                    grid[col][row]*=2
                    grid[col][row+1]=0 
                if grid[col][row-1]==0:#if the block behind is = 0
                    #if the first one is also = 0 then move this one there
                    if grid[col][row-2]==0:
                        grid[col][row-2] = grid[col][row]
                        grid[col][row]=0
                    else:
                        #if the first one is not 0 the move it to the second one
                        grid[col][row-1]=grid[col][row]
                        grid[col][row]=0
            elif row==3: #Looking at the last column
                #check if the behind row is 0 
                if grid[col][row-1]==0:
                    if grid[col][row-2]==0 and grid[col][row-3]==0: #If the fist and second col is equal to zero then move it to the first col
                        grid[col][row-3]=grid[col][row]
                        grid[col][row]=0
                    elif grid[col][row-2]==0: #If the second col is empty then move it to the second 
                        grid[col][row-2]=grid[col][row]
                        grid[col][row]=0
                    else: #Otherwise move it to one behind
                        grid[col][row-1]=grid[col][row]
                        grid[col][row]=0
                        
                        
    return grid

def push_right (grid):
    """merge grid values right"""  
    #I'm gonna start the loop from the columns for the right
    for col in range(len(grid)):
        for row in range(len(grid)-1,-1,-1):
            if row ==3: #if it's the right part
                if grid[col][row]==grid[col][row-1]: #If this col is equal to the behind one the add them
                    grid[col][row]*=2
                    grid[col][row-1]=0
                elif grid[col][row-1]==0 and grid[col][row]==grid[col][row-2]: #If the one behind is zero and the second one is equal to this one we add them
                    grid[col][row]*=2
                    grid[col][row-2]=0
                elif grid[col][row-1]==0 and grid[col][row-2]==0 and grid[col][row]==grid[col][row-3]: #If the one behind is zero and the second one is also zero and the top one is equal to this one add them
                    grid[col][row]*=2
                    grid[col][row-3]=0
            elif row ==2: #Looking at the second col from the left
                if grid[col][row]== grid[col][row-1]: #if the behind col is equal to this one add them
                    grid[col][row]*=2
                    grid[col][row-1]=0
                elif grid[col][row-1]==0 and grid[col][row]==grid[col][row-2]: #If the behind grid is zero and the first grid is equal to this one add them
                    grid[col][row]*=2
                    grid[col][row-2]=0 
                if grid[col][row+1]==0: #if the grid infront is empty then move this grid to that one
                    grid[col][row+1]=grid[col][row]
                    grid[col][row]=0
            elif row == 1 : #Checking the second col
                #Check if the behind col is equal to this one, if so add them
                if grid[col][row]==grid[col][row-1]:
                    grid[col][row]*=2
                    grid[col][row-1]=0
                if grid[col][row+1]==0: #Check if the col infront is zero
                    if grid[col][row+1]==0 and grid[col][row+2]==0:#If the last one is also zero , move the current to the last one
                        grid[col][row+2]=grid[col][row]
                        grid[col][row]=0
                    elif grid[col][row+1]==0:#Otherwise move it to the one infront
                        grid[col][row+1]=grid[col][row]
                        grid[col][row]=0
            elif row==0:#Looking at the first col
                if grid[col][row+1]==0: #If the col infront is empty
                    if grid[col][row+2]==0 and grid[col][row+3]==0:#if all cols infront are empty then move it  to the last one
                        grid[col][row+3]=grid[col][row]
                        grid[col][row]=0
                    elif grid[col][row+2]==0: #If the 3rd col is empty move it to this row:
                        grid[col][row+2]=grid[col][row]
                        grid[col][row]=0
                    elif grid[col][row+1]==0: #Otherwise move it to the one infront
                        grid[col][row+1]=grid[col][row]
                        grid[col][row]=0
    
                        
    return grid