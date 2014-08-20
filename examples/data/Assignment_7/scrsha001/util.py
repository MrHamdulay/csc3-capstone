# Shaaheen Sacoor SCRSHA001
#30 April 2014
# Programs that to be utilized for 2048 game

#Creating grid
def create_grid(grid):
    height =4
    for i in range(4):
        grid.append([0]*4)
    return grid
#Printing Grid
def print_grid(grid):
    print("+--------------------+")
    for y in range(4):
        for x in range(4):
            lnth = len(str(grid[y][x]))      #Works out how much space must be left
            ending = 5-lnth                  # between numbers. This is dependant on length
            if grid[y][x] ==0 :              #of number
                grid[y][x] = " "            #Changes 0 into space
            if x == 0:
                print("|",grid[y][x],end =" "*ending,sep="")     #Format of grid       
            elif x == 3:
                print(grid[y][x],"|",end ="",sep=" "*ending)
            else:
                print(grid[y][x],end=" "*ending)
        print()
    for y in range(4):
        for x in range(4): 
            if grid[y][x] ==" " : #Changes space back into 0
                grid[y][x] = 0      
    print("+--------------------+")
    
    #Checks if user has lost
def check_lost(grid):
    x= "STOP"
    for j in range(4):
        if 0 in grid[j]: #Goes through each line of grid to see if there is a space
            x= "carry on"
    if x =="carry on":
        return False     #if there isn't a space, user hasn't lost
    else:
        counter =0
        counter2 = 0
        for y in range(4): #Goes through each value on grid and looks for adjacent equal
            for x in range(3):    #values
                if grid[y][0] == grid[y][1] or grid[y][1] == grid[y][2] or grid[y][2] == grid[y][3]: 
                    counter +=1
                if grid[0][x] == grid[1][x] or grid[1][x] == grid[2][x] or grid[2][x] == grid[3][x]:
                    counter2 +=1
            if counter ==0 and counter2 ==0:
                return True
            else:
                return False
#Checks if user won            
def check_won(grid):
    for y in range(4):
        for x in range(4):
            if grid[y][x] ==" " :
                grid[y][x] = 0            
            if grid[y][x]>=32:
                return True
#            if grid[y][x] ==0 :
 #               grid[y][x] = " "             
                
    else:
        return False
    
    #Makes a deepcopy of grid
def copy_grid(grid):
    import copy
    global copygrid1
    copygrid1 = copy.deepcopy(grid)
    return copygrid1
#Checks if grids are equal so as to not add a new random number if grid doesn't move
def grid_equal(grid1,grid2):
    if grid1 == grid2:
        return True
    else :
        return False

