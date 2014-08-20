def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0,0,0,0])
    return grid
        

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    count = 0
    print("+--------------------+")
    for i in grid:
        for j in range(4):
            if((j == 0)):
                if((i[j] != 0)):
                    print("|",i[j]," "*(5-len(str(i[j]))),sep="", end="")
                else:
                    print("|"," "*(5),sep="", end="")                
            elif((j==3)):
                if((i[j] != 0)):
                    print(i[j]," "*(5-len(str(i[j]))),"|",sep="", end="")
                else:
                    print(" "*(5),"|",sep="", end="")
            elif((i[j] != 0)):
                print(i[j]," "*(5-len(str(i[j]))),sep="", end="")
            else:
                print(" "*(5),sep="", end="")
        print()
        count += 1
    print("+--------------------+")
        

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""

    numZeroEqual = 0
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if((row == 0) and (column == 0)):
                if((grid[row][column] == grid[row+1][column]) or (grid[row][column] == grid[row][column+1])):
                    numZeroEqual +=1
            elif((row == 3) and (column == 0)):
                if((grid[row][column] == grid[row][column+1])or(grid[row][column] == grid[row-1][column])):
                    numZeroEqual +=1
            elif((row == 0) and (column == 3)):
                if((grid[row][column] == grid[row][column-1])or(grid[row][column] == grid[row+1][column])):
                    numZeroEqual +=1
            elif((row == 3) and (column == 3)):
                if((grid[row][column] == grid[row][column-1])or(grid[row][column] == grid[row-1][column])):
                    numZeroEqual +=1
            elif(row == 0):
                if((grid[row][column] == grid[row][column-1])or(grid[row][column] == grid[row+1][column])or(grid[row][column] == grid[row][column+1])):
                    numZeroEqual +=1       
            elif(row == 3):
                if((grid[row][column] == grid[row-1][column])or(grid[row][column] == grid[row][column-1])or(grid[row][column] == grid[row][column+1])):
                    numZeroEqual +=1      
            elif(column == 0):
                if((grid[row][column] == grid[row-1][column])or(grid[row][column] == grid[row+1][column])or(grid[row][column] == grid[row][column+1])):
                    numZeroEqual +=1
            elif(column == 3):
                if((grid[row][column] == grid[row][column-1])or(grid[row][column] == grid[row+1][column])or(grid[row][column] == grid[row-1][column])):
                    numZeroEqual +=1
            else:
                if((grid[row][column] == grid[row][column-1])or(grid[row][column] == grid[row][column+1])or(grid[row][column] == grid[row-1][column])or(grid[row][column] == grid[row+1][column])):
                    #print("    ",grid[row-1][column],"    ","\n",grid[row][column-1]," ",grid[row][column]," ", grid[row][column+1]," \n   ",grid[row+1][column])
                    numZeroEqual +=1                
            
        
                    
            #if(r!=row): 
                #if(grid[row][column] == grid[r][column]):
                    #numZeroEqual +=1
                    
            if(grid[row][column] ==0):
                numZeroEqual +=1
                

                    
    if(numZeroEqual > 0):
        return False
    else:
        return True


def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    found = False
    for column in range(len(grid)):
        for row in range(len(grid[column])):
            if(grid[column][row] >= 32):
                found = True
                
    return found
                

def copy_grid (grid):
    """return a copy of the grid"""
    newGrid =[]
    for column in range(len(grid)):
        newGrid.append([0,0,0,0])
        for row in range(len(grid[column])):
            newGrid[column][row] = grid[column][row]
            
    return newGrid        
        

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    equal = True
    for row in range(len(grid1)):
        for column in range(len(grid1[row])):
            if(grid1[row][column] != grid2[row][column]):
                return False
    return equal
    
#x = create_grid([])
#print_grid (x)
#grid = [[4,2,8,2],[2,8,16,8],[16,32,8,4],[4,8,4,2]]
#print(check_lost(grid))