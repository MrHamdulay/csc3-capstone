#GLNRUS002
#Assignment 7
#Question 2
# 30 April 2014

def create_grid(grid):
    """create a 4x4 grid"""
    tmp_grid=[]
    for i in range (4):#create one dimensioanl array
        grid.append([0,0,0,0])

    return grid

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""#format
    count=0
    print("+--------------------+")
    for i in grid:
        print("|",end="")
        for j in grid[count]:
            if j==0:
                print("{0:<5}".format(""),end="")
            else:
                print("{0:<5}".format(j),end="")
        print("|")
        count+=1
    print("+--------------------+")

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    check =True#used to test all criterion
    
    zero=0#used to count amount of zeros
    for i in grid:#counts through arrays
        for j in i:#counts through single array
            if j==0:#if value in array=0
                zero+=1#add to mount of zeros
    if zero!=0:#if zeros were found
        check =False
##################################################################################check that adjacent values are not EQUAL      
    array_count=0  
    for i in grid:
        
        for j in i:#counts through values in single array
            count=0
            tmp_grid=i #used for doing operations on just a one dimensional array           
            j_position=count#find position of j in list being worked with
      
            if j_position==1 or j_position==2:#test beow can only fully be done if j value has values on either side
                if tmp_grid[j_position-1]==tmp_grid[j_position] or tmp_grid[j_popsition]==tmp_grid[j_position+1]:
                    check=False
            elif j_position==0:#position of j on left border
                if tmp_grid[j_position]==tmp_grid[j_position+1]:
                    check=False
            elif tmp_grid[jposition]==tmp_grid[jposition-1]:#border right as theres no other option
                    check=False
            count+=1
       
        array_count+=1
##################################################################################           
    return check

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for i in grid:
        for j in i:
            if j>=32:
                return True
    return False
            
def copy_grid (grid):###
    """return a copy of the grid"""
    copy_of_grid=[[],[],[],[]]
    count=0
    for i in grid:
        lim=i
        counter=0
        for j in range(4):
            copy_of_grid[count].insert(counter,lim[j])
            counter+=1
        count+=1
    return copy_of_grid

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1==grid2:
        return True
    else:
        return False
    