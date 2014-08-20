"""QUESTION 3, Assignment 7
Charlie Shang
SHNHUA002"""

def push(Tgrid): #this function is called by the other push_x() functions. The calling function will reorder the original grid in such a way that when the grid is "shifted to the left" in this function, and then returned to the calling function, it can be reordered in such a way that the intended direction of shift is reflected.

    """called by other push_x() functions to remove repeated code"""
    grid = Tgrid
    #Remove all zeroes before any numbers. "NumZeroes" counts the number of zeroes deleted and allows the loop to "step one back", since when the 0 is deleted, the values in the list shifts
    NumZeroes = 0
   
    for k in range(3):
       
        if grid[k-NumZeroes] == 0:
            del grid[k-NumZeroes]            
            grid.append(0) #puts the deleted zero back the the end of the list
            NumZeroes += 1
   
    #adding the equal numbers and storing the result in the foremost block
    for num in range(3):
            
            if grid[num] == grid[num+1]:
                grid[num] = grid[num]+grid[num+1]                
                del grid[num+1]
                grid.append(0)
   
    return grid

def push_up(grid):
    """Function to merge grid values upwards."""
    #Extract each column's values and stores them in the temp variable: "column."
    for x in range(4):
        
        column = []
        
        for y in range(4):
            column.append(grid[y][x])
        
        column = push(column)
       
        #replace the columb back into the original grid
        for y in range(4):
            grid[y][x] = column[y]
            
def push_down(grid):
    """Function to merge grid values downwards."""
    #same as push_up but the list is reversed before and then after being processed.
    for x in range(4):
        column = []
        
        for y in range(4):
            column.append(grid[y][x])
        
        column.reverse()
        column = push(column)
        column.reverse()
        
        for y in range(4):
            grid[y][x] = column[y]

def push_left(grid):
    """Function to merge grid values left."""
    #extract each row's values and places them in the temp variable "row"
    for y in range(4): 
        row = []
        
        for x in range(4):
            row.append(grid[y][x])
        row = push(row)
            
        for x in range(4):
            grid[y][x] = row[x]
            
def push_right(grid):
    #same as push_left() but the list is reversed before and after being processed
    """Function to merge grid values right."""
    for y in range(4):
        row = []
        
        for x in range(4):
            row.append(grid[y][x])
        
        row.reverse()
        row = push(row)
        row.reverse()
        
        for x in range(4):
            grid[y][x] = row[x]