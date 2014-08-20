def create_grid(grid):
    for a in range (4):
       grid.append ([0] * 4)

def print_grid (grid):
   print ('+--------------------+') 
   for r in range (4):
      print ("|",end="") 
      for c in range (4):
          if grid[r][c] > 0:
              print ("{0:<5}".format (grid[r][c]), end="")
          else:
              print ("     ",end="")
      print ("|")      
   print ('+--------------------+') 

def check_lost (grid):
    for r in range (4):
        for c in range (4):
            if grid[r][c] == 0:
                return False
    for r in range (4):
        for c in range (3):
            if grid[r][c] == grid[r][c+1]:
                return False
            if grid[c][r] == grid[c+1][r]:
                return False
    return True            

def check_won (grid):
    for r in range (4):
        for c in range (4):
            if grid[r][c] >= 32:
                return True
    return False

def copy_grid (grid):
    new_grid = []
    for a in range (4):
       new_grid.append ([0] * 4)
    for r in range (4):
        for c in range (4):
            new_grid[r][c] = grid[r][c]
    return new_grid

def grid_equal (grid1, grid2):
    for r in range (4):
        for c in range (4):
            if grid1[r][c] != grid2[r][c]:
                return False
    return True    
