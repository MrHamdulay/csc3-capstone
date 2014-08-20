#Asil Motala
#MTLASI002
#Assignment 7
#Question 2
#27 April 2014

def create_grid(grid):
    for i in range(4):                          #loop through the vertical/first array
        grid.append([0,0,0,0])                  #add an array to each index of the first array
    return grid                                 #return two dimensional array

def print_grid (grid):
    print("+--------------------+")             #print top of box
    for i in range(4):                          #loop through each row
        string="|"                              #add box beginning to row
        for j in range(4):                      #loop through each column
            value=str(grid[i][j])               #convert integer value to string
            if value=='0':
                value=" "                       #print blank space in place of zero
            string+=value+" "*(5-(len(value)))  #add value from list to column of 5 width
        string+="|"                             #add box end to row
        print(string)                           #print each row
    print("+--------------------+")             #print bottom of box

def check_lost (grid):
    for i in range(4):                          #loop through rows
        for j in range(4):                      #loop through columns
            if grid[i][j]==0:                   #check for value of 0
                return False
        for k in range(3):
            if grid[i][k]==grid[i][k+1] or grid[k][i]==grid[k+1][i]:    #check if adjacent values are equal
                return False
    else: return True                           #return true if loop completes itself

def check_won (grid):
    for i in range(4):                          #loop through rows
        for j in range(4):                      #loop through columns
            if grid[i][j]>=32:                  #check if value is greater than 32
                return True                     #return boolean true
    else: return False                          #return boolean false if loop completes itself
    
def copy_grid(grid):
    for i in range(4):                          #loop through each row
        for j in range(4):                      #loop through each column
            grid[i][j]=str(grid[i][j])          #convert each value to string(for string manipulation)
    for k in range(4):                          #loop through each index of outer list
        grid[k]="/".join(grid[k])               #join each small list into a string
    string="*".join(grid)                       #join 4 strings into one big string
    grid_copy=string.split("*")                 #grid_copy is now a copy, but in string
    for l in range(4):
        grid_copy[l]=grid_copy[l].split('/')    #split back into 4 strings
    for m in range(4):
        for n in range(4):                      #split back into 4 lists
            grid_copy[m][n]=eval(grid_copy[m][n])
    for h in range(4):
        grid[h]=grid[h].split('/')              #split back intro 4 strings
    for p in range(4):
        for t in range(4):                      #spplit back into 4 lists
            grid[p][t]=eval(grid[p][t])         #ensures grid(original) remains unchanged
    return grid_copy                            #return the copy of the grid

def grid_equal (grid1, grid2):
    if grid1==grid2:                            #check if two grids are identical
        return True
    else:
        return False