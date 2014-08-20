def shiftUL(grid):
     x = []
     s = 0
     while s != 4:
          if grid[s] != 0:
               x.append(grid[s])
          else:
               None
               
          s += 1
     while len(x) != 4:
          x.append(0)
     for i in range(len(grid)):
          grid[i] = x[i]

def shiftDR(grid):
     x = []
     s = 3
     while s != -1:
          if grid[s] != 0:
               x.append(grid[s])
          else:
               None
               
          s -= 1
     x.reverse()     
     while len(x) != 4:
          x.append(0)
     x.reverse()     
     for i in range(len(grid)):
          grid[i] = x[i]
     
     

def mergeUL(grid):
     x = []
     shiftUL(grid)
     for i in range(len(grid)):
          if i+1 < len(grid):
               if grid[i] == grid[i+1]:
                    x.append(2*grid[i])
                    grid[i+1] = 0
               else:
                    x.append(grid[i])
                    if i == 2:
                         if grid[3] != 0:
                              x.append(grid[3])
               
     
     while len(x) != 4:
          x.append(0)
     for j in range(len(grid)):
          grid[j] = x[j]
     shiftUL(grid)
     
def mergeDR(grid):
     x = []
     shiftDR(grid)
     for i in [3,2,1,0]:
          if i-1 < len(grid):
               if grid[i] == grid[i-1]:
                    x.append(2*grid[i])
                    grid[i-1] = 0
               else:
                    x.append(grid[i])
                    if i == 1:
                         if grid[0] != 0:
                              x.append(grid[0])
                                   
     
     while len(x) != 4:
          x.append(0)
     x.reverse()     
     for j in range(len(grid)):
          grid[j] = x[j]
     shiftDR(grid)     
 
          