# Author : Rayaan Fakier FKRRAY001
# Date : 13 - 05 - 2014
# question3.py

def create_grid():
    '''Function which creates the 2D array containing Sudoku values'''
    # Creates 'empty' 2D array
    grid = []
    for grid_blocks in range(9):
        grid.append([0]*9)
    
    # Takes sudoku grid as user-input and creates a grid
    ask = 0
    while ask < 9:
        val = input()
        for k in range(9):
            grid[ask][k] = val[k]
        ask += 1
    
    # my so-long tester grid
    '''sl_grid = [['2', '5', '9', '7', '1', '6', '4', '8', '3'], ['8', '6', '7', '3', '4', '5', '9', '1', '2'], ['4', '1', '3', '9', '2', '8', '6', '7', '5'], ['3', '9', '8', '5', '7', '4', '1', '2', '6'], ['5', '4', '6', '2', '8', '1', '7', '3', '9'], ['1', '7', '2', '6', '3', '9', '5', '4', '8'], ['9', '8', '4', '1', '6', '3', '2', '5', '7'], ['6', '2', '1', '8', '5', '7', '3', '9', '4'], ['7', '3', '5', '4', '9', '2', '8', '6', '1']]'''    
        
    return grid
    #return sl_grid

def create_sub_grid():
    sub_grids = []
    for sub_grid_blocks in range(9):
        for blocks in range(3):
            sub_grids.append([0]*3)
    return print(sub_grids)

def sudoku_checker(grid):
    '''Program which checks if a Sudoku grid is valid'''
    all_nums = ""
    for row in range(9):
        for column in range(9):
            val_col = column+1
            val_row = row+1
            
            # Checks if each row is valid
            while val_col < 9:
                if grid[row][column] == grid[row][val_col]:
                    return print("Sudoku grid is not valid")
                val_col += 1
                
                # Checks if each column is valid
            while val_row < 9:
                if grid[column][row] == grid[column][val_row]:
                    return print("Sudoku grid is not valid") 
                val_row +=1
                
            all_nums += grid[row][column]
            
            
    print(all_nums)
    sub_grids = []        
    for w in range(9):
        sub_grids.append(create_sub_grid())
        
    #all_nums = ""    
    #for g in range(9):
        #for h in grid[g]:
            #all_nums += str(h)
            
    #print(all_nums)
    #for f in range(len(all_nums)):
        #if (f > 0 and f < 3) or (f > 0 and f < 3) or (f > 0 and f < 3)
    #while p < 9:
        #q = 0
        #while q < 3:
            #z = 0
            #while z < 3:
                #sub_grids[p]
    
    #for p in range(9):
        #for q in range(3):
            #for z in range(3):
                #sub_grids[p][q][z] = grid[p][z]
                
    #print(grid)
    #print()
    #print(sub_grids)
    #sub_dict = {}
    #for t in range(1,10):
        #sub_dict["sub_list" + str(t)] = create_sub_grid()
    
    #print(sub_dict['sub_list1'])
    
    #for s in range(9):
        #for q in range(9):
            #while s < 3 and q < 3:
                #sub_dict['sub_list1'][s][q] = grid[s][q]
                #continue
                
    #print(sub_dict['sub_list1'])
            
                
       
    
    print("Sudoku grid is valid")
    
    
if __name__ == '__main__':
    sudoku_checker(create_grid())