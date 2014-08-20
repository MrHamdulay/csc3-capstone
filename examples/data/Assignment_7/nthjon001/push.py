"""merging functions for 2048 game
Jonathan Nathan
27 April 2014"""

def push_up(grid):
    """merge grid values upwards"""
    
    # shifts numbers in columns upwards, for each of the 16 combinations of four numbers in a column of height 4
    for i in range (4):
        
        if grid[0][i] == 0 and grid[1][i] == 0 and grid[2][i] == 0 and grid[3][i] == 0:
            continue
        
        elif grid[0][i] != 0 and grid[1][i] == 0 and grid[2][i] == 0 and grid[3][i] == 0:
            continue
        
        elif grid[0][i] == 0 and grid[1][i] != 0 and grid[2][i] == 0 and grid[3][i] == 0:
            grid[0][i] = grid[1][i]
            grid[1][i] = 0
            
        elif grid[0][i] == 0 and grid[1][i] == 0 and grid[2][i] != 0 and grid[3][i] == 0:
            grid[0][i] = grid[2][i]
            grid[2][i] = 0
            
        elif grid[0][i] == 0 and grid[1][i] == 0 and grid[2][i] == 0 and grid[3][i] != 0:
            grid[0][i] = grid[3][i]
            grid[3][i] = 0
            
        elif grid[0][i] != 0 and grid[1][i] != 0 and grid[2][i] == 0 and grid[3][i] == 0:
            continue
        
        elif grid[0][i] != 0 and grid[1][i] == 0 and grid[2][i] != 0 and grid[3][i] == 0:
            grid[1][i] = grid[2][i]
            grid[2][i] = 0
            
        elif grid[0][i] != 0 and grid[1][i] == 0 and grid[2][i] == 0 and grid[3][i] != 0:
            grid[1][i] = grid[3][i]
            grid[3][i] = 0
            
        elif grid[0][i] == 0 and grid[1][i] != 0 and grid[2][i] != 0 and grid[3][i] == 0:
            grid[0][i] = grid[1][i]
            grid[1][i] = grid[2][i]
            grid[2][i] = 0
            
        elif grid[0][i] == 0 and grid[1][i] != 0 and grid[2][i] == 0 and grid[3][i] != 0:
            grid[0][i] = grid[1][i]
            grid[1][i] = grid[3][i]
            grid[3][i] = 0
            
        elif grid[0][i] == 0 and grid[1][i] == 0 and grid[2][i] != 0 and grid[3][i] != 0:
            grid[0][i] = grid[2][i]
            grid[1][i] = grid[3][i]
            grid[2][i] = 0
            grid[3][i] = 0
            
        elif grid[0][i] != 0 and grid[1][i] != 0 and grid[2][i] != 0 and grid[3][i] == 0:
            continue
        
        elif grid[0][i] != 0 and grid[1][i] == 0 and grid[2][i] != 0 and grid[3][i] != 0:
            grid[1][i] = grid[2][i]
            grid[2][i] = grid[3][i]
            grid[3][i] = 0
            
        elif grid[0][i] == 0 and grid[1][i] != 0 and grid[2][i] != 0 and grid[3][i] != 0:
            grid[0][i] = grid[1][i]
            grid[1][i] = grid[2][i]
            grid[2][i] = grid[3][i]
            grid[3][i] = 0
            
        elif grid[0][i] != 0 and grid[1][i] != 0 and grid[2][i] != 0 and grid[3][i] != 0:
            continue
        
        elif grid[0][i] != 0 and grid[1][i] != 0 and grid[2][i] == 0 and grid[3][i] != 0:
            grid[2][i] = grid[3][i]
            grid[3][i] = 0
        
    # sums identical numbers on top of each other        
    for i in range(4):
        
        # sums columns with two identical numbers only
        if grid[0][i] == grid[1][i] and grid[0][i] != 0 and grid[2][i] == 0 and grid[3][i] == 0:
            grid[0][i] = grid[0][i] + grid[1][i]
            grid[1][i] = 0
            
        # sums columns with three numbers, and two identical numbers
        elif grid[0][i] == grid[1][i] and grid[0][i] != 0 and grid[2][i] != 0 and grid[3][i] == 0:
            grid[0][i] = grid[0][i] + grid[1][i]
            grid[1][i] = grid[2][i]
            grid[2][i] = 0
            
        # sums columns with three numbers, and two identical numbers
        elif grid[1][i] == grid[2][i] and grid[1][i] != 0 and grid[0][i] != 0 and grid[3][i] == 0:
            grid[1][i] = grid[1][i] + grid[2][i]
            grid[2][i] = 0
        
        # sums columns with four numbers, two sets of identical pairs
        elif grid[0][i] == grid[1][i] and grid[0][i] != 0 and grid[2][i] == grid[3][i] and grid[2][i] != 0:
            grid[0][i] = grid[0][i] + grid[1][i]
            grid[1][i] = grid[2][i] + grid[3][i]
            grid[2][i] = 0
            grid[3][i] = 0
        
        # sums columns with four numbers, one pair of identical numbers    
        elif grid[0][i] == grid[1][i] and grid[0][i] != 0 and grid[2][i] != 0 and grid[3][i] != 0:
            grid[0][i] = grid[0][i] + grid[1][i]
            grid[1][i] = grid[2][i]
            grid[2][i] = grid[3][i]
            grid[3][i] = 0
        
        # sums columns with four numbers, one pair of identical numbers
        elif grid[1][i] == grid[2][i] and grid[1][i] != 0 and grid[0][i] != 0 and grid[3][i] != 0:
            grid[1][i] = grid[1][i] + grid[2][i]
            grid[2][i] = grid[3][i]
            grid[3][i] = 0
            
        # sums columns with four numbers, one pair of identical numbers
        elif grid[2][i] == grid[3][i] and grid[2][i] != 0 and grid[0][i] != 0 and grid[1][i] != 0:
            grid[2][i] = grid[2][i] + grid[3][i] 
            grid[3][i] = 0
        
            
def push_down(grid):
    """merge grid values downwards"""
    
    # shifts numbers in columns downwards, for each of the 16 combinations of four numbers in a column of height 4
    for i in range (4):
            
        if grid[0][i] == 0 and grid[1][i] == 0 and grid[2][i] == 0 and grid[3][i] == 0:
            continue
            
        elif grid[0][i] != 0 and grid[1][i] == 0 and grid[2][i] == 0 and grid[3][i] == 0:
            grid[3][i] = grid[0][i] 
            grid[0][i] = 0
            
        elif grid[0][i] == 0 and grid[1][i] != 0 and grid[2][i] == 0 and grid[3][i] == 0:
            grid[3][i] = grid[1][i]
            grid[1][i] = 0
                
        elif grid[0][i] == 0 and grid[1][i] == 0 and grid[2][i] != 0 and grid[3][i] == 0:
            grid[3][i] = grid[2][i]
            grid[2][i] = 0
                
        elif grid[0][i] == 0 and grid[1][i] == 0 and grid[2][i] == 0 and grid[3][i] != 0:
            continue
                
        elif grid[0][i] != 0 and grid[1][i] != 0 and grid[2][i] == 0 and grid[3][i] == 0:
            grid[3][i] = grid[1][i]
            grid[2][i] = grid[0][i]
            grid[0][i] = 0
            grid[1][i] = 0
            
        elif grid[0][i] != 0 and grid[1][i] == 0 and grid[2][i] != 0 and grid[3][i] == 0:
            grid[3][i] = grid[2][i]
            grid[2][i] = grid[0][i]
            grid[0][i] = 0
                
        elif grid[0][i] != 0 and grid[1][i] == 0 and grid[2][i] == 0 and grid[3][i] != 0:
            grid[2][i] = grid[0][i]
            grid[0][i] = 0
                
        elif grid[0][i] == 0 and grid[1][i] != 0 and grid[2][i] != 0 and grid[3][i] == 0:
            grid[3][i] = grid[2][i]
            grid[2][i] = grid[1][i]
            grid[1][i] = 0
                
        elif grid[0][i] == 0 and grid[1][i] != 0 and grid[2][i] == 0 and grid[3][i] != 0:
            grid[2][i] = grid[1][i]
            grid[1][i] = 0
                
        elif grid[0][i] == 0 and grid[1][i] == 0 and grid[2][i] != 0 and grid[3][i] != 0:
            continue
                
        elif grid[0][i] != 0 and grid[1][i] != 0 and grid[2][i] != 0 and grid[3][i] == 0:
            grid[3][i] = grid[2][i]
            grid[2][i] = grid[1][i]
            grid[1][i] = grid[0][i]
            grid[0][i] = 0
            
        elif grid[0][i] != 0 and grid[1][i] == 0 and grid[2][i] != 0 and grid[3][i] != 0:
            grid[1][i] = grid[0][i]
            grid[0][i] = 0
                
        elif grid[0][i] == 0 and grid[1][i] != 0 and grid[2][i] != 0 and grid[3][i] != 0:
            continue
                
        elif grid[0][i] != 0 and grid[1][i] != 0 and grid[2][i] != 0 and grid[3][i] != 0:
            continue
            
        elif grid[0][i] != 0 and grid[1][i] != 0 and grid[2][i] == 0 and grid[3][i] != 0:
            grid[2][i] = grid[1][i]
            grid[1][i] = grid[0][i]
            grid[0][i] = 0
            
        # sums identical numbers on top of each other        
    for i in range(4):
            
        # sums columns with two identical numbers only
        if grid[3][i] == grid[2][i] and grid[3][i] != 0 and grid[0][i] == 0 and grid[1][i] == 0:
            grid[3][i] = grid[3][i] + grid[2][i]
            grid[2][i] = 0
                
        # sums columns with three numbers, and two identical numbers
        elif grid[3][i] == grid[2][i] and grid[3][i] != 0 and grid[1][i] != 0 and grid[0][i] == 0:
            grid[3][i] = grid[3][i] + grid[2][i]
            grid[2][i] = grid[1][i]
            grid[1][i] = 0
                
        # sums columns with three numbers, and two identical numbers
        elif grid[2][i] == grid[1][i] and grid[2][i] != 0 and grid[3][i] != 0 and grid[0][i] == 0:
            grid[2][i] = grid[2][i] + grid[1][i]
            grid[1][i] = 0
            
        # sums columns with four numbers, two sets of identical pairs
        elif grid[0][i] == grid[1][i] and grid[0][i] != 0 and grid[2][i] == grid[3][i] and grid[2][i] != 0:
            grid[3][i] = grid[3][i] + grid[2][i]
            grid[2][i] = grid[1][i] + grid[0][i]
            grid[1][i] = 0
            grid[0][i] = 0
            
        # sums columns with four numbers, one pair of identical numbers    
        elif grid[3][i] == grid[2][i] and grid[3][i] != 0 and grid[0][i] != 0 and grid[1][i] != 0:
            grid[3][i] = grid[3][i] + grid[2][i]
            grid[2][i] = grid[1][i]
            grid[1][i] = grid[0][i]
            grid[0][i] = 0
            
        # sums columns with four numbers, one pair of identical numbers
        elif grid[1][i] == grid[2][i] and grid[1][i] != 0 and grid[0][i] != 0 and grid[3][i] != 0:
            grid[2][i] = grid[2][i] + grid[1][i]
            grid[1][i] = grid[0][i]
            grid[0][i] = 0
                
        # sums columns with four numbers, one pair of identical numbers
        elif grid[0][i] == grid[1][i] and grid[0][i] != 0 and grid[2][i] != 0 and grid[3][i] != 0:
            grid[1][i] = grid[1][i] + grid[0][i] 
            grid[0][i] = 0    
            
    
def push_left(grid):
    """merge grid values left"""
    
    # shifts numbers in rows leftwards, for each of the 16 combinations of four numbers in a row of width 4
    for i in range (4):
        
        if grid[i][0] == 0 and grid[i][1] == 0 and grid[i][2] == 0 and grid[i][3] == 0:
            continue
        
        elif grid[i][0] != 0 and grid[i][1] == 0 and grid[i][2] == 0 and grid[i][3] == 0:
            continue
        
        elif grid[i][0] == 0 and grid[i][1] != 0 and grid[i][2] == 0 and grid[i][3] == 0:
            grid[i][0] = grid[i][1]
            grid[i][1] = 0
            
        elif grid[i][0] == 0 and grid[i][1] == 0 and grid[i][2] != 0 and grid[i][3] == 0:
            grid[i][0] = grid[i][2]
            grid[i][2] = 0
            
        elif grid[i][0] == 0 and grid[i][1] == 0 and grid[i][2] == 0 and grid[i][3] != 0:
            grid[i][0] = grid[i][3]
            grid[i][3] = 0
            
        elif grid[i][0] != 0 and grid[i][1] != 0 and grid[i][2] == 0 and grid[i][3] == 0:
            continue
        
        elif grid[i][0] != 0 and grid[i][1] == 0 and grid[i][2] != 0 and grid[i][3] == 0:
            grid[i][1] = grid[i][2]
            grid[i][2] = 0
            
        elif grid[i][0] != 0 and grid[i][1] == 0 and grid[i][2] == 0 and grid[i][3] != 0:
            grid[i][1] = grid[i][3]
            grid[i][3] = 0
            
        elif grid[i][0] == 0 and grid[i][1] != 0 and grid[i][2] != 0 and grid[i][3] == 0:
            grid[i][0] = grid[i][1]
            grid[i][1] = grid[i][2]
            grid[i][2] = 0
            
        elif grid[i][0] == 0 and grid[i][1] != 0 and grid[i][2] == 0 and grid[i][3] != 0:
            grid[i][0] = grid[i][1]
            grid[i][1] = grid[i][3]
            grid[i][3] = 0
            
        elif grid[i][0] == 0 and grid[i][1] == 0 and grid[i][2] != 0 and grid[i][3] != 0:
            grid[i][0] = grid[i][2]
            grid[i][1] = grid[i][3]
            grid[i][2] = 0
            grid[i][3] = 0
            
        elif grid[i][0] != 0 and grid[i][1] != 0 and grid[i][2] != 0 and grid[i][3] == 0:
            continue
        
        elif grid[i][0] == 0 and grid[i][1] != 0 and grid[i][2] != 0 and grid[i][3] != 0:
            grid[i][0] = grid[i][1]
            grid[i][1] = grid[i][2]
            grid[i][2] = grid[i][3]
            grid[i][3] = 0
            
        elif grid[i][0] != 0 and grid[i][1] == 0 and grid[i][2] != 0 and grid[i][3] != 0:
            grid[i][1] = grid[i][2]
            grid[i][2] = grid[i][3]
            grid[i][3] = 0
            
        elif grid[i][0] != 0 and grid[i][1] != 0 and grid[i][2] == 0 and grid[i][3] != 0:
            grid[i][2] = grid[i][3]
            grid[i][3] = 0
            
        elif grid[i][0] != 0 and grid[i][1] != 0 and grid[i][2] != 0 and grid[i][3] != 0:
            continue
        
    # sums identical numbers horizontally next to each other
    for i in range (4):
        
        # sums rows with two identical numbers only
        if grid[i][0] == grid[i][1] and grid[i][0] != 0 and grid[i][2] == 0 and grid[i][3] == 0:
            grid[i][0] = grid[i][0] + grid[i][1]
            grid[i][1] = 0
            
        # sums rows with three numbers, and two identical numbers
        elif grid[i][0] == grid[i][1] and grid[i][0] != 0 and grid[i][2] != 0 and grid[i][3] == 0:
            grid[i][0] = grid[i][0] + grid[i][1]
            grid[i][1] = grid[i][2]
            grid[i][2] = 0
            
        # sums rows with three numbers, and two identical numbers
        elif grid[i][1] == grid[i][2] and grid[i][1] != 0 and grid[i][0] != 0 and grid[i][3] == 0: 
            grid[i][1] = grid[i][1] + grid[i][2]
            grid[i][2] = 0
            
        
        # sums rows with four numbers, two sets of identical pairs
        elif grid[i][0] == grid[i][1] and grid[i][0] != 0 and grid[i][2] == grid[i][3] and grid[i][2] != 0:
            grid[i][0] = grid[i][0] + grid[i][1]
            grid[i][1] = grid[i][2] + grid[i][3]
            grid[i][2] = 0
            grid[i][3] = 0
            
        # sums rows with four numbers, one pair of identical numbers
        elif grid[i][0] == grid[i][1] and grid[i][0] != 0 and grid[i][2] != 0 and grid[i][3] != 0:
            grid[i][0] = grid[i][0] + grid[i][1]
            grid[i][1] = grid[i][2]
            grid[i][2] = grid[i][3]
            grid[i][3] = 0
            
        # sums rows with four numbers, one pair of identical numbers
        elif grid[i][1] == grid[i][2] and grid[i][1] != 0 and grid[i][0] != 0 and grid[i][3] != 0:
            grid[i][1] = grid[i][1] + grid[i][2]
            grid[i][2] = grid[i][3]
            grid[i][3] = 0
            
        # sums rows with four numbers, one pair of identical numbers
        elif grid[i][2] == grid[i][3] and grid[i][2] != 0 and grid[i][0] != 0 and grid[i][1] != 0:
            grid[i][2] = grid[i][2] + grid[i][3]
            grid[i][3] = 0
            
            
def push_right(grid):
    """merge grid values right"""
    
    # shifts numbers in rows rightwards, for each of the 16 combinations of four numbers in a row of width 4
    for i in range (4):
        if grid[i][0] == 0 and grid[i][1] == 0 and grid[i][2] == 0 and grid[i][3] == 0:
            continue
                
        elif grid[i][0] != 0 and grid[i][1] == 0 and grid[i][2] == 0 and grid[i][3] == 0:
            grid[i][3] = grid[i][0]
            grid[i][0] = 0
                
        elif grid[i][0] == 0 and grid[i][1] != 0 and grid[i][2] == 0 and grid[i][3] == 0:
            grid[i][3] = grid[i][1]
            grid[i][1] = 0
                    
        elif grid[i][0] == 0 and grid[i][1] == 0 and grid[i][2] != 0 and grid[i][3] == 0:
            grid[i][3] = grid[i][2]
            grid[i][2] = 0
                    
        elif grid[i][0] == 0 and grid[i][1] == 0 and grid[i][2] == 0 and grid[i][3] != 0:
            continue
                    
        elif grid[i][0] != 0 and grid[i][1] != 0 and grid[i][2] == 0 and grid[i][3] == 0:
            grid[i][3] = grid[i][1]
            grid[i][2] = grid[i][0]
            grid[i][1] = 0
            grid[i][0] = 0
        
        elif grid[i][0] != 0 and grid[i][1] == 0 and grid[i][2] != 0 and grid[i][3] == 0:
            grid[i][3] = grid[i][2]
            grid[i][2] = grid[i][0]
            grid[i][0] = 0
                    
        elif grid[i][0] != 0 and grid[i][1] == 0 and grid[i][2] == 0 and grid[i][3] != 0:
            grid[i][2] = grid[i][0]
            grid[i][0] = 0
                    
        elif grid[i][0] == 0 and grid[i][1] != 0 and grid[i][2] != 0 and grid[i][3] == 0:
            grid[i][3] = grid[i][2]
            grid[i][2] = grid[i][1]
            grid[i][1] = 0
                    
        elif grid[i][0] == 0 and grid[i][1] != 0 and grid[i][2] == 0 and grid[i][3] != 0:
            grid[i][2] = grid[i][1]
            grid[i][1] = 0
                    
        elif grid[i][0] == 0 and grid[i][1] == 0 and grid[i][2] != 0 and grid[i][3] != 0:
            continue
            
        elif grid[i][0] != 0 and grid[i][1] != 0 and grid[i][2] != 0 and grid[i][3] == 0:
            grid[i][3] = grid[i][2]
            grid[i][2] = grid[i][1] 
            grid[i][1] = grid[i][0]
            grid[i][0] = 0
                
        elif grid[i][0] == 0 and grid[i][1] != 0 and grid[i][2] != 0 and grid[i][3] != 0:
            continue
                    
        elif grid[i][0] != 0 and grid[i][1] == 0 and grid[i][2] != 0 and grid[i][3] != 0:
            grid[i][1] = grid[i][0]
            grid[i][0] = 0
                    
        elif grid[i][0] != 0 and grid[i][1] != 0 and grid[i][2] == 0 and grid[i][3] != 0:
            grid[i][2] = grid[i][1]
            grid[i][1] = grid[i][0]
            grid[i][0] = 0
            
        elif grid[i][0] != 0 and grid[i][1] != 0 and grid[i][2] != 0 and grid[i][3] != 0:
            continue
        
    # sums identical numbers horizontally next to each other
    for i in range (4):
                
        # sums rows with two identical numbers only
        if grid[i][3] == grid[i][2] and grid[i][3] != 0 and grid[i][1] == 0 and grid[i][0] == 0:
            grid[i][3] = grid[i][3] + grid[i][2]
            grid[i][2] = 0
            
        # sums rows with three numbers, and two identical numbers
        elif grid[i][3] == grid[i][2] and grid[i][3] != 0 and grid[i][1] != 0 and grid[i][0] == 0:
            grid[i][3] = grid[i][3] + grid[i][2]
            grid[i][2] = grid[i][1]
            grid[i][1] = 0
                    
        # sums rows with three numbers, and two identical numbers
        elif grid[i][2] == grid[i][1] and grid[i][2] != 0 and grid[i][3] != 0 and grid[i][0] == 0: 
            grid[i][2] = grid[i][2] + grid[i][1]
            grid[i][1] = 0
                    
                
        # sums rows with four numbers, two sets of identical pairs
        elif grid[i][0] == grid[i][1] and grid[i][0] != 0 and grid[i][2] == grid[i][3] and grid[i][2] != 0:
            grid[i][3] = grid[i][3] + grid[i][2]
            grid[i][2] = grid[i][1] + grid[i][0]
            grid[i][1] = 0
            grid[i][0] = 0
                    
        # sums rows with four numbers, one pair of identical numbers
        elif grid[i][0] == grid[i][1] and grid[i][0] != 0 and grid[i][2] != 0 and grid[i][3] != 0:
            grid[i][1] = grid[i][1] + grid[i][0]
            grid[i][0] = 0
                    
        # sums rows with four numbers, one pair of identical numbers
        elif grid[i][1] == grid[i][2] and grid[i][1] != 0 and grid[i][0] != 0 and grid[i][3] != 0:
            grid[i][2] = grid[i][2] + grid[i][1]
            grid[i][1] = grid[i][0]
            grid[i][0] = 0
            
        # sums rows with four numbers, one pair of identical numbers
        elif grid[i][2] == grid[i][3] and grid[i][2] != 0 and grid[i][0] != 0 and grid[i][1] != 0:
            grid[i][3] = grid[i][3] + grid[i][2]
            grid[i][2] = grid[i][1]
            grid[i][1] = grid[i][0]
            grid[i][0] = 0