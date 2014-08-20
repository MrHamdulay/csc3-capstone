# Push module for 2048 game
# James Behr
# 2014-04-30

def push_up (grid):
    """merge grid values upwards"""
    # Move across columns, then down rows, as we're moving vertically
    for x in range(4):
        for y1 in range(4):
            # go over each cell
            canadd = True
            
            for y2 in range(y1 + 1, 4):
                # go over each cell after the one we're on (look ahead)
                if grid[y2][x] == 0:
                    continue
                
                # If we reach this point, we're on a non-zero cell
                if grid[y1][x] == grid[y2][x] and canadd:
                    # if the cells are equal, add them and erase look ahead cell
                    grid[y1][x] += grid[y2][x]
                    grid[y2][x] = 0
                    break
                elif grid[y1][x] != grid[y2][x] and grid[y1][x] and grid[y2][x]:
                    # There is another non-equal and non-zero number in the way, thus we can't add
                    canadd = False
                    
                if grid[y1][x] == 0:
                    # if the cell is zero, move the look ahead cell
                    grid[y1][x] = grid[y2][x]
                    grid[y2][x] = 0

# The other functions work the same, no need to comment
def push_down (grid):
    """merge grid values downwards"""
    # Move across columns, then down rows, as we're moving vertically
    for x in range(4):
        for y1 in range(3, -1, -1):
            # go over each cell
            canadd = True
            
            for y2 in range(y1 - 1, -1, -1):
                # go over each cell after the one we're on (look ahead)
                if grid[y2][x] == 0:
                    # we use 4 - x in order to start at bottom-most cell
                    continue
                
                # If we reach this point, we're on a non-zero cell
                if grid[y1][x] == grid[y2][x] and canadd:
                    # if the cells are equal, add them and erase look ahead cell
                    grid[y1][x] += grid[y2][x]
                    grid[y2][x] = 0
                    break
                elif grid[y1][x] != grid[y2][x] and grid[y1][x] and grid[y2][x]:
                    # There is another non-equal and non-zero number in the way, thus we can't add
                    canadd = False
                    
                if grid[y1][x] == 0:
                    # if the cell is zero, move the look ahead cell
                    grid[y1][x] = grid[y2][x]
                    grid[y2][x] = 0

                                
def push_left (grid):
    """merge grid values left"""
    # Move down rows, then across columns, as we're moving horizontally
    for y in range(4):
        for x1 in range(4):
            # go over each cell
            canadd = True
            
            for x2 in range(x1 + 1, 4):
                # go over each cell after the one we're on (look ahead)
                if grid[y][x2] == 0:
                    continue
                
                # If we reach this point, we're on a non-zero cell
                if grid[y][x1] == grid[y][x2] and canadd:
                    # if the cells are equal, add them and erase look ahead cell
                    grid[y][x1] += grid[y][x2]
                    grid[y][x2] = 0
                    break
                elif grid[y][x1] != grid[y][x2] and grid[y][x1] and grid[y][x2]:
                    # There is another non-equal and non-zero number in the way, thus we can't add
                    canadd = False
                    
                if grid[y][x1] == 0:
                    # if the cell is zero, move the look ahead cell
                    grid[y][x1] = grid[y][x2]
                    grid[y][x2] = 0

def push_right (grid):
    """merge grid values right"""
    # Move down rows, then across columns, as we're moving horizontally
    for y in range(4):
        for x1 in range(3, -1, -1):
            # go over each cell
            canadd = True
            
            for x2 in range(x1 - 1, -1, -1):
                # go over each cell after the one we're on (look ahead)
                if grid[y][x2] == 0:
                    continue
                
                # If we reach this point, we're on a non-zero cell
                if grid[y][x1] == grid[y][x2] and canadd:
                    # if the cells are equal, add them and erase look ahead cell
                    grid[y][x1] += grid[y][x2]
                    grid[y][x2] = 0
                    break
                elif grid[y][x1] != grid[y][x2] and grid[y][x1] and grid[y][x2]:
                    # There is another non-equal and non-zero number in the way, thus we can't add
                    canadd = False
                    
                if grid[y][x1] == 0:
                    # if the cell is zero, move the look ahead cell
                    grid[y][x1] = grid[y][x2]
                    grid[y][x2] = 0