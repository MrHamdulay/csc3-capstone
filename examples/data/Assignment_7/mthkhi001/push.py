#MTHKHI001
#ASSIGNMENT 7
#QUESTION 3 PUSH.PY



def push_up (grid):
        
    count = 4
    for j in range (3):
        count = count - 1
        for m in range (4):
            if grid[count][m] == grid[count - 1][m]:
                grid[count-1][m] = grid[count][m] + grid[count-1][m]
                
                grid[count][m] = 0
            
            if grid[count -1][m] == 0:
                grid[count -1][m] = grid[count][m]
                grid[count][m] = 0
                


                