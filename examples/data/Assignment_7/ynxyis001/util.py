#2048 functions
#Jennifer Yuan (YNXYIS001)
#2 May 2014

def create_grid(grid): #creates an empty 4x4 grid
          for i in range(4): #rows
                    temp =[] #empty dtring
                    for j in range(4): #columns
                              temp.append(0) #inputs 0 as value in list (temp)
                    grid.append(temp) #adds temp to grid to create a 2D list 
          return grid

def print_grid(grid): #prints out a 4x4 grid in 5-width columns within a box
          print("+--------------------+") #border
          for i in range(4): #rows
                    print("|", end="")
                    for j in range(4): #columns
                              if str(grid[i][j]) == "0": #if the value is 0, it prints 5 spaces to keep column widths = 5
                                        print(" "*5, end="") #end ="" makes the values stay on the same line
                              else:
                                        print("{0:<5}".format(str(grid[i][j])), end="") #if the value is not 0, then it formats the grid
                                                                                                    
                    print("|")
          print("+--------------------+") #border

def check_lost(grid): #returns True if there are no 0 values and no adjacent values that are equal
          for i in range(4): #row
                    for j in range(4): #column
                              if str(grid[i][j]) == "0":
                                        return False
                              elif j+1< 4 and str(grid[i][j]) == str(grid[i][j+1]): #checks that there are no identical values to the right of any value
                                        return False
                              elif i+1<4 and str(grid[i][j]) == str(grid[i+1][j]):
                                        return False #checks that there are no identical values right below any value
          return True

def check_won(grid): #Returns true if a value > = 32 is found in the grid, else False
          for i in range(4): #row
                    for j in range(4): #column
                              if grid[i][j] >= 32:
                                        return True
          return False

def copy_grid(grid): #creates a copy of the grid
          grid2 = [] #empty string
          for i in range(4): #row
                    temp =[] #empty string
                    for j in range(4): #column
                              temp.append(grid[i][j]) #adds respective value in original grid to new one
                    grid2.append(temp) #adds 1D list to grid2 to create a 2D grid
          return grid2
          
def grid_equal(grid1, grid2): #checks if 2 grids are equal and returns True if they are. 
          if grid1 == grid2: 
                    return True
          return False
                                        
          

         
