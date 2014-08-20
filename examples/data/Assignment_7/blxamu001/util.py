def create_grid(grid):
    
    for i in range(4):
        grid.append([0]*4)
    return grid
    #print(grid)
       
    ##for i in range(4):
        ##for j in range(4):
            ##x += str(grid[i][j])
            
        ##print()

def print_grid(grid):
    
    
    print('+','-'*20,'+', sep='')
    for i in range(4):
        a = ' '
        print('|', end="")
        for j in range(4):     
            if grid[i][j] == 0:
                print("{:<5}".format(a), end="")
            else:
                print("{:<5}".format(grid[i][j]), end="")                
        print('|', end="")
        print()
    print('+','-'*20,'+', sep='')

def check_lost(grid):
	
	for d in range(4):
		
		for a in range(4):
			
			if grid[d][a] == 0:
				return(False)
			
			if a>0:
				if grid[d][a] == grid[d][a-1]:
					return(False)
			
			if d>0:
				if grid[d][a] == grid[d-1][a]:
					return(False)
	return(True)

#def check_lost (grid):
    #for i in range(4):
        #for j in range(4):
            #if grid[i][j] == 0:
                #return False
            #if i - 1 > 0 and i + 3 < 4 and j - 1>= 0 and j + 3<4:
                #if grid[i][j] != grid[i][j-1] and grid[i][j] != grid[i][j+1] and grid[i][j] != grid[i-1][j] and grid[i][j] != grid[i+1][j]:
                    #return True
            #else:
                #return False
                #elif grid[i][j] == grid[i][j+1]:
                   # return False
               # elif grid[i][j] == grid[i-1][j]:
                #    return False
                #elif grid[i][j] == grid[i+1][j]:
                 #   return False
            #if j - 1>= 0 and j + 3<4:
                #if grid[i][j] == grid[i-1][j]:
                    #return False
                #elif grid[i][j] == grid[i+1][j]:
                    #return False
    #return True

def check_won(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j]>=32:
                return True
    return False

def copy_grid(grid):
    return grid


def grid_equal(grid1,grid2):
    for i in range(4):
        for j in range(4):
            if grid1[i][j] != grid2[i][j]:
                return False
    return True