#==============================================================================

#create grid (0)
def create_grid(grid):
    for k in range(4):
        grid.append ([0] * 4)
#==============================================================================        
        
#Print Grid (1-2)
def print_grid (grid):
    
    print('+', '-' *(5*4), '+', sep = '')
    
    arrHold = []
    
    for row in range(4):
        for col in range(4):
            hold = grid[row][col]
            arrHold.append(hold)
            string = ''
        
        #print('|', arrHold[0], ' ' * 4, arrHold[1], ' ' * 4,arrHold[2], ' ' * 4,arrHold[3], ' ' * 4, '|', sep = '')
        
        for k in range(4):
            now = str(arrHold[k])

            if now == '0':
                now = ' '            

            length = 5 - len(now)
            now = now + (' ' * length)
            
            string += now
            
        print('|', string, '|', sep = '')      
        
        arrHold = []
        
    
    print('+', '-' *(5*4), '+', sep = '')

#==============================================================================

#Check lost (3-7)    
def check_lost (grid):
    #Check Zeros
    zero = 'False'
    
    for row in range(4):
        for col in range(4):
            if grid[row][col] == 0:
                zero = 'True'
                break
            
    #Check Left/Right Adjacent
    LRAdj = 'False'
    
    for row in range(4):
        for col in range(1, 4):
            if grid[row][col] == grid[row][col - 1]:
                LRAdj  = 'True'
                break
            
    #Check Up/Down Adjacent
    UDAdj = 'False'
    
    for col in range(4):
        for row in range(1, 4):
            if grid[row][col] == grid[row - 1][col]:
                UDAdj = 'True'
                break
            
    if (zero == 'True') or ((LRAdj == 'True') or (UDAdj == 'True')):
        win = 'False'
    
    else: win = 'True'
    
    return win
                
            
#==============================================================================
    
# Check Won (8-16)
def check_won (grid):
    found = 'False'
    
    for row in range(4):
        for col in range(4):
            if grid[row][col] >= 32:
                found = 'True'
                break
    return found


#==============================================================================

#Copy Grid (17)
def copy_grid (grid):
    arrNew = []
    for i in range (4):
        arrNew.append ([0] * 4)
        
    for row in range(4):
        for col in range(4):
            hold = grid[row][col]
            arrNew[row][col] = hold
    
    return arrNew
             
#=============================================================================

#Grid Equal (18-22)
def grid_equal (grid1, grid2):
    equal = 'True'
    
    for row in range(4):
        for col in range(4):
            
            if grid1[row][col] != grid2[row][col]:
                equal = 'False'
                break
            
    return equal

#==============================================================================
#==============================================================================
#==============================================================================

#The Following is all my Tracing steps. Helped me to see how I got all my answers and the correct (hypothetical) output before putting it into the functions

'''# create 2d array
arrX = []
for i in range (4):
    arrX.append ([0] * 4)

# populate array with fill values
for row in range (4):
    for col in range (4):
        arrX[row][col] = row + col
        
print(arrX)
print()

arrHold = []

print('+', '-' *(5*4), '+', sep = '')

for row in range(4):
    for col in range(4):
        hold = arrX[row][col]
        arrHold.append(hold)
        string = ''
    
    #print('|',arrHold[0], ' ' * 4, arrHold[1], ' ' * 4,arrHold[2], ' ' * 4,arrHold[3], ' ' * 4, '|', sep = '')
    
    for k in range(4):
        now = str(arrHold[k])
        
        if now == '0':
            now = ' '
        
        length = 5 - len(now)
        now = now + (' ' * length)
        
        string += now
        
    print('|', string, '|', sep = '')
    
    arrHold = []
    
print('+', '-' *(5*4), '+', sep = '')


print()
print()
print()


arrNew = []
for i in range (4):
    arrNew.append ([0] * 4)
    
for row in range(4):
    for col in range(4):
        hold = arrX[row][col]
        arrNew[row][col] = hold

print(arrNew)'''