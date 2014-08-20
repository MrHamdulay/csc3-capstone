### Tashiv Sewpersad (SWPTAS001)
### Assignment 7 - Question 2
### 01-05-2014

## Decalarations
def create_grid(grid): 
  """create a 4x4 grid"""
  for i in range(4):
    Row = []
    for j in range(4):
      Row.append(0)
    grid.append(Row)

def print_grid (grid):
  """print out a 4x4 grid in 5-width columns within a box"""
  sBorder = "+--------------------+"
  form = "{0:<5}"
  print(sBorder)
  for y in grid:
    print("|",end="")
    for x in y:
      if x != 0:
        print(form.format(x),end="") # formats into coloumns
      else:
        print(form.format(""),end="") # prints a blank where there is a zero
    print("|")
  print(sBorder)

def check_lost (grid):
  """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
  # Checks for zeros
  for y in grid:
    if 0 in y:
      return False
  # Checks for adjacent values that are the same    
  for y in range(3): # runs to 2 as it compares n to n+1 for better effeciency
     for x in range(3):
        if grid[y][x] == grid[y][x+1]: # checks horizontally adjacent
          return False
        elif grid[y][x] == grid[y+1][x]: # checks vertically adjacent
          return False
  return True
  
def check_won (grid):
  """return True if a value>=32 is found in the grid; otherwise False"""
  for y in grid:
    if max(y) >= 32: # checks only the max value of each row against >=32
      return True
  return False

def copy_grid (grid):
  """return a copy of the grid"""
  NewGrid = []
  # Must be done to create a new grid in memory
  for y in grid:
    row = []
    for x in y:
      row.append(x)
    NewGrid.append(row)
  return NewGrid

def grid_equal (grid1, grid2):
  """check if 2 grids are equal - return boolean value"""
  # Checks Corresponding elements in both grids
  for y in range(4):
    for x in range(4):
      if grid1[y][x] != grid2[y][x]:
        return False
  return True