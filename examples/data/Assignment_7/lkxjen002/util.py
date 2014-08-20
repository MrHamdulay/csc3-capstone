#A program that manipulates a 2D array
#created by: Jenna Lake
#Date: 3 May 2014

def create_grid(grid):
    for i in range(4):
        grid.append(["0"]*4) #creates a 4 by 4 array filled with zeros
    
def print_grid(grid):
    print("+","-"*20,"+",sep="")
    for row in range(4):
        print("|",end="")
        for col in range(4):  
            if grid[row][col]==0: #makes sure that non-values/ zeros are not printed
                zero=" "
                print("{0:<5}".format(zero),sep="",end="")
            else:
                print("{0:<5}".format(grid[row][col]),sep="",end="")#formats grid such that the columns are width 5
            if col==3:
                print("|",end="")
        print()
    print("+","-"*20,"+",sep="")
def check_lost(grid):
    no_space=0
    count=0
    count1=0
    stop=False
    lost=True
    for row in range(4):
        for col in range(4):
            if grid[row][col]==0: #check if there are any white spaces, if any lost is straightaway false
                lost=False
                stop=True # no need to check whether adjacent blocks are equal, as already determined that lost is false
                
    if stop==False:   #only check if no 'spaces'         
        for row in range(4):
            for col in range(4):
                if row==3 and col==3: # no blocks below or to the right 
                    ignore=True
                elif row==3:
                    if grid[row][col]==grid[row][col+1]: 
                        lost=False
                        break
                elif col==3:
                    if grid[row][col]==grid[row+1][col]:
                        lost=False
                        break
                else:
                    if grid[row][col]==grid[row+1][col] or grid[row][col]==grid[row][col+1]:#work through grid checking block below and to the right
                        lost=False
                        break      
    return lost #retruns true or false
            
def check_won(grid):
    check_won=False
    for row in range(4):
        for col in range(4):
            if int(grid[row][col])>=32: # won if any value in grid is greater or equal to 32
                check_won=True
                break
    return check_won #retruns true or false

def copy_grid(grid):
    test_grid=[] #copys the original grid to a new grid, number by number(nested loops)
    appendable_grid=[]
    for row in range(4):
        appendable_grid=[] 
        for col in range(4):
            appendable_grid.append(grid[row][col]) #in each col a sub grid is created which is appended to test_grid in each row
        test_grid.append(appendable_grid)
    
    return test_grid

def grid_equal(grid1,grid2):
    equal=False
    count1=0
    for row in range(4):
        for col in range(4):
            if grid1[row][col]==grid2[row][col]: #compares the value with the corresponding index in the two grids
                count1+=1
    if count1==16: # if all of them are equal there will be 16 equal values
        equal=True
    return equal